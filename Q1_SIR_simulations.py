import SIR_utils as sir

ta, Sa, Ia, Ra = sir.simple_SIR(S0=999, I0=1, R0=0, beta=1, gamma=0.5, dt=0.1, tmax=50)
sir.plotSIR(ta, Sa, Ia, Ra, 'Time', '# of People', 'Simple SIR - Beta = 1', 'SIR_sim_A.png')

tb, Sb, Ib, Rb = sir.simple_SIR(S0=999, I0=1, R0=0, beta=1.5, gamma=0.5, dt=0.1, tmax=50)
sir.plotSIR(tb, Sb, Ib, Rb, 'Time', '# of People', 'Simple SIR - Beta = 1.5', 'SIR_sim_B.png')

tc, Sc, Ic, Rc = sir.simple_SIR(S0=999, I0=1, R0=0, beta=2, gamma=0.5, dt=0.1, tmax=50)
sir.plotSIR(tc, Sc, Ic, Rc, 'Time', '# of People', 'Simple SIR - Beta = 2', 'SIR_sim_C.png')