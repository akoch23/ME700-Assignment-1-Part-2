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
        self.E = E  # Elastic modulus
        self.H = H  # Hardening modulus
        self.Y_0 = Y_0  # Initial yield stress
        self.sigma_n = 0  # Initial stress state
        self.epsilon_p_n = 0  # Initial plastic strain
        self.alpha_n = 0  # Kinematic hardening state variable
        self.hardening_type = hardening_type  # Type of hardening (Isotropic or Kinematic)
        
    def elastic_predictor(self, delta_epsilon):
        # Elastic stress prediction using Hooke's law: sigma = E * epsilon
        return self.E * delta_epsilon
    
    def check_state(self, delta_epsilon):
        # Compute trial stress
        delta_sigma_trial = self.elastic_predictor(delta_epsilon)
        sigma_trial = self.sigma_n + delta_sigma_trial
        
        # Check hardening type and compute corresponding trial yield condition
        if self.hardening_type == "Isotropic":
            Y_n = self.Y_0 + self.H * self.epsilon_p_n  # Yield stress with isotropic hardening
            phi_trial_iso = np.linalg.norm(sigma_trial) - Y_n  # Yield condition for isotropic
            phi_trial = phi_trial_iso

        elif self.hardening_type == "Kinematic":
            alpha_trial = self.alpha_n  # Kinematic hardening state
            nu_trial = sigma_trial - alpha_trial  # Trial stress for kinematic model
            Y_n = self.Y_0  # Constant yield stress in kinematic hardening
            phi_trial_kin = np.linalg.norm(nu_trial) - Y_n  # Yield condition for kinematic
            phi_trial = phi_trial_kin

        elif self.hardening_type == "Both":
            # Isotropic + Kinematic combined
            Y_n = self.Y_0 + self.H * self.epsilon_p_n  # Isotropic hardening contribution
            alpha_trial = self.alpha_n
            nu_trial = sigma_trial - alpha_trial  # Combined trial stress for both models
            phi_trial_iso = np.linalg.norm(sigma_trial) - Y_n
            phi_trial_kin = np.linalg.norm(nu_trial) - Y_n
            phi_trial = max(phi_trial_iso, phi_trial_kin)  # Choose the max phi from both models
        
        # Check if material is elastic or plastic
        if phi_trial <= 0:  # Elastic regime
            sigma_new = sigma_trial
            epsilon_p_new = self.epsilon_p_n
            alpha_new = self.alpha_n
            Y_new = Y_n  # Yield stress (can be isotropic or constant)
        else:  # Plastic regime
            delta_epsilon_p = phi_trial / (self.E + self.H)
            
            if self.hardening_type == "Isotropic":
                sigma_new = sigma_trial - np.sign(np.linalg.norm(sigma_trial)) * self.E * delta_epsilon_p
            elif self.hardening_type == "Kinematic":
                sigma_new = sigma_trial - np.sign(nu_trial) * self.E * delta_epsilon_p
                alpha_new = self.alpha_n + np.sign(nu_trial) * self.H * delta_epsilon_p
            elif self.hardening_type == "Both":
                # In both models, consider contributions from both isotropic and kinematic
                sigma_new = sigma_trial - np.sign(nu_trial) * self.E * delta_epsilon_p
                alpha_new = self.alpha_n + np.sign(nu_trial) * self.H * delta_epsilon_p
                # For combined hardening, we can also adjust yield stress based on both models

            epsilon_p_new = self.epsilon_p_n + delta_epsilon_p
            Y_new = Y_n

        # Update internal state
        self.sigma_n = sigma_new
        self.alpha_n = alpha_new
        self.Y_n = Y_new
        self.epsilon_p_n = epsilon_p_new

        # Return updated values depending on hardening model
        if self.hardening_type == "Isotropic":
            return sigma_new, epsilon_p_new
        elif self.hardening_type == "Kinematic":
            return sigma_new, alpha_new, epsilon_p_new
        elif self.hardening_type == "Both":
            return sigma_new, alpha_new, epsilon_p_new  # Could return a combination of both states
