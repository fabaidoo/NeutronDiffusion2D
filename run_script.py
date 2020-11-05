#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:43:51 2020

@author: fabaidoo
"""
from neutrondiffusion import neutrondiffusion

#REFLECTOR
## Vacuum
#### ratio = 1e01
'''
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'vacuum', bigsquare=.1, smallsquare=.01)
fig[0].savefig('bottom_v10_ref.png')
fig[1].savefig('diag_v10_ref.png')
'''

#### ratio = 1e02
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'vacuum', bigsquare=1, smallsquare=.01)
fig[0].savefig('bottom_v100_ref.png')
fig[1].savefig('diag_v100_ref.png')

#### ratio = 1e03
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'vacuum', bigsquare=10, smallsquare=.01, 
                       basis = 'spline')
fig[0].savefig('bottom_v1000_ref.png')
fig[1].savefig('diag_v1000_ref.png')


#### ratio = 1e04
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'vacuum', bigsquare=100, smallsquare=.01,
                       basis = 'spline')
fig[0].savefig('bottom_v10000_ref.png')
fig[1].savefig('diag_v10000_ref.png')


## Reflecting
#### ratio = 1e01
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'reflecting', bigsquare=.1, smallsquare=.01)
fig[0].savefig('bottom_r10_ref.png')
fig[1].savefig('diag_r10_ref.png')


#### ratio = 1e02
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'reflecting', bigsquare=1, smallsquare=.01)
fig[0].savefig('bottom_r100_ref.png')
fig[1].savefig('diag_r100_ref.png')


#### ratio = 1e03
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'reflecting', bigsquare=10, smallsquare=.01,
                       basis= 'spline')
fig[0].savefig('bottom_r1000_ref.png')
fig[1].savefig('diag_r1000_ref.png')

#### ratio = 1e04
fig = neutrondiffusion(mat_flag = 'reflector', BC_flag = 'reflecting', bigsquare=100, smallsquare=.01,
                       basis= 'spline')
fig[0].savefig('bottom_r10000_ref.png')
fig[1].savefig('diag_r10000_ref.png')

#SCATTERER
## Vacuum
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04

## Reflecting
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04



#ABSORBER
## Vacuum
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04

## Reflecting
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04


#AIR
## Vacuum
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04

## Reflecting
#### ratio = 1e01

#### ratio = 1e02

#### ratio = 1e03

#### ratio = 1e04



