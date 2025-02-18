import matplotlib.pyplot as plt
import numpy as np

class Elastoplastic:
  def __init__(self, E, H, Y_0):
    self.E = E
    self.H = H
    self.Y_0 = Y_0
    self.sigma_n = 0
    self.epsilon_p_n = 0

  def elastic_stress(self, epsilon):
    return self.E * epsilon

  def accumulated_plastic_strain(self, delta_epsilon_p):
    return np.linalg.norm(delta_epsilon_p)

  def update_stress(self, delta_epsilon):
    sigma_e = self.elastic_stress(delta_epsilon)
    Y = self.Y_0 + self.H * self.epsilon_p_n

  if np.linalg.norm(self.sigma_n) > Y:
    delta_epsilon_p = delta_epsilon - (self.sigma_n / self.E)
    self.epsilon_p_n += self.accumulated_plastic_strain(delta_epsilon_p)
    sigma_new = self.sigma_n - (self.sigma_n / np.linalg.norm(self.sigma_n)) * (np.linalg.norm(self.sigma_n) - Y)

  else:
    self.epsilon_p_n += 0
    sigma_new = sigma_e

  self.sigma_n = sigma_new
  return sigma_new, self.epsilon_p_n

if __name__ == "__main__":
  E = 210e9
  H = 1000
  Y_0 = 250e6

  material = Elastoplastic(E, H, Y_0)
  delta_epsilon = np.array([0.001, 0, 0])
  sigma_new, epsilon_p = material.update_stress(delta_epsilon)

  print("Updated Stress: " sigma_new)
  print("Updated Stress: ", epsilon_p)
