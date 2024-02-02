import matplotlib
import matplotlib.pyplot as plt

def simple_SIR(S0, I0, R0, beta, gamma, dt, tmax):
    '''
    '''
    # Initial values
    S = S0
    I = I0
    R = R0
    N = S + I + R
    
    # Store each time point
    S_list = [S0]
    I_list = [I0]
    R_list = [R0]
    
    # If 0<dt<1, can't use range
    t_list = []
    if (dt > 0 and dt < 1):
        count = 0
        while (count < tmax):
            t_list.append(count)
            count += dt
    else:  # Get list of times using range
        t_list = list(range(0,tmax, dt))

    # Iterate over all times
    for t in t_list:
        # Calculate instantaneous rates of change
        dS = -beta * S * I / N
        dI = (beta * S * I / N) - (gamma * I)
        dR = gamma * I
    
        # Update S, I, R
        S = S + dt * dS
        I = I + dt * dI
        R = R + dt * dR
        
        # Store values
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    
    # Complete list of times, return results
    t_list.append(tmax)
    
    return t_list, S_list, I_list, R_list

def plotSIR(t, S, I, R, x_label, y_label, title, outfile):
    '''
    '''
    fig, ax = plt.subplots()
    ax.plot(t, S, label='S Aidan')
    ax.plot(t, I, label='I Aidan')
    ax.plot(t, R, label='R Aidan')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

    plt.savefig(outfile, bbox_inches='tight')