import numpy as np
import matplotlib.pyplot as plt

def diff1 (x,h):
    
    return (np.exp(x+h)-np.exp(x-h))/(2*h)

def diff2 (x,h):
    
    return (np.exp(x+h)-2*np.exp(x)+np.exp(x-h))/(h**2)

def error1 (x,h):
    
    return np.log10(abs((diff1(x,h)-np.exp(x))/(np.exp(x))))

def error2 (x,h):
    
    return np.log10(abs((diff2(x,h)-np.exp(x))/(np.exp(x))))

def min1 (x):
    a=[]
    m = np.linspace(10e-7,10e-5,10000)
    
    for i in range (0, len(m)):
        a.append(error1 (m[i],x))
        
    return m[a.index(min(a))]

def min2 (x):
    a=[]
    m = np.linspace(10e-5,10e-3,10000)
    
    for i in range (0, len(m)):
        a.append(error2 (m[i],x))
        
    return m[a.index(min(a))]
    

def main():

    h1=np.linspace(0.1,0.000001,10000)
    h2=np.linspace(0.000001,0.0000000000000001,10000)
    h= np.concatenate((h1, h2))
    fig1, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11) = plt.subplots(11, 1,  sharey=True, figsize=[8,100])
    ax1.plot(np.log10(h),error1(0,h),color='black')
    #ax1.set_title('x = 0, h_min = %lf' %min1(0) ,loc='right')
    ax1.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax1.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax2.plot(np.log10(h),error1(1,h),color='black')
    ax2.set_title('x = 0, h_min = %lf' %min1(1) ,loc='right')
    ax2.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax2.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax3.plot(np.log10(h),error1(2,h),color='black')
    ax3.set_title('x = 0, h_min = %lf' %min1(2) ,loc='right')
    ax3.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax3.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax4.plot(np.log10(h),error1(3,h),color='black')
    ax4.set_title('x = 0, h_min = %lf' %min1(3) ,loc='right')
    ax4.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax4.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax5.plot(np.log10(h),error1(4,h),color='black')
    ax5.set_title('x = 0, h_min = %lf' %min1(4) ,loc='right')
    ax5.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax5.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax6.plot(np.log10(h),error1(5,h),color='black')
    ax6.set_title('x = 0, h_min = %lf' %min1(5) ,loc='right')
    ax6.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax6.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax7.plot(np.log10(h),error1(6,h),color='black')
    ax7.set_title('x = 0, h_min = %lf' %min1(6) ,loc='right')
    ax7.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax7.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax8.plot(np.log10(h),error1(7,h),color='black')
    ax8.set_title('x = 0, h_min = %lf' %min1(7) ,loc='right')
    ax8.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax8.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax9.plot(np.log10(h),error1(8,h),color='black')
    ax9.set_title('x = 0, h_min = %lf' %min1(8) ,loc='right')
    ax9.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax9.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax10.plot(np.log10(h),error1(9,h),color='black')
    ax10.set_title('x = 0, h_min = %lf' %min1(9) ,loc='right')
    ax10.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax10.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax11.plot(np.log10(h),error1(10,h),color='black')
    ax11.set_title('x = 0, h_min = %lf' %min1(10) ,loc='right')
    ax11.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax11.set_ylabel(r'$\epsilon $',fontsize=13) 

    #plt.legend(fontsize=20)
    fig1.suptitle("First Derivative Error", fontsize=16)
    #plt.tight_layout()
    plt.show()

    fig2, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11) = plt.subplots(11, 1,  sharey=True, figsize=[8,50])
    ax1.set_title('x = 0, h_min = %lf' %min2(0) ,loc='right')
    ax1.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax1.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax2.plot(np.log10(h),error2(1,h),color='black')
    ax2.set_title('x = 0, h_min = %lf' %min2(1) ,loc='right')
    ax2.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax2.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax3.plot(np.log10(h),error2(2,h),color='black')
    ax3.set_title('x = 0, h_min = %lf' %min2(2) ,loc='right')
    ax3.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax3.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax4.plot(np.log10(h),error2(3,h),color='black')
    ax4.set_title('x = 0, h_min = %lf' %min2(3) ,loc='right')
    ax4.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax4.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax5.plot(np.log10(h),error2(4,h),color='black')
    ax5.set_title('x = 0, h_min = %lf' %min2(4) ,loc='right')
    ax5.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax5.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax6.plot(np.log10(h),error2(5,h),color='black')
    ax6.set_title('x = 0, h_min = %lf' %min2(5) ,loc='right')
    ax6.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax6.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax7.plot(np.log10(h),error2(6,h),color='black')
    ax7.set_title('x = 0, h_min = %lf' %min2(6) ,loc='right')
    ax7.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax7.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax8.plot(np.log10(h),error2(7,h),color='black')
    ax8.set_title('x = 0, h_min = %lf' %min2(7) ,loc='right')
    ax8.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax8.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax9.plot(np.log10(h),error2(8,h),color='black')
    ax9.set_title('x = 0, h_min = %lf' %min2(8) ,loc='right')
    ax9.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax9.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax10.plot(np.log10(h),error2(9,h),color='black')
    ax10.set_title('x = 0, h_min = %lf' %min2(9) ,loc='right')
    ax10.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax10.set_ylabel(r'$\epsilon $',fontsize=13) 

    ax11.plot(np.log10(h),error2(10,h),color='black')
    ax11.set_title('x = 0, h_min = %lf' %min2(10) ,loc='right')
    ax11.set_xlabel(r'$log_{10} h$',fontsize=13) 
    ax11.set_ylabel(r'$\epsilon $',fontsize=13) 

    fig2.suptitle("Second Derivative Error", fontsize=16)
    #plt.tight_layout()
    plt.show()

    print('first derivative') 
    print(' ')
    print('x,         exp(x),         h=0.1,               h=0.01,          h=0.0001,           h=0.000001,         h=0.0000001')
    x=0
    print(x, ' '*8,np.exp(x), ' '*8,diff1(x,0.1), ' '*1 ,diff1(x,0.01), ' '*1,diff1(x,0.0001), ' '*1,diff1(x,0.000001), ' '*1,diff1(x,0.00000000001))

    for x in range(1,11):
            print(x, ' '*1 ,np.exp(x), ' '*1,diff1(x,0.1), ' '*1 ,diff1(x,0.01), ' '*1,diff1(x,0.0001), ' '*1,diff1(x,0.000001), ' '*1,diff1(x,0.00000000001))


    print('second derivative') 
    print(' ')
    print('x,         exp(x),         h=0.1,               h=0.01,          h=0.0001,           h=0.000001,         h=0.00000000001')
    x=0
    print(x, ' '*8,np.exp(x), ' '*8,diff1(x,0.1), ' '*1 ,diff1(x,0.01), ' '*1,diff1(x,0.0001), ' '*1,diff1(x,0.000001), ' '*1,diff1(x,0.00000000001))

    for x in range(1,11):
            print(x, ' '*1 ,np.exp(x), ' '*1,diff2(x,0.1), ' '*1 ,diff2(x,0.01), ' '*1,diff2(x,0.0001), ' '*1,diff2(x,0.000001), ' '*1,diff2(x,0.00000000001))



if  __name__ == "__main__":
    main()