#include <iostream>
#include <cmath>

using namespace std;
#include <chrono>
using namespace std::chrono;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
double even_energies_of_the_bound_state(double V, double E) {
    return sqrt(V - E) * tan(sqrt(V - E)) - sqrt(E)   ;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

double derivative_double_even_energies_of_the_bound_state(double V, double E) {
    return - tan(sqrt(V - E))/(2 * sqrt(V - E)) - 1/(2*sqrt(E)) - 1/(2*(pow(cos(sqrt(V - E)),2)))   ;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

double Bisection(double x_1, double x_2, double V, double epsilon) {

    double x_c = x_1;

    if (even_energies_of_the_bound_state(V, x_1) * even_energies_of_the_bound_state(V, x_2) >=0) {
        return 1;
    }


    for (int i = 0; i < 200; i++) {


        x_c = (x_1 + x_2) / 2;

        if (abs(x_1 - x_2) < epsilon) {
            break ;
        }

        else if (even_energies_of_the_bound_state(V, x_c) * even_energies_of_the_bound_state(V, x_1) < 0) {
            x_2 = x_c;
        }
        else {
            x_1 = x_c;
        }
    }
    return x_c ;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

double Newton_Raphson(double x_0, double V, double epsilon) {

    for (int i = 0; i < 200; i++) {

        double dumy = x_0;

        x_0 = x_0 - (even_energies_of_the_bound_state(V, x_0))/(derivative_double_even_energies_of_the_bound_state(V, x_0)) ;

        if (abs(dumy-x_0) < epsilon) {
            break;
        }

    }

    return  x_0  ;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {

    const double epsilon = 0.0000001;

    double V_0 = 10;

    cout << "\n";

    cout << "E_B obtained from Newton Raphson algorithm for V_0 = 10 \n";

    auto start = high_resolution_clock::now();

    double E_B = Newton_Raphson(0.01, V_0, epsilon);

    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();

    E_B = Newton_Raphson(8.6, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 2 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;
/////////////////////////////////////////////////////////////////////////////////////////////////////////
    cout << "E_B obtained from Bisection algorithm for V_0 = 10 \n";

    start = high_resolution_clock::now();

    E_B = Bisection(0, 0.5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();


    E_B = Bisection(8.5, 8.6, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);


    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 2  in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;
///////////////////////////////////////////////////////////////////////////////////////////////////////////
    V_0 = 20;

    cout << "E_B obtained from Newton Raphson algorithm for V_0 = 20 \n";

    start = high_resolution_clock::now();


    E_B = Newton_Raphson(5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();


    E_B = Newton_Raphson(18.5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 2 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;

/////////////////////////////////////////////////////////////////////////////////////////////////////////
    cout << "E_B obtained from Bisection algorithm for V_0 = 20 \n";

    start = high_resolution_clock::now();


    E_B = Bisection(5, 7.5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();


    E_B = Bisection(18.25, 18.5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 2  in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;
///////////////////////////////////////////////////////////////////////////////////////////////////////////
    V_0 = 30;

    cout << "E_B obtained from Newton Raphson algorithm for V_0 = 30 \n";

    start = high_resolution_clock::now();


    E_B = Newton_Raphson(14, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();


    E_B = Newton_Raphson(28.4, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 2 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;

/////////////////////////////////////////////////////////////////////////////////////////////////////////
    cout << "E_B obtained from Bisection algorithm for V_0 = 30 \n";

    start = high_resolution_clock::now();


    E_B = Bisection(13, 15, V_0, epsilon);


    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 1 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    cout << "E_B 1 in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n"  ;

    start = high_resolution_clock::now();


    E_B = Bisection(28.2, 28.5, V_0, epsilon);

    stop = high_resolution_clock::now();

    duration = duration_cast<microseconds>(stop - start);

    cout << "E_B 2 = " << E_B << "\n"  ;

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;


    cout << "E_B 2  in the even function = " << even_energies_of_the_bound_state(V_0, E_B) << "\n \n"  ;

    return 0;
}