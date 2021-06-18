import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.path import Path
import matplotlib.patches as patches
import time


# define timer
then = time.time()

#==============================================
#                   SHAPES
#==============================================

# # ####################################
# # #    Circle (uncomment to use)
# # ####################################
# # Create the initial circle
# circle = Circle([-1,-1], radius=1)

# # Get the path
# path = circle.get_path()
# patch = patches.PathPatch(path, facecolor='none', edgecolor='#000000')


# # ####################################
# # #   Polar Rose (uncomment to use)
# # ####################################

#Plot in polar coordinates
theta = np.linspace(0, 2*np.pi, 1000) #generate 1000 points in a circle (hence 2pi)

r = 1.8* np.cos(4 * theta) #funtion

#convert to cartesian
xcart = r*np.cos(theta)
ycart = r*np.sin(theta)

newarrx = np.array_split(xcart, 1000)
newarry = np.array_split(ycart, 1000)


verts = [None] * 1000
codes = [None] * 1000


i = 0
while i < 1000:
    # verts[i] = (1.0, 0.0)
    verts[i] = ( float(newarrx[i]), float(newarry[i]))
    codes[i] = Path.CURVE4
    i = i+1
    print(i)
    

codes[0] = Path.MOVETO


path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.add_patch(patch)



##################
#  Scatter Plot
##################

# Total number of random points
total_random_points = 5

# Create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty(shape=(1,total_random_points))
y_plot_array = np.empty(shape=(1,total_random_points))

# Create random values (x,y) between -1 and 1
x = np.random.uniform(-2, 2, size = total_random_points)
y = np.random.uniform(-2, 2, size = total_random_points)

# Plot output of random points and circle
random_points_plot = plt.scatter(x, y, color='red', s=.25)
random_points_plot.set_zorder(0) #set scatter plot position to back



#==============================================
#           MONTE CARLO CALCULATIONS
#==============================================

inside_shape = 0;

# Iterate over points to locate them and count points inside unit circle
for i in range(0, total_random_points):
    #locates the points    
    x_2 = x[i]
    y_2 = y[i]

    # Tests for whether the specified point is contained by the shape
    result = str(path.contains_points([[x_2,y_2]]))

    # Count if inside shape
    if "[ True]" == result:
        inside_shape = inside_shape + 1 # Add 1 to the counter
        plt.scatter(x[i] , y[i], color='lime', s=.25) # Change the color of the point to green
    
# Stats: Number of points inside shape compared to total
in_to_out_ratio = inside_shape / total_random_points



#==============================================
#                    DRAW
#==============================================
# Create axis with equal aspect ratio in both axis
ax = plt.gca()
ax.set_aspect('equal', 'box')


# Set axis limits
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

# Add the points and the shape to the plot
ax.add_artist(random_points_plot)
ax.add_patch(patch)

# Render plot in screen
plt.show()

#end timer
now = time.time()

# Log stats in console
print ('\n--------------')
print ('\n Statistics')
print ('\n Total number of points on graph:',total_random_points)
print ('\n Area of graph:', 16)
print ('\n IN OUT RATIO:', in_to_out_ratio)
print ('\n Number of points inside shape:', inside_shape)
print ('\n Area of shape:', in_to_out_ratio * (16)) # Multiplying probability by total area to find area of sector
print ('\n\n Calculation performed in: ', now-then, " seconds")

