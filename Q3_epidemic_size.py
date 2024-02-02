import matplotlib
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

# Functions for fsolve
def func(x, R0):
    return [x[1] - x[0],
            1 - math.exp(-R0*x[0]) - x[1]]

# Values of R0
R0 = [0.9, 1.0, 1.1, 1.2]

# Solve functions over range of values
r = [x/100 for x in range(0, 50, 5)]
fr = r
gr_list = []
for val in R0:
    temp = []
    for i in r:
        gr = 1 - math.exp(-val * i)
        temp.append(gr)
    gr_list.append(temp)

# List of output file names and plot titles
titles = ['r vs r_infinity - R0 = 0.9',
          'r vs r_infinity - R0 = 1.0',
          'r vs r_infinity - R0 = 1.1',
          'r vs r_infinity - R0 = 1.2']
file_names = ['Q3_plot_r9',
              'Q3_plot_r10',
              'Q3_plot_r11',
              'Q3_plot_r12']

# Perform fsolve
#root09 = fsolve(func09, [0.25, 0.25])
#root10 = fsolve(func09, [0.25, 0.25])
#root11 = fsolve(func09, [0.25, 0.25])
#root12 = fsolve(func09, [0.25, 0.25])

# Save plots
fig, ax = plt.subplots(4, figsize=(10,20))
for i, name in enumerate(file_names):
    # Perform fsolve
    root = fsolve(func, [0.25, 0.25], args=(R0[i]))
    #print(root)
    # Plot
    ax[i].scatter(root[0], root[1], color='b', facecolors='none')
    ax[i].plot(r, fr, color='k', label='f')
    ax[i].plot(r, gr_list[i], color='r', label='g')
    ax[i].set_xlabel('r_infinity')
    ax[i].set_ylabel('r')
    ax[i].set_title(titles[i])
    ax[i].legend()
    
plt.savefig('plots.png')
