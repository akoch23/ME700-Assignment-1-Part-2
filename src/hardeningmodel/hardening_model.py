import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass

'''
hardening_type = input("Please enter which type of hardening model you would like to use for your chosen material: ")

try:
  if hardening_type == "Isotropic":
    model_iso = True
    model_kin = False
  elif hardening_type == "Kinematic":
    model_kin = True
    model_iso = False
  elif hardening_type == "Both":
    model_kin = True
    model_iso = True
  else:
    raise error
'''

@dataclass
class Elastoplastic:
  def __init__(self, E: float, H: float, Y_0: float):
    self.E = E
    self.H = H
    self.Y_0 = Y_0
    self.sigma_n = 0
    self.epsilon_p_n = 0
    self.alpha_n = 0

  def compute_yield_stress(self):
    return self.Y_0 + self.H * self.epsilon_p_n

  def elastic_predictor(self, delta_epsilon):
    return self.E * delta_epsilon

  def check_state(self, delta_epsilon):
    delta_sigma_trial = self.elastic_predictor(delta_epsilon)
    sigma_trial = self.sigma_n + delta_sigma_trial

    if hardening_type == "Isotropic" or hardening_type = "Both":
      Y_trial = self.compute_yield_stress()
    else:
      Y_trial = self.Y_0

    if hardening_type == "Kinematic" or hardening_type == "Both":
            alpha_trial = self.alpha_n
        else:
            alpha_trial = 0
          
    nu_trial = sigma_trial - alpha_trial 
    phi_trial = np.linalg.norm(sigma_trial) - Y_n

    if phi_trial <= 0:
      sigma_new = sigma_trial
      alpha_new = self.alpha_n
      epsilon_p_new = self.epsilon_p_n
      Y_new = self.compute_yield_stress()
    else:
      delta_epsilon_p = phi_trial / (self.E + self.H)

      if hardening_type == "Isotropic" or hardening_type == "Both":
        sigma_new = sigma_trial - np.sign(np.linalg.norm(sigma_trial)) * self.E * delta_epsilon_p
      else:
        alpha_new = self.alpha_n

      if hardening_type == "Isotropic" or hardening_type == "Both":
        Y_new = self.Y_0 + self.H * self.epsilon_p_n
      else:
        Y_new = self.Y_n

      epsilon_p_new = self.epsilon_p_n + delta_epsilon_p

    self.sigma_n = sigma_new
    self.alpha_n = alpha_new
    self.Y_n = Y_new
    self.epsilon_p_n = epsilon_p_new
    
    return sigma_new, epsilon_p_new
