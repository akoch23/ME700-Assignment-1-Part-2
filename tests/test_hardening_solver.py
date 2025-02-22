import numpy as np
from hardening_model import Isotropic
import pytest

def Isotropic_test():
    E = 1000
    E_t = 100
    H = (E*E_t)/(E-E_t)
    return IH(E=E, H = H, Y_0 = 10)

def Kinematic_test():
    E = 1000
    E_t = 100
    H = (E*E_t)/(E-E_t)
    return KH(E=E, H = H, Y_0 = 10)

def test_yield_stress(Isotropic_test):
    found = Isotropic_test.yield_stress()
    known = 10
    assert known == found

def test_phi_trial(Isotropic_test):
    found = Isotropic_test.phi_trial(20,10)
    known = 10
    assert known == found

def yield_check(Isotropic_test):
    #founde = Isotropic_test.check_phi_trial(phi_trial = -2.5,sigma_trial = 7.5)
    #knowne = 7.5#,0
    Isotropic_test.check_phi_trial(phi_trial = 10, sigma_trial = 20)
    known = 11#,0.005
    assert np.isclose(known, Isotropic_test.sigma_n)

def test_step(Isotropic_test):
    Isotropic_test.step_forward(delta_epsilon = 0.02)
    assert np.isclose(Isotropic_test.sigma_n, 11)

def test_model(Isotropic_test):
    epsilon = np.array([0,0,0.001001001001001001])
    found = Isotropic_test.hardening_model(epsilon)
    known = np.array([0,0,1.0010010010010015])
    assert np.allclose(known, found,atol=1e-15)

# Testing equivalent for Kinematic
