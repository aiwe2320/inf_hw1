import SIR_utils as sir
from scipy.optimize import fsolve
import math
import matplotlib
import matplotlib.pyplot as plt

# First solve for r_infinity
# Functions for fsolve
def func(x, R0):
    return [x[1] - x[0],
            1 - math.exp(-R0*x[0]) - x[1]]

# R0 = beta/gamma
beta = 1
gamma = 0.5
R0 = beta / gamma

# Calculate r infinity using same method
root = fsolve(func, [1, 1], args=(R0))
r_inf = root[0]
r_inf_list = [r_inf] * 11
t_r = list(range(0, 55, 5))

# Perform SIR simulation
t, S, I, R = sir.simple_SIR(S0=999, I0=1, R0=R0, beta=beta, gamma=gamma, dt=1, tmax=50)

# Want to plot proportions
s = [val/1000 for val in S]
i = [val/1000 for val in I]
r = [val/1000 for val in R]

# Plot
fig, ax = plt.subplots()
ax.plot(t, s, label='s Aidan')
ax.plot(t, i, label='i Aidan')
ax.plot(t, r, label='r Aidan')
ax.plot(t_r, r_inf_list,'g--', label='r_infinity')
ax.set_xlabel('Time')
ax.set_ylabel('Proportion of Population')
ax.set_title('SIR with r_infinity')
ax.legend()

plt.savefig('SIR_with_r_inf.png', bbox_inches='tight')