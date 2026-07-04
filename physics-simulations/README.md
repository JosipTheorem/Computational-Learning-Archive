# Physics Simulations

This folder collects physics simulations, numerical experiments, and visual
studies written mostly in Python and Jupyter notebooks.

The projects range from classical mechanics and optics to orbital motion,
general relativity, electrodynamics, Monte Carlo experiments, and graphene band
structure work. Some folders are compact notebook studies; the `Graphene/` folder
is more of a computational-materials archive with Quantum ESPRESSO inputs,
outputs, post-processing scripts, and saved figures.

## Contents

- `Electrodynamics/` - a notebook study of simple kernel orbits using SciPy,
  SymPy, and numerical integration tools.
- `Graphene/` - graphene band structure calculations, Quantum ESPRESSO input and
  output files, unfolding scripts, vacancy and polaron cases, and saved plots of
  band structures, density of states, and wavefunctions.
- `Mechanics/` - triple pendulum work, including a notebook and accompanying PDF.
- `Monte_carlo/` - Monte Carlo style experiments, including a notebook inspired
  by Veritasium's success paradox discussion.
- `Optics/` - ray tracing through a sphere using numerical integration and
  geometric optics relationships.
- `Orbital Mechanics/` - Newtonian central-force and N-body simulations, plus
  general-relativistic Schwarzschild/geodesic notebooks and scripts.

## Inspiration

- Success paradox / Monte Carlo notebook, inspired by Veritasium:
  https://www.youtube.com/watch?v=3LopI4YeC4I

## Python Setup

The Python notebooks and scripts use scientific Python packages, plotting tools,
and a few optional packages for interactive or materials-science work. Create an
environment and install the dependencies with:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then open the notebooks with Jupyter:

```powershell
jupyter lab
```

You can also run individual scripts directly, for example:

```powershell
python ".\Orbital Mechanics\Newton's mechanics\N_body_gravitational_problem_OOP.py"
python ".\Orbital Mechanics\General Relativity\Schwarzschild_black_hole_inPlane.py"
python ".\Graphene\1x1_bands\Graphene_1x1.py"
```

## Graphene And Quantum ESPRESSO Notes

The `Graphene/` folder includes files from electronic-structure calculations,
including `.in`, `.out`, `.gnu`, `.dat`, `.xml`, `.UPF`, and image outputs. The
Python requirements cover plotting and post-processing scripts, but they do not
install Quantum ESPRESSO itself.

To rerun the original electronic-structure calculations, install Quantum
ESPRESSO separately and use the provided input files where available. Some input
or output files are incomplete or intentionally preserved as archive material.
For example, `Graphene/2x2_bands/Input_and_output_files_are_lost.txt` notes that
some files from that calculation are missing.

The band-unfolding scripts use specialized Python packages such as `banduppy`,
`ase`, and `seekpath`. These are included in `requirements.txt`, but they are
mainly relevant for the graphene post-processing work.

## Notes

This is an archive of study and exploration code, not a polished physics
simulation package. Some notebooks contain saved outputs, exploratory cells, or
hard-coded constants from the original experiments. The goal is to preserve the
work and make the folder understandable enough to revisit later.
