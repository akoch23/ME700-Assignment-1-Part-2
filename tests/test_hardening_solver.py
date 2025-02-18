if __name__ == "__main__":
  E = 210e9
  H = 1000
  Y_0 = 250e6

  material = Elastoplastic(E, H, Y_0)
  delta_epsilon = np.array([0.001, 0, 0])
  sigma_new, epsilon_p = material.update_stress(delta_epsilon)

  print("Updated Stress: " sigma_new)
  print("Updated Stress: ", epsilon_p)
