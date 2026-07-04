#include <algorithm>
#include <chrono>
#include <iostream>
#include<vector>
#include <cmath>
#include<bits/stdc++.h>
#define N 9

using namespace std;

typedef double (*IntFunctionWithOneParameter) (double x[9]);  ///// Used for putting functions f1,...,f9 into an array

//////////////////////////////////

////// Functions f1,....,f9:
double f1(double x[9]) {
    return 3*x[3] + 4*x[4] + 4*x[5] - 8   ;
}

double f2(double x[9]) {
    return 3*x[0] + 4*x[1] - 4*x[2]    ;
}

double f3(double x[9]) {
    return x[6]*x[0] - x[7]*x[1] - 10  ;
}

double f4(double x[9]) {
    return x[6]*x[3] - x[7]*x[4]   ;
}

double f5(double x[9]) {
    return x[7]*x[1] + x[8]*x[2] - 20   ;
}

double f6(double x[9]) {
    return x[7]*x[4] - x[8]*x[5]   ;
}

double f7(double x[9]) {
    return pow(x[0],2) + pow(x[3],2)  - 1   ;
}

double f8(double x[9]) {
    return pow(x[1],2) + pow(x[4],2)  - 1   ;
}

double f9(double x[9]) {
    return pow(x[2],2) + pow(x[5],2)  - 1   ;
}

//////////////////////////////////

void getCofactor(double A[N][N], double temp[N][N], int p, int q, int n)
{
    int i = 0, j = 0;

    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {

            if (row != p && col != q)
            {
                temp[i][j++] = A[row][col];

                if (j == n - 1)
                {
                    j = 0;
                    i++;
                }
            }
        }
    }
}

//////////////////////////////////

double determinant(double A[N][N], int n)  ///Determinant finder
{
    double D = 0;


    if (n == 1)
        return A[0][0];

    double temp[N][N];

    int sign = 1;

    for (int f = 0; f < n; f++)
    {
        getCofactor(A, temp, 0, f, n);
        D += sign * A[0][f] * determinant(temp, n - 1);

        sign = -sign;
    }

    return D;
}

//////////////////////////////////

void adjoint(double A[N][N],double adj[N][N])  ///Adjoint finder
{
    if (N == 1)
    {
        adj[0][0] = 1;
        return;
    }

    int sign = 1;
    double temp[N][N];

    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            getCofactor(A, temp, i, j, N);


            sign = ((i+j)%2==0)? 1: -1;


            adj[j][i] = (sign)*(determinant(temp, N-1));
        }
    }
}

//////////////////////////////////

bool inverse(double A[N][N], double inverse[N][N])  /// inverse finder
{
    double det = determinant(A, N);
    if (det == 0)
    {
        cout << "Singular matrix, can't find its inverse";
        return false;
    }

    double adj[N][N];
    adjoint(A, adj);

    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            inverse[i][j] = adj[i][j]/double(det);

    return true;
}

template<class T>

//////////////////////////////////

void display(T A[N][N])   //// for printing any matrix
{
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
            cout << A[i][j] << " ";
        cout << endl;
    }
}


//////////////////////////////////

int main()
{
    const double epsilon = 0.0000001; //// Precision

    const double h = 0.000001;  //// For derivations

    double x0[9] = {1,1,1,1,1,1,1,1,1} ; //// Initial guess

    double a[9] = {} ; //// Dummy array

    double delta_x[9] = {};  //// Delta x

    double k; /// Dummy

    double l; /// Dummy

    IntFunctionWithOneParameter functions[] = {f1,f2,f3,f4,f5,f6,f7,f8,f9,}; /// Array of function equations

    double f[9] = {}; /// f

    double F[9][9]; /// F

    double adj[N][N];  // To store adjoint of F[][]

    double inv[N][N]; // To store inverse of F[][]

    //////////////////////////////////        //////////////////////////////////        //////////////////////////////////

    for(int m=0; m<100; m++) {

        ////////////////////////////////// f calculation

        for (int i = 0; i < 9; ++i) {
            f[i] = functions[i](x0);
        }

        ////////////////////////////////// F calculation
        for (int i = 0; i < 9; ++i) {
            std::copy(x0, x0 + 9, a);

            for (int j = 0; j < 9; ++j) {
                a[i] = x0[i] + h;
                k = functions[j](a);

                a[i] = x0[i] - h;
                l = functions[j](a);

                F[j][i] = (k - l) / (2 * h);
            }
        }
        ////////////////////////////////// F^-1 calculation
        inverse(F, inv);
        ////////////////////////////////// delta_x and x_i+1 calculation

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                delta_x[i] = delta_x[i] + inv[i][j] * f[j];
            }
            x0[i] = x0[i] - delta_x[i];
        }
        ////////////////////////////////// reseting some arrays

         std::fill(std::begin(delta_x), std::end(delta_x), 0);

         std::fill(std::begin(f), std::end(f), 0);

         memset(adj,0,sizeof(adj));

         memset(inv,0,sizeof(inv));

         memset(inv,0,sizeof(F));

    }
    //////////////////////////////////        //////////////////////////////////        //////////////////////////////////

    cout <<"Solution for a given x0 :\n" ;
    for (int j = 0; j < 9; ++j) {
        cout << x0[j] << "\n" ;
    }

    cout <<" \nSolution substituted into equations f1,....,f9 :\n" ;
    for (int i = 0; i < 9; ++i) {
        cout << functions[i](x0) <<"\n";
    }

    return 0;
}