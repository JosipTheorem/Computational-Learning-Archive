import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve


def LU(A): ### LU decomposition
    
    n = len(A)
    
    U = np.zeros((n, n))
    L = np.eye(n)
    
    for k in range(n):
        
        U[k, k:] = A[k, k:] - L[k,:k] @ U[:k,k:]
        L[(k+1):,k] = (A[(k+1):,k] - L[(k+1):,:] @ U[:,k]) / U[k, k]
    
    return L, U

def solve(A,w):  # solving for x
    LU,p = lu_factor(A) 
    return lu_solve((LU,p),w)

def main():

    A = np.array([[2., 5., 8], [5., 2., 2.], [7., 5., 6.]])
    L,U = LU(A)

    print('---------------\nOriginal matrix:\n',A,'\n---------------')
    print('LU decomposition:\nL:')
    print(L)
    print('U:\n',U)
    print('---------------\nA = LU:\n',L@U)
    print('---------------\ndet(A)=u11*u22*u33:\ndet(A):\n',np.linalg.det(A))
    print('u11*u22*u33:\n',U[0][0]*U[2][2]*U[1][1])


if  __name__ == "__main__":
    main()