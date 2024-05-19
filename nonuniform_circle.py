import numpy as np

np.random.seed(45)
frac = 1.6
n_perm = 26
theta1 = np.linspace(0.0,(frac*np.pi),num=300)
theta2 = np.linspace((frac*np.pi),2*np.pi,num=5)
theta = np.hstack([theta1,theta2])
nonuniform_circle = np.column_stack([np.cos(theta1),np.sin(theta1)])
nonuniform_circle = nonuniform_circle + 0.1*np.random.randn(*nonuniform_circle.shape)
nonuniform_circle = np.vstack([np.column_stack([np.cos(theta2),np.sin(theta2)]),nonuniform_circle])

np.savetxt('bad_circle.txt',nonuniform_circle)
np.savetxt('angles.txt',theta)