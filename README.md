# Computational Learning Archive

This repository collects older learning projects, notebooks, simulations, and
small experiments from my student work in computational mathematics, physics,
numerical methods, and machine learning.

The original repositories were imported into subfolders so the work can live in
one place while preserving the old project histories. This is an archive and
learning lab, not a single polished Python package.

## Repository Map

- [physics-simulations](physics-simulations/) - physics simulations and visual studies, including
  mechanics, optics, electrodynamics, Monte Carlo experiments, orbital mechanics,
  general relativity, and graphene band-structure work. This is the largest and
  most mixed folder; it includes Python notebooks, scripts, Quantum ESPRESSO
  inputs/outputs, plots, and archive material.
- [numerical-methods](numerical-methods/) - numerical methods exercises in Python, Jupyter, and a
  small amount of C++. Topics include equation solving, interpolation, numerical
  differentiation, numerical integration, LU decomposition, and differential
  equation solvers such as Euler's method and RK4.
- [mathematical-sets-and-sequences](mathematical-sets-and-sequences/) - visual experiments with mathematical
  patterns and sequences, including the Mandelbrot set, the Recaman sequence,
  and toothpick patterns.
- [machine-learning](machine-learning/) - a small collection of early machine learning exercises,
  including hand-computed linear regression and a from-scratch NumPy neural
  network.
- [islp-book-problems](islp-book-problems/) - selected solutions and experiments from *An
  Introduction to Statistical Learning with Python*.

Each subfolder has its own README with more specific notes.

## Running Code

There is no single environment for the whole repository. Use the README inside
the folder you want to run.

Most folders that need local Python dependencies include their own
`requirements.txt` file:

- [physics-simulations/requirements.txt](physics-simulations/requirements.txt)
- [numerical-methods/requirements.txt](numerical-methods/requirements.txt)
- [mathematical-sets-and-sequences/requirements.txt](mathematical-sets-and-sequences/requirements.txt)
- [machine-learning/requirements.txt](machine-learning/requirements.txt)

The [islp-book-problems](islp-book-problems/) folder points readers to the official ISLP resources
instead of maintaining a local requirements file.

A typical Python workflow looks like this:

```powershell
cd path\to\folder
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

Some material needs additional tooling outside Python. For example,
[numerical-methods](numerical-methods/) contains C++ files, and [physics-simulations/Graphene](physics-simulations/Graphene/)
contains Quantum ESPRESSO-related inputs, outputs, and post-processing files.
Those tools are documented in the relevant folder READMEs where possible.

## Archive Notes

This repository is intentionally uneven. Some projects are polished notebooks,
some are quick experiments, some contain saved plots or outputs, and some preserve
partial work from the original repositories.

The goal is to keep the work discoverable and understandable without pretending
that every folder is a finished library. If you are browsing the repository, start
with the folder README files and treat the code as study material.
