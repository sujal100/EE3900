import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

def is_parallogram(a,b,c,d):
    # change list to numpy array
    a = np.array(a).reshape(len(a),1)
    b = np.array(b).reshape(len(a),1)
    c = np.array(c).reshape(len(a),1)
    d = np.array(d).reshape(len(a),1)
    
    # checking all points are descrete points
    if((a == b).all() or
       (b == c).all() or
       (c == d).all() or
       (d == a).all() or
       (c == a).all() or
       (b == d).all()):
        return False
    
    # finding midpoint of all joining lines
    p = (a+b)/2
    q = (b+c)/2
    r = (c+d)/2
    s = (d+a)/2
    t = (a+c)/2
    u = (b+d)/2
    
    # concatenate all calculated mid-points
    vec = np.concatenate((p,q,r,s,t,u), axis = -1)
    
    # checking if two mid-points are coincidence
    for i in range(6):
        for j in range(6):
            if (np.array_equal(vec[:,i],vec[:,j])and (i!=j)):
                return True
    return False


A = np.array([1,3,2]).reshape((3,1))
B = np.array([4,5,0]).reshape((3,1))
C = np.array([2,0,4]).reshape((3,1))
D = np.array([5,2,2]).reshape((3,1))
print("Example 0, Is this a parallelogram : ",is_parallogram(A,B,C,D))

P,Q,R,S = [-2, -2], [2, -2], [2, 0], [-2, 0]
print("Example 1, [-2, -2], [2, -2], [2, 0], [-2, 0] ",is_parallogram(P,Q,R,S))
P,Q,R,S = [0, 0], [5, 0], [8, 4], [3, 4]
print("Example 2, [0, 0], [5, 0], [8, 4], [3, 4] ",is_parallogram(P,Q,R,S))
P,Q,R,S = [4, 2], [6, 3], [6, 5], [4, 4]
print("Example 3, [4, 2], [6, 3], [6, 5], [4, 4] ",is_parallogram(P,Q,R,S))
P,Q,R,S = [5, 2], [9, 2], [9, 4], [7, 4]	
print("Example 4, [5, 2], [9, 2], [9, 4], [7, 4] ",is_parallogram(P,Q,R,S))
P,Q,R,S = [2, 1], [8, 1], [9, 8], [6, 6]
print("Example 5, [2, 1], [8, 1], [9, 8], [6, 6] ",is_parallogram(P,Q,R,S))

''' output
Example 0, Is this a parallelogram :  True
Example 1, [-2, -2], [2, -2], [2, 0], [-2, 0]  True
Example 2, [0, 0], [5, 0], [8, 4], [3, 4]  True
Example 3, [4, 2], [6, 3], [6, 5], [4, 4]  True
Example 4, [5, 2], [9, 2], [9, 4], [7, 4]  False
Example 5, [2, 1], [8, 1], [9, 8], [6, 6]  False
'''

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')
 
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CD[0,:],x_CD[1,:],x_CD[2,:],label="CD")
plt.plot(x_DA[0,:],x_DA[1,:],x_DA[2,:],label="DA")
plt.plot(x_AC[0,:],x_AC[1,:],x_AC[2,:],label="AC")
plt.plot(x_BD[0,:],x_BD[1,:],x_BD[2,:],label="BD")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(D[0],D[1],D[2],'o')
ax.text(1,3,2,"A", color='red')
ax.text(4,5,0,"B", color='red')
ax.text(2,0,4,"C", color='red')
ax.text(5,2,2,"D", color='red')

#save plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.savefig('../figures/Plot.png')