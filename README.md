# Elastoplastic Hardening Model

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)




### Elastoplastic Hardening Model Algorithm

**Elastoplastic Hardening Model** is a mathematical model for approximating and visualing the stress/strain behavior of a material undergoing elastic and plastric strain/hardening. 




### Conda environment installation and testing

To install this package, first establish a new conda environment:
```bash
conda create --name elastoplastic-solver-env python=3.12
```
Afterwards, activate the environment:
```bash
conda activate elastoplastic-solver-env
```

You can double check if the installed version of python is indeed version 3.12 in the new conda environment:
```bash
python --version
```

Ensure that pip is using the latest version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

Create an editable install of the newton's method code (reminder: make sure you're in the right directory for this step, using the cd: [insert folder path] command)
```bash
pip install -e .
```

Test that the code is working with pytest:
```bash
pytest -v --cov-hardening_model --cov-report term-missing
```

Code coverage should be 100%
