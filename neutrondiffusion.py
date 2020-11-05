from nutils import function, mesh, solver, topology, element
import matplotlib.pyplot as plt

def neutrondiffusion(mat_flag = 'scatterer', BC_flag = 'vacuum',bigsquare = 1, smallsquare = .1, degree = 1,
                     basis = 'lagrange'):
                     
    W = bigsquare #width of outer box
    Wi = smallsquare #width of inner box

    nelems = int((2 * 1 * W/Wi)) 
    
    if mat_flag == 'scatterer':
        sigt = 2
        sigs = 1.99
    elif mat_flag == 'reflector':
        sigt = 2
        sigs = 1.8
    elif mat_flag == 'absorber':
        sigt = 10
        sigs = 2
    elif mat_flag == 'air':
        sigt = .01
        sigs = .006
    
    topo, geom = mesh.unitsquare(nelems, 'square') #unit square centred at (0.5, 0.5)
    ns = function.Namespace()
    ns.basis = topo.basis(basis, degree = degree)
    
    ns.x = W * geom #scales the unit square to our physical square
    ns.f =function.max(function.abs(ns.x[0] -  W/2), function.abs(ns.x[1] - W/2)) #level set function for inner square 
    
    inner, outer = function.partition(ns.f, Wi / 2) #indicator function for inner square and outer square

    ns.phi = 'basis_A ?dofs_A'
    ns.SIGs  = sigs * outer              #scattering cross-section
    ns.SIGt  = 0.1 * inner + sigt* outer              #total cross-section
    ns.SIGa = 'SIGt - SIGs' #absorption cross-section
    ns.D = '1 / (3 SIGt)'   #diffusion co-efficient
    ns.Q =  inner #source term

    if BC_flag == 'vacuum':
        sqr = topo.boundary.integral('(phi - 0)^2 J(x)' @ns, degree = degree * 2)
        cons = solver.optimize('dofs', sqr, droptol=1e-14) #this applies the boundary condition to u
    
        #residual
        res = topo.integral( '(D basis_i,j phi_,j + SIGa basis_i phi - basis_i Q) J(x)' @ ns, degree = degree * 2) 
    
        #solve for degrees of freedom
        dofs = solver.solve_linear('dofs', res, constrain = cons)
    
    elif BC_flag == 'reflecting':
        #residual
        res = topo.integral( '(D basis_i,j phi_,j + SIGa basis_i phi - basis_i Q) J(x)' @ ns, degree = degree * 2) 
        
        #solve for degrees of freedom
        dofs = solver.solve_linear('dofs', res)
    
    #select lower triangular half of square domain. Diagonal is one of its boundaries
    triang = topo.trim('x_0 - x_1' @ns, maxrefine=5)
    triangbnd = triang.boundary #select boundary of lower triangle 
    # eval the vertices of the boundary elements of lower triangle:
    verts = triangbnd.sample(*element.parse_legacy_ischeme("vertex")).eval('x_i' @ns)
    # now select the verts of the boundary
    diag = topology.SubsetTopology(triangbnd, [triangbnd.references[i]
                                               if (verts[2*i][0] == verts[2*i][1] and verts[2*i+1][0] == verts[2*i+1][1] )
                                               else triangbnd.references[i].empty
                                               for i in range(len(triangbnd.references))])
    bezier_diag = diag.sample('bezier', degree + 1)
    x_diag = bezier_diag.eval('(x_0^2 + x_1^2)^(1 / 2)' @ns)
    phi_diag = bezier_diag.eval('phi' @ ns, dofs = dofs)
    
    bezier_bottom = topo.boundary['bottom'].sample('bezier', degree + 1)
    x_bottom = bezier_bottom.eval('x_0' @ns)
    phi_bottom = bezier_bottom.eval('phi' @ns, dofs = dofs)
    
    fig_bottom = plt.figure(0)
    ax_bottom = fig_bottom.add_subplot(111) 
    plt.plot(x_bottom, phi_bottom)
    ax_bottom.set_title('Scalar flux along bottom for %s with %s BCs'%(mat_flag, BC_flag))
    ax_bottom.set_xlabel('x')
    ax_bottom.set_ylabel('$\\phi(x)$')
    
    
    fig_diag = plt.figure(1)
    ax_diag = fig_diag.add_subplot(111)
    plt.plot(x_diag, phi_diag)
    ax_diag.set_title('Scalar flux along diagonal for %s with %s BCs'%(mat_flag, BC_flag))
    ax_diag.set_xlabel('$\\sqrt{x^2 + y^2}$')
    ax_diag.set_ylabel('$\\phi(x = y)$')
    
    return fig_bottom, fig_diag
    
    

    

