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
# Elastoplastic Base Class
class Elastoplastic:
    def __init__(self, E: float, H: float, Y_0: float): # Initialize material property/state variables
        self.E = E  # Elastic modulus
        self.H = H  # Hardening modulus
        self.Y_0 = Y_0  # Initial yield stress
        self.sigma_n = 0  # Initial stress state
        self.epsilon_p_n = 0  # Initial plastic strain
        self.alpha_n = 0  # Kinematic hardening state variable
        
    def yield_stress(self): # Function containing current yield stress formula
        Y_n = self.Y_0 + self.H * self.epsilon_p_n
        return Y_n
    
    def hardening_model(self, strain_change): # Main data collection function that appends stress and strain values calculated from later classes/functions to lists which will be used for graphing.
        stress_list = [] # List of stress values calculated at each strain increment
        strain_list = [] # List of strain values that will be defined by user
        for i, epsilon_n in enumerate(strain_change): # Loop over each strain step and calculate corresponding stress
            if i == 0: # IMPORTANT: At first step the stress remains at its initial value
                stress_list.append(self.sigma_n)
                continue
            delta_epsilon_n = epsilon_n - strain_change[i-1]
          
            if np.isclose(delta_epsilon_n, 0): # Skip value if the strain change is close to zero (no change in strain)
                stress_list.append(self.sigma_n)
                continue
            self.step_forward(delta_epsilon_n)
            stress_list.append(self.sigma_n)
            strain_list.append(self.epsilon_p_n)
        return stress_list

class Isotropic(Elastoplastic): # Sub-class of Elastoplastic that defines operations for Isotropic Hardening model
    def phi_trial(self, sigma_trial, Y_n): # Trial Yield function value
        phi_trial = np.abs(sigma_trial) - Y_n
        return phi_trial

    def check_phi_trial(self, phi_trial, sigma_trial): # Key function that verifies previous Trial Yield function and which will be used to predict if the material remains elastic or has begun to yield
        if phi_trial <= 0: # material deformation is still elastic
            self.sigma_n = sigma_trial
            self.epsilon_p_n = self.epsilon_p_n
        else: # material is yielding/deformation is plastic, return mapping
            delta_epsilon = phi_trial / (self.E + self.H)
            self.sigma_n = sigma_trial - np.sign(sigma_trial) * self.E * delta_epsilon
            self.epsilon_p_n = self.epsilon_p_n + delta_epsilon
            
    def step_forward(self, delta_epsilon): # Function that performs elastic predictor step and returns updated stress and trial stress values
        Y_n = self.yield_stress()
        delta_sigma_trial = self.E * delta_epsilon
        sigma_trial = self.sigma_n + delta_sigma_trial
        phi_trial = self.phi_trial(sigma_trial,Y_n)
        self.check_phi_trial(phi_trial,sigma_trial)
   # How to return mapping?

class Kinematic(Elastoplastic): # Sub-class of Elastoplastic that defines operations for Kinematic Hardening model
    def __init__(self, E, H, Y_0, alpha_n):
        super().__init__(E, H, Y_0, alpha_n)
        
    def check_phi_trial(self,phi_trial, sigma_trial, alpha_trial, eta_trial):
        if phi_trial <= 0: # material deformation is still elastic
            self.sigma_n = sigma_trial
            self.alpha_n = alpha_trial
            self.epsilon_p_n = self.epsilon_p_n
            
        else: # material is yielding/deformation is plastic, return mapping
            delta_epsilon = phi_trial / (self.E + self.H)
            self.sigma_n = sigma_trial - np.sign(eta_trial) * self.E * delta_epsilon
            self.alpha_n = self.alpha_n + np.sign(eta_trial) * self.H * delta_epsilon
            self.epsilon_p_n = self.epsilon_p_n + delta_epsilon

        def step_forward(self, delta_epsilon): # Function that performs elastic predictor step and returns updated stress, trial stress, and back stress values
        # Elastic predictor step with sigma trial
            sigma_trial = self.sigma_n + self.E * delta_epsilon
            alpha_trial = self.alpha_n
            eta_trial = sigma_trial - alpha_trial
            phi_trial = np.abs(eta_trial) - self.Y_0

        # Check if the material is experiencing elastic or plastic deformation and update values accordingly
        self.check_phi_trial(phi_trial,sigma_trial,alpha_trial,eta_trial)
        
      
