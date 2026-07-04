import numpy as np
import matplotlib.pyplot as plt


#Integration of exp(-x) from 0 to 1
def Gaussian_quadrature(a,b,N):
    C = np.polynomial.legendre.leggauss(N)
    Sum = 0
    c1=(b-a)/2
    c2=(b+a)/2
    for i in range(0,N):
        Sum = C[1][i]*np.exp(-(c1*C[0][i]+c2)) + Sum
        
    return Sum * (b-a)/2    

def error_Gaussian_quadrature(a,b,N):
    
    return (abs(Gaussian_quadrature(a,b,N)-1+np.exp(-1)))/(abs(-1+np.exp(-1)))

def error_values(a,b,n):
    
    e=[]
   
    for i in range (1,n+1):
        e.append(error_Gaussian_quadrature(a,b,i))
            
    return e

def N(n):

    N=np.linspace(1,n,n)
    N = [ int(i) for i in N ]
    return N




if  __name__ == "__main__":

    a=0
    b=1
    n=200
    N1=N(n)
    errors=error_values(a,b,n)

    plt.plot(N1,errors)  

    plt.title('Error v.s. N for Gaussian quadrature',fontsize='16')
    plt.ylabel('Error',fontsize='16') 
    plt.xlabel('N',fontsize='16')
    plt.show()

    print(' ' * 25, 'Error for Gaussian Quadrature')
    print(' ')
    print('N  |  Gaussian quadrature')
    Z = 16
    print(2, ' ' * 2, round(error_Gaussian_quadrature(a, b, 2), Z))
    w = 10
    for i in range(0, 6):
        print(w, ' ' * 2, round(error_Gaussian_quadrature(a, b, w), Z))
        w = w * 2

    plt.plot(N1,errors)  
    plt.title('log-log plot of Error v.s. N for Gaussian quadrature',fontsize='16')
    plt.ylabel('Error',fontsize='16') 
    plt.xlabel('N',fontsize='16')
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
