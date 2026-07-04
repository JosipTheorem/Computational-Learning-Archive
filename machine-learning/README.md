# Machine Learning

This folder contains a small set of early machine learning exercises and
from-scratch implementations.

It is split into two parts:

- ` Traditional_ml/` - a Jupyter notebook that works through a hand-computed
  linear regression example, including the regression formulas and a simple plot.
- `Deep_learning/` - a NumPy implementation of a small fully connected neural
  network trained on synthetic two-dimensional Gaussian data.

## Contents

- ` Traditional_ml/Hand_Linear_Regression.ipynb` - manual linear regression with
  measured current/voltage data and visualization of the fitted line.
- `Deep_learning/Fully_Connected_NN_Numpy.py` - a basic two-layer neural network
  implemented mostly from scratch with NumPy, plus simple classification metrics
  from scikit-learn.

## Running The Code

Create a Python environment and install the small set of dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then open the notebook with Jupyter or run the neural network script directly:

```powershell
jupyter lab
python .\Deep_learning\Fully_Connected_NN_Numpy.py
```

## Notes

This is a learning folder rather than a polished machine learning package. The
code is intentionally close to the underlying formulas, especially in the linear
regression notebook and the NumPy neural network implementation.
