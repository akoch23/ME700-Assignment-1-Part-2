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
pytest -v --cov=newtonsmethod --cov-report term-missing
```

Code coverage should be 100%


## Solver Description

### Variables

* `E`: Elastic Modulus of material
* `E_t`: Tangent Modulus of material
* `H`: Plastic Modulus of material
* `Y_0`: Initial Yield Stress of material
* `Y_n`: Yield Stress of material at step "n"
* `delta_epsilon`: Change in strain of material
* `sigma_n`: Current Stress on material at step "n"
* `delta_sigma_trial`: Change in Trial Stress, equal to E * delta_epsilon
* `sigma_trial`: Trial Stress, equal to sigma_n + delta_sigma_trial
* `epsilon_p_n`: Current Plastic Strain of material at step "n"
* `alpha_n`: Back Stress on material (only considering during Kinematic Hardening)
* `phi_trial`: Trial Stress State, Yield Function equal to |sigma_trial| - Y_n

### Classes
* Elastoplastic: Parent Class for "Isotropic" and "Kinematic" classes which utilize separate solver formulae for input variables.

### Files

* *src/hardeningmodel/hardening_model.py*: Contains main functions for iteratively calculating stress values based on input strain values and selected hardening mode (model type).
* *tests/test_hardening_model.py*: Test commands for main file *hardening_model*
* *tutorial/tutorial_hardeningmodel.py*: Tutorial file containing six example problems that can be copied and run
```

Code coverage should be 100%
