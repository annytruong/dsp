# Matrix Algebra

import numpy as np

a = np.matrix('1 2 3; 2 7 4')
b = np.matrix('1 -1; 0 1')
c = np.matrix('5 -1; 9 1; 6 0')
d = np.matrix('3 -2 -1; 1 2 3')
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

# Part I: Matrix Dimensions
print '1.1) ', a.shape
print '1.2) ', b.shape
print '1.3) ', c.shape
print '1.4) ', d.shape
print '1.5) ', u.shape
print '1.6) ', v.shape
print '1.7) ', w.shape

# Part II: Vector Operations
print '2.1) ', u + v
print '2.2) ', u - v
print '2.3) ', 6*u
print '2.4) ', np.dot(u,v)
print '2.5) ', np.linalg.norm(u)

# Part III: Matrix Operations

print '3.1) ',
try: a + c
except ValueError: print 'Not Defined'

print '3.2) ', 
try: a - c.T
except ValueError: print 'Not Defined'

print '3.3) ', 
try: c.T + 3*d
except ValueError: print 'Not Defined'

print '3.4) ', 
try: b*a
except ValueError: print 'Not Defined'

print '3.5) ', 
try: b*a.T
except ValueError: print 'Not Defined'
