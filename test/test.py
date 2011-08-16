#!/usr/bin/env python
"""This module provides some tests for the GeoSolver. 
The tests are also simple examples of how to use of the GeomSolver API"""

from geosolver.geometric import *
from geosolver.vector import vector 
from geosolver.randomproblem import *
from geosolver.diagnostic import diag_select, diag_print
import geosolver.tolerance as tolerance
from time import time

# ---------- 3D problems -----

def fix3_problem_3d():
    """A problem with a fix constraint"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.0, 0.0, 1.0]))
    #problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    #problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    #problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(FixConstraint('v1', vector([0.0,0.0,0.0])))
    problem.add_constraint(FixConstraint('v2', vector([10.0,0.0,0.0])))
    problem.add_constraint(FixConstraint('v3', vector([5.0,5.0,0.0])))
    return problem

def fix2_problem_3d():
    """A problem with a fix constraint"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.0, 0.0, 1.0]))
    #problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(FixConstraint('v1', vector([0.0,0.0,0.0])))
    problem.add_constraint(FixConstraint('v2', vector([10.0,0.0,0.0])))
    return problem

def fix1_problem_3d():
    """A problem with a fix constraint"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.0, 0.0, 1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(FixConstraint('v1', vector([0.0,0.0,0.0])))
    return problem


    
def double_banana_problem():
    """The double banana problem"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))
    
    problem.add_point('w1', vector([0.0, 0.0, 0.0]))
    problem.add_point('w2', vector([1.0, 0.0, 0.0]))
    problem.add_point('w3', vector([0.0, 1.0, 0.0]))
    problem.add_constraint(DistanceConstraint('w1', 'w2', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'w3', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'w3', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('w3', 'v5', 10.0))
    
    return problem

def double_banana_plus_one_problem():
    """The double banana problem, plus one constraint (well-constrained)"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))
    
    problem.add_point('w1', vector([0.0, 0.0, 0.0]))
    problem.add_point('w2', vector([1.0, 0.0, 0.0]))
    problem.add_point('w3', vector([0.0, 1.0, 0.0]))
    problem.add_constraint(DistanceConstraint('w1', 'w2', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'w3', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'w3', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('w1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('w2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('w3', 'v5', 10.0))
   
    problem.add_constraint(DistanceConstraint('v1', 'w1', 10.0))
 
    return problem


def double_tetrahedron_problem():
    """The double tetrahedron problem"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))
    return problem


def dad_tetrahedron_problem():
    """The double tetrahedron problem with an angle"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(AngleConstraint('v2', 'v1','v3', 60.0*math.pi/180.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))
    return problem

def ada_tetrahedron_problem():
    """The double tetrahedron problem with an angle"""
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(AngleConstraint('v3', 'v1','v2', 60.0*math.pi/180.0))
    problem.add_constraint(AngleConstraint('v1', 'v2','v3', 60.0*math.pi/180.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))
    return problem

def ada_3d_problem():
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',distance_2p(problem.get_point('v1'), problem.get_point('v2'))))
    problem.add_constraint(AngleConstraint('v3', 'v1', 'v2', 
       angle_3p(problem.get_point('v3'), problem.get_point('v1'), problem.get_point('v2'))
    ))
    problem.add_constraint(AngleConstraint('v1', 'v2', 'v3',
       angle_3p(problem.get_point('v1'), problem.get_point('v2'), problem.get_point('v3'))
    ))
    return problem




def overconstrained_tetra():
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    # overconstrain me!
    problem.add_constraint(AngleConstraint('v1', 'v2', 'v3', math.pi/3))
    #problem.add_constraint(AngleConstraint('v1', 'v2', 'v3', math.pi/4))
    return problem

def diamond_3d():
    """creates a diamond shape with point 'v1'...'v4' in 3D with one solution"""
    # Following should be well-constraint, gives underconstrained (need extra rule/pattern) 
    L=10.0
    problem = GeometricProblem(dimension=3)
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([-5.0, 5.0, 0.0]))
    problem.add_point('v3', vector([5.0, 5.0, 0.0]))
    problem.add_point('v4', vector([0.0, 10.0, 0.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', L))
    problem.add_constraint(DistanceConstraint('v1', 'v3', L))
    problem.add_constraint(DistanceConstraint('v2', 'v3', L))
    problem.add_constraint(DistanceConstraint('v2', 'v4', L))
    problem.add_constraint(DistanceConstraint('v3', 'v4', L))
    # this bit of code constrains the points v1...v4 in a plane with point p above it
    problem.add_point('p', vector([0.0, 0.0, 1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'p', 1.0))
    problem.add_constraint(AngleConstraint('v2','v1','p', math.pi/2))
    problem.add_constraint(AngleConstraint('v3','v1','p', math.pi/2))
    problem.add_constraint(AngleConstraint('v4','v1','p', math.pi/2))
    return problem

# -------- 2D problems

def ddd_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',distance_2p(problem.get_point('v1'), problem.get_point('v2'))))
    problem.add_constraint(DistanceConstraint('v1','v3',distance_2p(problem.get_point('v1'), problem.get_point('v3'))))
    problem.add_constraint(DistanceConstraint('v2','v3',distance_2p(problem.get_point('v2'), problem.get_point('v3')))) 
    return problem

def dad_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',
        distance_2p(problem.get_point('v1'), problem.get_point('v2'))
    ))
    problem.add_constraint(DistanceConstraint('v2','v3',
        distance_2p(problem.get_point('v2'), problem.get_point('v3'))
    )) 
    problem.add_constraint(AngleConstraint('v1','v2','v3', 
       angle_3p(problem.get_point('v1'), problem.get_point('v2'), problem.get_point('v3'))
    ))
    return problem

def add_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',
        distance_2p(problem.get_point('v1'), problem.get_point('v2'))
    ))
    problem.add_constraint(DistanceConstraint('v2','v3',
        distance_2p(problem.get_point('v2'), problem.get_point('v3'))
    )) 
    problem.add_constraint(AngleConstraint('v3','v1','v2', 
       angle_3p(problem.get_point('v3'), problem.get_point('v1'), problem.get_point('v2'))
    ))
    return problem


def aad_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',distance_2p(problem.get_point('v1'), problem.get_point('v2'))))
    problem.add_constraint(AngleConstraint('v2', 'v3', 'v1', 
       angle_3p(problem.get_point('v2'), problem.get_point('v3'), problem.get_point('v1'))
    ))
    problem.add_constraint(AngleConstraint('v3', 'v1', 'v2',
       angle_3p(problem.get_point('v3'), problem.get_point('v1'), problem.get_point('v2'))
    ))
    return problem

def ada_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_constraint(DistanceConstraint('v1','v2',distance_2p(problem.get_point('v1'), problem.get_point('v2'))))
    problem.add_constraint(AngleConstraint('v3', 'v1', 'v2', 
       angle_3p(problem.get_point('v3'), problem.get_point('v1'), problem.get_point('v2'))
    ))
    problem.add_constraint(AngleConstraint('v1', 'v2', 'v3',
       angle_3p(problem.get_point('v1'), problem.get_point('v2'), problem.get_point('v3'))
    ))
    return problem



def propagation_problem():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([random.random() for i in [1,2]]))
    problem.add_point('v2', vector([random.random() for i in [1,2]]))
    problem.add_point('v3', vector([random.random() for i in [1,2]]))
    problem.add_point('v4', vector([random.random() for i in [1,2]]))
    problem.add_point('v5', vector([random.random() for i in [1,2]]))
    
    problem.add_constraint(DistanceConstraint('v1','v2',
        distance_2p(problem.get_point('v1'), problem.get_point('v2'))
    ))
    
    problem.add_constraint(DistanceConstraint('v1','v3',
        distance_2p(problem.get_point('v1'), problem.get_point('v3'))
    ))
    
    problem.add_constraint(DistanceConstraint('v2','v3',
        distance_2p(problem.get_point('v2'), problem.get_point('v3'))
    ))
   
    problem.add_constraint(DistanceConstraint('v2','v4',
        distance_2p(problem.get_point('v2'), problem.get_point('v4'))
    ))
 
    problem.add_constraint(DistanceConstraint('v1','v5',
        distance_2p(problem.get_point('v1'), problem.get_point('v5'))
    ))
    
    problem.add_constraint(AngleConstraint('v3', 'v1', 'v4', 
       angle_3p(problem.get_point('v3'), problem.get_point('v1'), problem.get_point('v4'))
    ))
    
    problem.add_constraint(AngleConstraint('v3', 'v2', 'v5', 
       angle_3p(problem.get_point('v3'), problem.get_point('v2'), problem.get_point('v5'))
    ))

    return problem


def balloon_problem():
    """test angle propagation via balloon"""
    problem = GeometricProblem(dimension=2)
    problem.add_point('A', vector([0.0, 0.0]))
    problem.add_point('B', vector([1.0, -1.0]))
    problem.add_point('C', vector([1.0, +1.0]))
    problem.add_point('D', vector([2.0, 0.0]))
    problem.add_constraint(AngleConstraint('B','A','C', 
       angle_3p(problem.get_point('B'), problem.get_point('A'), problem.get_point('C'))
    ))
    problem.add_constraint(AngleConstraint('A','B','C', 
       angle_3p(problem.get_point('A'), problem.get_point('B'), problem.get_point('C'))
    ))
    problem.add_constraint(AngleConstraint('B','C','D', 
       angle_3p(problem.get_point('B'), problem.get_point('C'), problem.get_point('D'))
    ))
    problem.add_constraint(AngleConstraint('C','D','B', 
       angle_3p(problem.get_point('C'), problem.get_point('D'), problem.get_point('B'))
    ))
    problem.add_constraint(DistanceConstraint('A', 'D', 6.0))
    return problem

def double_triangle():
    problem = GeometricProblem(dimension=2)
    problem.add_point('v1', vector([0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0]))
    problem.add_point('v4', vector([1.0, 1.0]))
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    return problem

def triple_double_triangle():
    problem = GeometricProblem(dimension=2)
    problem.add_point('QX', vector([0.0, 0.0]))
    problem.add_point('QA2', vector([1.0, 0.0]))
    problem.add_point('QA3', vector([0.0, 1.0]))
    problem.add_point('QY', vector([1.0, 1.0]))
    problem.add_constraint(DistanceConstraint('QX', 'QA2', 10.0))
    problem.add_constraint(DistanceConstraint('QX', 'QA3', 10.0))
    problem.add_constraint(DistanceConstraint('QA2', 'QA3', 10.0))
    problem.add_constraint(DistanceConstraint('QA2', 'QY', 10.0))
    problem.add_constraint(DistanceConstraint('QA3', 'QY', 10.0))
    
    #problem.add_point('QX', vector([0.0, 0.0]))
    problem.add_point('QB2', vector([1.0, 0.0]))
    problem.add_point('QZ', vector([0.0, 1.0]))
    problem.add_point('QB4', vector([1.0, 1.0]))
    problem.add_constraint(DistanceConstraint('QX', 'QB2', 10.0))
    problem.add_constraint(DistanceConstraint('QX', 'QZ', 10.0))
    problem.add_constraint(DistanceConstraint('QB2', 'QZ', 10.0))
    problem.add_constraint(DistanceConstraint('QB2', 'QB4', 10.0))
    problem.add_constraint(DistanceConstraint('QZ', 'QB4', 10.0))
    
    #problem.add_point('QY', vector([0.0, 0.0]))
    problem.add_point('QC2', vector([1.0, 0.0]))
    #problem.add_point('QZ', vector([0.0, 1.0]))
    problem.add_point('QC4', vector([1.0, 1.0]))
    problem.add_constraint(DistanceConstraint('QY', 'QC2', 10.0))
    problem.add_constraint(DistanceConstraint('QY', 'QZ', 10.0))
    problem.add_constraint(DistanceConstraint('QC2', 'QZ', 10.0))
    problem.add_constraint(DistanceConstraint('QC2', 'QC4', 10.0))
    problem.add_constraint(DistanceConstraint('QZ', 'QC4', 10.0))
    
    return problem




def hog1():
    # double triangle with inter-angle (needs angle propagation)
    problem = GeometricProblem(dimension=2)
    problem.add_point('A', vector([0.0, 0.0]))
    problem.add_point('B', vector([1.0, 0.0]))
    problem.add_point('C', vector([1.0, 1.0]))
    problem.add_point('D', vector([0.0, 1.0]))
    problem.add_constraint(DistanceConstraint('A', 'B', 10.0))
    problem.add_constraint(DistanceConstraint('B', 'C', 10.0))
    problem.add_constraint(DistanceConstraint('C', 'D', 10.0))
    problem.add_constraint(AngleConstraint('B','A','C', math.pi / 8))
    problem.add_constraint(AngleConstraint('B','A','D', math.pi / 4))
    return problem

def hog2():
    # several triangles with inter-angles (needs angle propagation)
    problem = GeometricProblem(dimension=2)
    problem.add_point('M', vector([0.0, 0.0]))
    problem.add_point('A', vector([0.0, 1.0]))
    problem.add_point('B', vector([1.0, 1.0]))
    problem.add_point('C', vector([2.0, 1.0]))
    problem.add_point('D', vector([3.0, 1.0]))
    problem.add_point('E', vector([4.0, 1.0]))
    problem.add_constraint(DistanceConstraint('A', 'M', 10.0))
    problem.add_constraint(DistanceConstraint('A', 'E', 10.0))
    problem.add_constraint(DistanceConstraint('B', 'E', 7.0))
    problem.add_constraint(DistanceConstraint('C', 'E', 6.0))
    problem.add_constraint(DistanceConstraint('D', 'E', 5.0))
    problem.add_constraint(AngleConstraint('A','M','B', math.pi / 20))
    problem.add_constraint(AngleConstraint('B','M','C', math.pi / 20))
    problem.add_constraint(AngleConstraint('D','M','C', math.pi / 20))
    problem.add_constraint(AngleConstraint('D','M','E', math.pi / 20))
    return problem

def balloons():
    # for testing angle propagation via balloon
    problem = GeometricProblem(dimension=2)
    problem.add_point('A', vector([0.0, 0.0]))
    problem.add_point('B', vector([0.0, 1.0]))
    problem.add_point('C', vector([1.0, 1.0]))
    problem.add_point('D', vector([2.0, 1.0]))
    problem.add_constraint(AngleConstraint('B','A','C', math.pi / 8))
    problem.add_constraint(AngleConstraint('A','B','C', math.pi / 8))
    problem.add_constraint(AngleConstraint('B','C','D', math.pi / 8))
    problem.add_constraint(AngleConstraint('C','D','B', math.pi / 8))
    problem.add_constraint(DistanceConstraint('A', 'D', 6.0))
    return problem

def twoscisors():
    problem = GeometricProblem(dimension=2)
    problem.add_point('A', vector([0.0, 0.0]))
    problem.add_point('B', vector([0.0, 1.0]))
    problem.add_point('C', vector([1.0, 1.0]))
    problem.add_point('D', vector([2.0, 1.0]))
    problem.add_constraint(AngleConstraint('B','A','C', math.pi / 8))
    problem.add_constraint(AngleConstraint('B','D','C', math.pi / 8))
    problem.add_constraint(DistanceConstraint('A', 'B', 6.0))
    problem.add_constraint(DistanceConstraint('A', 'C', 6.0))
    problem.add_constraint(DistanceConstraint('D', 'B', 6.0))
    problem.add_constraint(DistanceConstraint('D', 'C', 6.0))
    return problem

def selection_problem():
    """The double tetrahedron problem with selection constraints"""
    
    problem = GeometricProblem(dimension=3)
    
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))

    #problem.add_constraint(SelectionConstraint(is_right_handed, ['v1','v2','v4','v5']))
    problem.add_constraint(RightHandedConstraint('v1','v2','v4','v5'))
    
    return problem



# ------ 2D tests -------

def test_fix(n):
    """Test fix constraints"""
    #diag_select("drplan._search_triangle")
    
    print "generate a random 2D problem"
    problem = random_problem_2D(n)
    
    print "create dr planner"
    drplanner = GeometericSolver(problem)
    print "number of top clusters:", len(drplanner.dr.top_level())
    #print "top clusters:", map(str, drplanner.dr.top_level())
    
    cons = problem.cg.constraints()
    dists = filter(lambda d: isinstance(d, DistanceConstraint), cons)
    con = random.choice(dists)
    print "remove distance", con
    problem.rem_constraint(con)
    print "number of top clusters:", len(drplanner.dr.top_level())
    #print "top clusters:", map(str, drplanner.dr.top_level())

    print "replace with two fixes"
    v1 = con.variables()[0]
    v2 = con.variables()[1]
    f1 = FixConstraint(v1, problem.get_point(v1))
    f2 = FixConstraint(v2, problem.get_point(v2))
    problem.add_constraint(f1)
    problem.add_constraint(f2)
    print "number of top clusters:", len(drplanner.dr.top_level())
    #print "top clusters:", map(str, drplanner.dr.top_level())

def test_fix2(n):
    """Test fix constraints"""
    # diag_select("drplan.*")
    print "generate a random 2D problem"
    problem = random_problem_2D(n)
   
    cons = problem.cg.constraints()
    dists = filter(lambda d: isinstance(d, DistanceConstraint), cons)
    con = random.choice(dists)
    print "remove distance", con
    problem.rem_constraint(con)

    print "replace with two fixes"
    v1 = con.variables()[0]
    v2 = con.variables()[1]
    f1 = FixConstraint(v1, problem.get_point(v1))
    f2 = FixConstraint(v2, problem.get_point(v2))
    problem.add_constraint(f1)
    problem.add_constraint(f2)

    print "create dr planner"
    drplanner = GeometricSolver(problem)
    print "number of top clusters:", len(drplanner.dr.top_level())
    print "top clusters:", map(str, drplanner.dr.top_level())
    
    
def find_error(count, size, over_ratio):
    """Test solver by generating random problems"""
    random.seed(1)
    diag_select("xyzzy")
    for i in range(0,count):
        if random.random() > over_ratio: 
            if not test_random_wellconstrained(size):
                print "failed wellconstrained problem #"+str(i)
                return
        else:
            if not test_random_overconstrained(size):
                print "failed overconstrained problem #"+str(i)
                return
    print "all tests passed"
       

def test_random_overconstrained(size):
    # start with random well-constrained problem
    problem = random_problem_2D(size, 0.0)
    # add one random contraint
    for i in range(100):
        try: 
            add_random_constraint(problem, 0.5)
            break
        except:
            pass
    if i == 99:
        raise StandardError, "could not add extra constraint"
    # test
    try:
        drplanner = GeometricSolver(problem)
        ntop = len(drplanner.dr.top_level())
        if ntop > 1:
            message = "underconstrained"
            check = False
        elif ntop == 0:
            message = "no top level"
            check = False
        else:  # ntop == 1
            top = drplanner.dr.top_level()[0]
            if not top.overconstrained:
                message = "well-constrained"
                check = False
            else:
                check = True
    except Exception, e:
        message =  "error:",e
        check = False
    #end try 
    if check == False:
        print "--- problem ---"
        print problem
        print "--- diasgnostic messages ---"
        diag_select("drplan")
        drplanner = GeometricSolver(problem)
        print "--- plan ---"
        top = drplanner.dr.top_level()
        print drplanner.dr
        print "--- top level ---"
        print len(top),"clusters:"
        for cluster in drplanner.dr.top_level():
            print cluster 
        print "--- conclusion ---"
        print message
        return False
    else:
        return True


def test_random_wellconstrained(size):
    problem = random_problem_2D(size, 0.0)
    try:
        drplanner = GeometricSolver(problem)
        ntop = len(drplanner.dr.top_level())
        if ntop > 1:
            message = "underconstrained"
            check = False
        elif ntop == 0:
            message = "no top level"
            check = False
        else:  # ntop == 1
            top = drplanner.dr.top_level()[0]
            if top.overconstrained:
                message = "overconstrained"
                check = False
            else:
                check = True
    except Exception, e:
        print "error in problem:",e
        check = False
    #end try 
    if check == False:
        print "--- problem ---"
        print problem
        print "--- diasgnostic messages ---"
        diag_select("drplan")
        drplanner = GeometricSolver(problem)
        top = drplanner.dr.top_level()
        print "--- plan ---"
        print drplanner.dr
        print "--- top level ---"
        print len(top),"clusters:"
        for cluster in drplanner.dr.top_level():
            print cluster 
        print "--- conclusion ---"
        print message
        return False
    else:
        return True

#fed

def buggy1():
    problem = GeometricProblem(dimension=2)
    p0 = "P0"
    p1 = "P1"
    p2 = "P2"
    p3 = "P3"
    problem.add_point(p2,vector([4.2516273494524803, -9.510959969336783]))
    problem.add_point(p3,vector([0.96994030830283862, -3.6416260233938491]))
    problem.add_point(p0,vector([6.6635607149389386, -8.5894325593219882]))
    problem.add_point(p1,vector([-0.06750282559988996, 6.6760454282229134]))
    problem.add_constraint(AngleConstraint(p1,p3,p0,2.38643631762))
    problem.add_constraint(DistanceConstraint(p2,p0,2.58198282856))
    problem.add_constraint(AngleConstraint(p1,p0,p2,-1.52046205861))
    problem.add_constraint(DistanceConstraint(p3,p1,10.3696977989))
    problem.add_constraint(AngleConstraint(p3,p0,p1,0.440080782652))
    return problem

def test_mergehogs():
    diag_select(".")
    problem = GeometricProblem(dimension=2)
    problem.add_point('x',vector([0.0, 0.0]))
    problem.add_point('a',vector([1.0, 0.0]))
    problem.add_point('b',vector([0.0, 1.0]))
    problem.add_point('c',vector([-1.0, 0.0]))
    problem.add_point('d',vector([0.0, -1.0]))
    problem.add_constraint(AngleConstraint('a','x','b', 30.0/180*math.pi))
    problem.add_constraint(AngleConstraint('b','x','c', 30.0/180*math.pi))
    problem.add_constraint(AngleConstraint('c','x','d', 30.0/180*math.pi))
    solver = GeometricSolver(problem) 
    print solver.dr
    for hog in solver.dr.hedgehogs():
        conf = list(solver.mg.get(hog))[0]
        print hog
        print conf
        print problem.verify(conf.map)
 
def test_non_triangular(n):
    problem = random_problem_2D(n)
    print "before:"
    print problem
    randomize_angles(problem)
    print "after:"
    print problem
    test(problem)


# ----------- 3d tests ----------

def test_ada_3d():
    problem = ada_3d_problem()
    diag_select("nothing")
    print "problem:"
    print problem
    solver = GeometricSolver(problem)
    print "drplan:"
    print solver.dr
    print "number of top-level rigids:",len(solver.dr.top_level())
    result = solver.get_result()
    print "result:"
    print result
    print "result is",result.flag, "with", len(result.solutions),"solutions"
    check = True
    if len(result.solutions) == 0:
        check = False
    diag_select(".*")
    for sol in result.solutions:
        print "solution:",sol
        check = check and problem.verify(sol)
    diag_select("nothing")
    if check: 
        print "all solutions valid"
    else:
        print "INVALID"


# ------- generic test -------

def test(problem, use_prototype=True):
    """Test solver on a given problem"""
    #diag_select(".*")
    print "problem:"
    print problem
    print "use_prototype=",use_prototype
    print "Solving..."
    solver = GeometricSolver(problem, use_prototype)
    print "...done"
    print "drplan:"
    print solver.dr
    print "top-level rigids:",list(solver.dr.top_level())
    result = solver.get_result()
    print "result:"
    print result
    print "result is",result.flag, "with", len(result.solutions),"solutions"
    check = True
    if len(result.solutions) == 0:
        check = False
    diag_select("GeometricProblem.verify")
    for sol in result.solutions:
        print "solution:",sol
        check = check and problem.verify(sol)
    if check: 
        print "all solutions valid"
    else:
        print "INVALID"
  
# ----- what to test today -------

#if __name__ == "__main__": 
#    find_error(1000, 4)

#if __name__ == "__main__": 
#    test(random_problem_2D(4, 0.0))  

#if __name__ == "__main__": 
#    diag_select("(.*Method)|(GeometricProblem.verify)")
#    test(random_AAD())  

#if __name__ == "__main__": 
#    #diag_select("(.*Method)|(GeometricProblem.verify)")
#    diag_select("drplan")
#    test(propagation_problem())   

#if __name__ == "__main__": 
#     diag_select("(GeometricProblem.verify)")
#     test(balloon_problem())  

# create statistics for solving time
def stats_solving():
    print "size \t # \t time \t result"
    for size in range(4,31):
        for i in range(1,10):
            problem = random_triangular_problem_3D(size,10.0,0.0,0.0)
            t1 = time()
            solver = GeometricSolver(problem)
            result = solver.get_status()
            t2 = time()
            t = t2-t1
            print size,"\t",i,"\t",t,"\t",result

# create statistics for incremental solving time
def stats_incremental():
    #diag_select("clsolver.remove")
    print "size \t # \t time \t result"
    for size in range(4,31):
        for i in range(1,10):
            problem = random_triangular_problem_3D(size,10.0,0.0,0.0)
            solver = GeometricSolver(problem)
            t1 = time()
            constraint = random.choice(problem.cg.constraints())
            problem.rem_constraint(constraint)
            problem.add_constraint(constraint)
            result = solver.get_status()
            t2 = time()
            t = t2-t1
            print size,"\t",i,"\t",t,"\t",result

# create statistics for parametric change
def stats_parametric_incremental():
    #diag_select("clsolver.remove")
    print "size \t # \t time \t result"
    for size in range(4,31):
        for i in range(1,10):
            problem = random_triangular_problem_3D(size,10.0,0.0,0.0)
            solver = GeometricSolver(problem)
            constraint = random.choice(problem.cg.constraints())
            #problem.rem_constraint(constraint)
            #problem.add_constraint(constraint)
            #problem.rem_constraint(constraint)
            #problem.add_constraint(constraint)
            t1 = time()
            #problem.rem_constraint(constraint)
            #problem.add_constraint(constraint)
            #constraint.set_parameter(constraint.get_parameter())
            result = solver.get_status()
            t2 = time()
            t = t2-t1
            print size,"\t",i,"\t",t,"\t",result

# create statistics for parametric change
def stats_parametric():
    #diag_select("clsolver.remove")
    print "size \t # \t time \t result"
    for size in range(4,31):
        for i in range(1,10):
            problem = random_triangular_problem_3D(size,10.0,0.0,0.0)
            solver = GeometricSolver(problem)
            constraint = random.choice(problem.cg.constraints())
            t1 = time()
            constraint.set_parameter(constraint.get_parameter())
            result = solver.get_status()
            t2 = time()
            t = t2-t1
            print size,"\t",i,"\t",t,"\t",result

def runstats():
    stats_solving() 
    stats_incremental() 
    stats_parametric_incremental() 
    stats_parametric() 

def selection_test():
    problem = GeometricProblem(dimension=3)
    
    problem.add_point('v1', vector([0.0, 0.0, 0.0]))
    problem.add_point('v2', vector([1.0, 0.0, 0.0]))
    problem.add_point('v3', vector([0.0, 1.0, 0.0]))
    problem.add_point('v4', vector([0.5, 0.5, 1.0]))
    problem.add_point('v5', vector([0.5, 0.5,-1.0]))
    
    problem.add_constraint(DistanceConstraint('v1', 'v2', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v3', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v4', 10.0))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v2', 'v5', 10.0))
    problem.add_constraint(DistanceConstraint('v3', 'v5', 10.0))

    s1 = SelectionConstraint(is_right_handed, ['v1','v2','v4','v5'])
    
    # add selection con
    problem.add_constraint(s1)
    
    # solve
    solver = GeometricSolver(problem, False)
    print len(solver.get_solutions()), "solutions"
    
    # remove and add constraint
    print "removing selection-constraint"
    problem.rem_constraint(s1)

    # solve again
    print len(solver.get_solutions()), "solutions"

    # remove and add constraint
    print "re-adding selection constraint"
    problem.add_constraint(s1)

    # solve again
    print len(solver.get_solutions()), "solutions"

    # remove distance
    print "removing and re-adding distance v1-v5"
    problem.rem_constraint(problem.get_distance("v1","v5"))
    problem.add_constraint(DistanceConstraint('v1', 'v5', 10.0))

    # solve again
    print len(solver.get_solutions()), "solutions"


def test3d():
    #diag_select("clsolver")
    #test(double_tetrahedron_problem())
    #test(ada_tetrahedron_problem())
    #test(double_banana_problem())
    #test(double_banana_plus_one_problem())
    #test(random_triangular_problem_3D(10,10.0,0.0,0.5))
    #test(random_distance_problem_3D(10,1.0,0.0))
    #test(fix1_problem_3d())
    test(fix2_problem_3d())
    #test(fix3_problem_3d())
    #diag_select("SelectionMethod.*")
    #test(selection_problem(),False)
    #selection_test()
    #test(overconstrained_tetra())
    #test(diamond_3d(),False)

def test2d():
    #test(ddd_problem())
    #test(double_triangle())
    #test(triple_double_triangle())
    #test(dad_problem())
    #test(add_problem())
    test(aad_problem())

if __name__ == "__main__": 
    test2d()
