# Numerical Methods

This folder collects numerical methods exercises written in Python, Jupyter
notebooks, and a small amount of C++.

The projects cover standard topics from computational mathematics: solving
equations, interpolation, numerical differentiation and integration, LU
decomposition, and differential equation methods such as Euler and RK4. The code
is mostly educational and exploratory, with formulas and algorithms kept close to
the surface.

## Contents

- `Differential_equations/` - Euler's method and RK4 examples, including harmonic
  and anharmonic oscillator notebooks.
- `Equations/` - C++ programs for equation-solving projects, plus a notebook for
  plotting final project graphs and a project PDF.
- `InterpolationFun/` - interpolation experiments using SciPy cubic splines on
  several example datasets.
- `LU_decomposition/` - LU decomposition examples and comparisons with SciPy's
  linear algebra tools.
- `Numerical_differentiation/` - first and second numerical derivatives of
  `exp(x)` using finite-difference formulas and different step sizes.
- `Numerical_integration/` - trapezoidal rule, Simpson's rule, and Gaussian
  quadrature experiments.

## Python Setup

The Python notebooks and scripts use the usual scientific Python stack. Create an
environment and install the listed packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then open the notebooks with Jupyter:

```powershell
jupyter lab
```

You can also run individual Python scripts directly, for example:

```powershell
python .\Numerical_integration\Gaussian_quadrature.py
python .\Differential_equations\RK4_method.py
```

## C++ Notes

The C++ files in `Equations/` do not use Python dependencies. They need a C++
compiler instead. With `g++`, they can be compiled from this folder like this:

```powershell
g++ ".\Equations\TRIAL-AND-ERROR.cpp" -std=c++17 -O2 -o trial-and-error.exe
.\trial-and-error.exe

g++ ".\Equations\TWO MASSES ON A STRING.cpp" -std=c++17 -O2 -o two-masses.exe
.\two-masses.exe
```

One of the C++ files includes `bits/stdc++.h`, which is commonly available with
GCC/MinGW but not with every compiler. If compilation fails with MSVC, try using
`g++` or replace that include with the specific standard-library headers needed
by the file.

## Notes

This is an archive of study code rather than a polished numerical methods
library. Some folders include both notebooks and scripts for the same topic, and
some examples are written in a direct, formula-first style to make the numerical
method easier to follow.
