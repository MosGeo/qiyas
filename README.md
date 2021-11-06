# qias

[![Upload Python Package](https://github.com/MosGeo/qiyas/actions/workflows/python-publish.yml/badge.svg)](https://github.com/MosGeo/qiyas/actions/workflows/python-publish.yml)


qias is lightweight easy-to-use non-opinionated unit conversion Python library for scientists and engineers. It is based on graph theory and allows easy customization and addition of new units via script. Each unit need to be only defined by one existing unit. qias is smart enough to figure out the rest.

## Important note
This is a very early release to proove the concept. Everything is working as expected and there are no issues. conversion tables need to be added. Currently, there are some units for length, mass, and volume for testing.

## Philosophy
- Lightweight: it only relies on the `networkx` package to handle graph operations and `varname` to identify variable names.
- Easy-to-use: customize it easily with new units.
- non-opinionated: It does not assume anything about your data. It does not create new data type. You can pass numpy array (or datatype that can be multiplied by a number) to it without issue.

## Installation
Install it in your environment by running the command

```
pip install qiyas
```

## Getting started

```python
from qiyas import qs

# Typical use
x = 10
x_cm = qs.convert(x, 'm', 'cm')

# Immediate use (Python 3.8+)
x_m = 10
x_cm = qs.to(x_m, 'cm')

# Get multiplier information
multiplier_info = qs.get_multiplier('m', 'cm')
```

## Contribution
Contributions are welcome, especially for unit tables. Create an issue first to discuss architectural change.
