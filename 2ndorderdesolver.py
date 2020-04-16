import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np

def sys_des(y, t, params):
    """param y: the current values of the function and its first derivative
       param t: current time
       param params: all the data which varies dependent on the problem setup
    """
    x, v = y # Unpack the input, x is function and v is its first derivative
    w, c, r = params #put your appropriate params in the problem setup section
    dx = v
    dv = - (w ** 2) / c * np.sin(x) - 1/ c / r * v + (w ** 2) / c  # Equation 2.
    return([dx, dv])

def phase_2_volt(function):
    """param function: numpy array of values
       param time: numpy array of time values
    """
    return 3.29 * 10 ** (-5) * np.gradient(function)

# Problem setup
w = 5.477 * 10 ** 10
c = 1
r = 10 ** (-9)
paramstuff = [w, c]

# Initial values 


# Setup the time domain for the solution. 
t_end = 0.1 * 10**(-8)
N     = 100000 
t = np.linspace(0.,t_end,N)

fig1 = plt.figure(figsize=(10,7))
plt.title('Different Resistor Values(1 pF capacitor)')
plt.xlabel('Time (sec)')
plt.ylabel("Voltage Difference (mV)")

fns=[] #use this for storing different solutions if I need them later

#use the following for loop to change parameter values and or try diff initial conditions
for y0 in [3, 1, 0.25, 0.05]: #do a nested loop if doing multiple params and/or initial conds.
    parameters = [paramstuff[0], paramstuff[1], y0 * r]
    solution = spi.odeint(sys_des, [0, 0], t, args=(parameters,))
    solutionT = phase_2_volt(np.transpose(solution)[0])

    plt.plot(t, solutionT, label="R = {} nOhms".format(y0))
    
 

plt.legend()
plt.show()
