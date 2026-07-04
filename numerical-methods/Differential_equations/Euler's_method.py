import numpy as np
import matplotlib.pyplot as plt

###### Analytic solution

def analytic_oscilator_x(t):
    
    return x_0*np.cos(w_0*t) + (v_0/w_0) * np.sin(w_0*t)

def analytic_oscilator_v(t):
    
    return -x_0*w_0*np.sin(w_0*t) + v_0*np.cos(w_0*t)


def main():

    ti = 0
    tf = 5*(2*np.pi/w_0)

    ######  Euler’s method
    NE = 10000
    N = NE
    h = (tf-ti)/(N)


    x_tE = [x_0]
    v_tE = [v_0]
    E_tE = []

    for i in range (0,N-1):
        x_tE.append(x_tE[i] + h*v_tE[i])
        v_tE.append(v_tE[i] + h*(-w_0**2 * x_tE[i]))
        E_tE.append(0.5*k*x_tE[i]**2 + 0.5*m*v_tE[i]**2)
        
    E_tE.append(0.5*k*x_tE[N-1]**2 + 0.5*m*v_tE[N-1]**2)    
        
    t = np.linspace(ti,tf,N)

    #x(t)
    plt.plot(t,x_tE,color='firebrick',ls='--',lw=3,label='Euler’s method,N = %d' %NE) 
    plt.plot(t,analytic_oscilator_x(t),label='analytic solution')  
    plt.xlabel('t',fontsize='13') 
    plt.ylabel(r'$x (t)$',fontsize='13')
    plt.legend(fontsize=13)
    plt.show()

    #v(t)
    plt.plot(t,v_tE,color='firebrick',ls='--',lw=3,label='Euler’s method,N = %d' %NE)  
    plt.plot(t,analytic_oscilator_v(t),label='analytic solution')  
    plt.xlabel('t',fontsize='13') 
    plt.ylabel(r'$v (t)$',fontsize='13')
    plt.legend(fontsize=13)
    plt.show()

    #E(t)
    plt.axhline(y=E_0,linewidth=2,ls='--',color='red',label=r'$E_0$')
    plt.plot(t,E_tE,label='Euler’s E') 
    plt.xlabel('t',fontsize='13') 
    plt.ylabel(r'$E(t)$',fontsize='13')
    plt.legend(fontsize=13)
    plt.ticklabel_format(useOffset=False)
    plt.show()

if  __name__ == "__main__":
    plt.rcParams['figure.figsize'] = [12,8]
    k = 1
    m = 1
    x_0 = 0.1
    v_0 = 0
    w_0 = np.sqrt(k/m)
    E_0 = 0.5*k*x_0**2 + 0.5*m*v_0**2

    main()    