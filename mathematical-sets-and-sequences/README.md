# Mathematical Sets and Sequences

This folder contains small Python experiments for generating and visualizing
mathematical sequences, patterns, and sets.

The projects are written as a mix of Jupyter notebooks and standalone Python
scripts. The code is exploratory and visual: the goal is to see the structure of
the pattern, not to build a reusable Python package.

## Contents

- `Mandelbrot/` - builds a grid of complex numbers and plots a sparse view of
  the Mandelbrot set.
- `Recaman/` - generates the Recaman sequence and draws the classic semicircle
  visualization.
- `ToothpickPatterns/` - simulates the toothpick pattern generation process and
  plots the resulting structure.

Each folder contains either a notebook, a Python script, or both. Some folders
also include saved preview images from the generated plots.

## Inspiration

- Toothpick pattern, inspired by Numberphile:
  https://www.youtube.com/watch?v=_UtCli1SgjI
- Recaman sequence, inspired by Numberphile:
  https://www.youtube.com/watch?v=_UtCli1SgjI

## Running The Code

Create a Python environment and install the small dependency set:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then open the notebooks with Jupyter or run one of the scripts directly:

```powershell
jupyter lab
python .\Mandelbrot\Mandelbrot.py
python .\Recaman\Recaman.py
python .\ToothpickPatterns\ToothpickPatterns.py
```

## Notes

These are learning experiments. Some implementations intentionally build the
objects step by step with loops and explicit arrays so the construction is easy
to follow visually.
