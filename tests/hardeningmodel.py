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
    raise ValueError ("Invalid Hardening Type.")
'''

@dataclass
class Elastoplastic:
  def __init__(self, E: float, H: float, Y_0: float, hardening_type: str):
    self.E = E
    self.H = H
    self.Y_0 = Y_0
    self.sigma_n = 0
    self.epsilon_p_n = 0
    self.alpha_n = 0
    self.hardening_type = hardening_type

  def elastic_predictor(self, delta_epsilon):
    return self.E * delta_epsilon

  def check_state(self, delta_epsilon, hardening_type):
    delta_sigma_trial = self.elastic_predictor(delta_epsilon)
    sigma_trial = self.sigma_n + delta_sigma_trial

    if self.hardening_type == "Isotropic":
      Y_n = self.Y_0 + self.H * self.epsilon_p_n
      phi_trial_iso = np.linalg.norm(sigma_trial) - Y_n

    if self.hardening_type == "Kinematic":
      alpha_trial = self.alpha_n
      nu_trial = sigma_trial - alpha_trial
      phi_trial_kin = np.linalg.norm(nu_trial) - Y_n
       
    
    if phi_trial <= 0: # Material is still undergoing Elastic Deformation
      sigma_new = sigma_trial
      epsilon_p_new = self.epsilon_p_n
      alpha_new = self.alpha_n
      Y_new = self.compute_yield_stress()
      
    else: # Material is yielding/undergoing Plastic Deformation
      delta_epsilon_p = phi_trial / (self.E + self.H)

      if self.hardening_type == "Isotropic":
        sigma_new = sigma_trial - np.sign(np.linalg.norm(sigma_trial)) * self.E * delta_epsilon_p
        

      if self.hardening_type == "Kinematic":
        sigma_new = sigma_trial - np.sign(nu_trial) * self.E * delta_epsilon_p
        alpha_new = self.alpha_n + np.sign(nu_trial) * self.H * delta_epsilon_p
        
    epsilon_p_new = self.epsilon_p_n + delta_epsilon_p

    self.sigma_n = sigma_new
    self.alpha_n = alpha_new
    self.Y_n = Y_new
    self.epsilon_p_n = epsilon_p_new

    if self.hardening_type == "Isotropic":
      return sigma_new, epsilon_p_new

    if self.hardening_type == "Kinematic":
      return sigma_new, alpha_new, epsilon_p_new
