import numpy as np

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

class Elastoplastic:
  def __init__(self, E: float, H: float, Y_0: float, hardening_type: str):
      self.E = E  # Elastic modulus
      self.H = H  # Hardening modulus
      self.Y_0 = Y_0  # Initial yield stress
      self.sigma_n = 0  # Initial stress state
      self.epsilon_p_n = 0  # Initial plastic strain
      self.alpha_n = 0  # Kinematic hardening state variable
    
'''
  def elastic_predictor(self, delta_epsilon):
      # Elastic stress prediction using Hooke's law: sigma = E * epsilon
      return self.E * delta_epsilon
'''

  def yield_stress(self):
        Y_n = self.Y_0 + self.H * self.epsilon_p_n
        return Y_n

   def hardening_model(self, strain_change):
    stress_list = []
    strain_list = []
    for i, epsilon_n in enumerate(strain_change):
        if i == 0:
            stress_list.append(self.sigma_n)
            continue
        delta_epsilon_n = epsilon_n - strain_change[step-1]
        if np.isclose(delta_epsilon_n, 0):
            stress_list.append(self.sigma_n)
            continue
        self.update_step(delta_epsilon_n)
        stress_list.append(self.sigma_n)
        strain_list.append(self.epsilon_p_n)
    return stress_list

class Isotropic(Elastoplastic):
  def phi_trial(self, sigma_trial, Y_n):
      phi_trial = np.abs(sigma_trial) - Y_n
      return phi_trial

  def check_phi_trial_iso(self, phi_trial, sigma_trial):
      if phi_trial <= 0: # material deformation is still elastic
          self.sigma_n = sigma_trial
          self.epsilon_p_n = self.epsilon_p_n
      else: # material is yielding/deformation is plastic, return mapping
          delta_epsilon = phi_trial / (self.E + self.H)
          self.sigma_n = sigma_trial - np.sign(sigma_trial) * self.E * delta_epsilon
          self.epsilon_p_n = self.epsilon_p_n + delta_epsilon
          
  def step_forward_iso(self, delta_epsilon):
      Y_n = self.yield_stress()
      delta_sigma_trial = self.E * delta_epsilon
      sigma_trial = self.sigma_n + delta_sigma_trial
      phi_trial = self.phi_trial(sigma_trial,Y_n)
      self.check_phi_trial(phi_trial,sigma_trial)
   # How to return mapping?

class Kinematic(Elastoplastic):
  def __init__(self, E, H, Y_0, alpha_n):
      super().__init__(E, H, Y_0, alpha_n)
    
  def check_phi_trial_kin(self,phi_trial, sigma_trial, alpha_trial, eta_trial):
      if phi_trial <= 0: # material deformation is still elastic
          self.sigma_n = sigma_trial
          self.alpha_n = alpha_trial
          self.epsilon_p_n = self.epsilon_p_n
      else: # material is yielding/deformation is plastic, return mapping
          delta_epsilon = phi_trial / (self.E + self.H)
          self.sigma_n = sigma_trial - np.sign(eta_trial) * self.E * delta_epsilon
          self.alpha_n = self.alpha_n + np.sign(eta_trial) * self.H * delta_epsilon
          self.epsilon_p_n = self.epsilon_p_n + delta_epsilon

  def step_foward_kin(self, delta_epsilon):
        # Elastic predictor step with sigma trial
        sigma_trial = self.sigma_n + self.E * delta_epsilon
        alpha_trial = self.alpha_n
        eta_trial = sigma_trial - alpha_trial
        phi_trial = np.abs(eta_trial) - self.Y_0

        # Check if the material is experiencing elastic or plastic deformation and update values accordingly
        self.check_phi_trial(phi_trial,sigma_trial,alpha_trial,eta_trial)
        
      
