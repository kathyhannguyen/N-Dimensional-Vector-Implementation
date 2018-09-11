# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 01:38:18 2018

@author: Kathyhan
"""

class MathVector: 
    'N-dimensional mathematical (Euclidian) vector'
    
    def __init__(self, *args): 
        if len(args) == 1: #single numerical argument specifying dimensions
            if isinstance(args[0], int): 
                self.dimen = args[0] 
                self.values = [0] * self.dimen
            else: #single list or tuple argument
                self.dimen = len(args[0])
                y = []
                for i in range(self.dimen): 
                    y.append(args[0][i])
                self.values = y
        elif len(args) > 1: #multiple arguments 
            self.dimen = len(args)
            y = []
            for i in args: 
                y.append(i)
            self.values = y
                
    def get_el(self, i): 
        return self.values[i-1]
    
    def neg(self): 
        return MathVector([x*-1 for x in self.values])
    
    def mag(self): 
        return (reduce(lambda x, y: x + y**2, self.values, 0))**0.5 
        
    def dot(self, VectorB): 
        return sum(x*y for x, y in zip(self.values, VectorB.values))
        
    def plus(self, VectorB): 
        return MathVector(([self.values[i] + VectorB.values[i] 
                            for i in range(len(self.values))]))
    
    def sp(self, k): 
        return MathVector([i*k for i in self.values])
    
    def print_me(self) :
        print self.values
        
    #MAGIC METHODS
    def __getitem__(self, i): 
        return self.get_el(i)
    
    def __neg__(self): 
        return self.neg()
   
    def __abs__(self): 
        return self.mag()
    
    def __mul__(self, k): 
        if isinstance(k, int):
            return self.sp(k)
        else: 
            return self.dot(k)
    
    def __rmul__(self, k): 
        return self.sp(k)
    
    def __add__(self, VectorB): 
        return self.plus(VectorB)
    
    def __str__(self): 
        return str(self.values)   
            
#TEST CODE: 
u = MathVector(5)
print "u =",
u.print_me()
 

v = MathVector([2,3,6])
print "v =",
v.print_me()
 
w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v 