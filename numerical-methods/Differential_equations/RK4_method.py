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


    ###### RK4 method
    N = 10000
    h = (tf-ti)/(N)

    x_t = [x_0]
    v_t = [v_0]
    E_t = []

    for i in range (0,N-1):
        k1x = h*v_t[i]
        k2x = h*(v_t[i] + h/2 * (-w_0**2 * x_t[i]))
        k3x = h*(v_t[i] + h/2 * (-w_0**2 * x_t[i]))
        k4x = h*(v_t[i] + h * (-w_0**2 * x_t[i]))
        
        x_t.append(x_t[i] + 1/6 *(k1x + 2*k2x + 2*k3x +k4x))
        
        k1v = h*(-w_0**2 * x_t[i])
        k2v = h*(-w_0**2 * x_t[i] + h/2 * (-w_0**2 * v_t[i]))
        k3v = h*(-w_0**2 * x_t[i] + h/2 * (-w_0**2 * v_t[i]))
        k4v = h*(-w_0**2 * x_t[i] + h * (-w_0**2 * v_t[i]))
        
        
        v_t.append(v_t[i] + 1/6 *(k1v + 2*k2v + 2*k3v +k4v))
        
        E_t.append(0.5*k*x_t[i]**2 + 0.5*m*v_t[i]**2)
        
        
    E_t.append(0.5*k*x_t[N-1]**2 + 0.5*m*v_t[N-1]**2)    
        
    t = np.linspace(ti,tf,N)

    #x(t)
    plt.plot(t,x_t,color='firebrick',ls='--',lw=3,label='RK4 method,N = %d' %N) 
    plt.plot(t,analytic_oscilator_x(t),label='analytic solution')  
    plt.xlabel('t',fontsize='13') 
    plt.ylabel(r'$x (t)$',fontsize='13')
    plt.legend(fontsize=13)
    plt.show()

    #v(t)
    plt.plot(t,v_t,color='firebrick',ls='--',lw=3,label='RK4 method,N = %d' %N) 
    plt.plot(t,analytic_oscilator_v(t),label='analytic solution')  
    plt.xlabel('t',fontsize='13') 
    plt.ylabel(r'$v (t)$',fontsize='13')
    plt.legend(fontsize=13)
    plt.show()

    #E(t)
    plt.axhline(y=E_0,linewidth=2,ls='--',color='red',label=r'$E_0$')
    plt.plot(t,E_t,label='RK4 E')
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