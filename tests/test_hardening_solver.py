import numpy as np
import matplotlib.pyplot as plt
from hardening_model import Elastoplastic

material = Elastoplastic (E, H, Y_0)
strain_incr = np.linspace(0, 0.05, 100)
stress_values = []
plastic_strain_values = []

for delta_epsilon in strain_increment:
  sigma_new, epsilon_p_new = material.check_state(delta_epsilon)
  stress_values.append(np.linalg.norm(sigma_new))
  plastic_strain_values.append(epsilon_p_new)

plt.plot(strain_increments, stress_values, label="Stress")
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title("Stress vs. Strain Curve")
plt.grid(True)
plt.legend()
plt.show()

plt.plot(strain_increments, plastic_strain_values, label="Plastic Strain", color='r')
plt.xlabel("Strain")
plt.ylabel("Plastic Strain")
plt.title("Plastic Strain vs Strain")
plt.grid(True)
plt.legend()
