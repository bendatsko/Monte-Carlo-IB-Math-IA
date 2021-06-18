import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.path import Path
import matplotlib.patches as patches
import time

then = time.time()

#==============================================
#                   SHAPES
#==============================================

# # ####################################
# # #    Circle (uncomment to use)
# # ####################################
# circle = Circle([-1,-1], radius=1)

# path = circle.get_path()
# patch = patches.PathPatch(path, facecolor='none', edgecolor='#000000')


# # ####################################
# # #   Polar Rose (uncomment to use)
# # ####################################

theta = np.linspace(0, 2*np.pi, 1000) 

r = 1.8* np.cos(4 * theta) 

xcart = r*np.cos(theta)
ycart = r*np.sin(theta)

newarrx = np.array_split(xcart, 1000)
newarry = np.array_split(ycart, 1000)


verts = [None] * 1000
codes = [None] * 1000


i = 0
while i < 1000:
    verts[i] = ( float(newarrx[i]), float(newarry[i]))
    codes[i] = Path.CURVE4
    i = i+1
    

codes[0] = Path.MOVETO


path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.add_patch(patch)



##################
#  Scatter Plot
##################

# adheres to the law of large numbers! the more points generated, the more accurate the calculation will be!
total_random_points = 1000

x_plot_array = np.empty(shape=(1,total_random_points))
y_plot_array = np.empty(shape=(1,total_random_points))

x = np.random.uniform(-2, 2, size = total_random_points)
y = np.random.uniform(-2, 2, size = total_random_points)

random_points_plot = plt.scatter(x, y, color='red', s=.25)
random_points_plot.set_zorder(0) 



#==============================================
#           MONTE CARLO CALCULATIONS
#==============================================

inside_shape = 0;

for i in range(0, total_random_points):
    x_2 = x[i]
    y_2 = y[i]

    result = str(path.contains_points([[x_2,y_2]]))

    if "[ True]" == result:
        inside_shape = inside_shape + 1 
        plt.scatter(x[i] , y[i], color='lime', s=.25) 
    
in_to_out_ratio = inside_shape / total_random_points



#==============================================
#                    DRAW
#==============================================
ax = plt.gca()
ax.set_aspect('equal', 'box')


ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

ax.add_artist(random_points_plot)
ax.add_patch(patch)


now = time.time()

print ('--------------')
print ('Statistics')
print ('Total number of points on graph:',total_random_points)
print ('Area of graph:', 16)
print ('IN OUT RATIO:', in_to_out_ratio)
print ('Number of points inside shape:', inside_shape)
print ('Area of shape:', in_to_out_ratio * (16)) 
print ('\nCalculation performed in: ', now-then, " seconds")


plt.show()



