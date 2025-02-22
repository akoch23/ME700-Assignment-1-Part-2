NOTE: PLEASE USE/PASTE ONLY THE CODE FOR A SINGULAR EXAMPLE AT A TIME, DO NOT ATTEMPT TO RUN THE ENTIRE FILE.
----------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 1: Lecture #6 Isotropic Hardening Example

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 10
H = E*E_t/(E-E_t)

Hardening_Isotropic = Isotropic(E=E, H=H, Y_0 = Y_0)

stress_values = Hardening_Isotropic.hardening_model(strain_change = total_strain)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_values, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

---------------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 2: Lecture #6 Kinematic Hardening Example

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 10
H = E*E_t/(E-E_t)

Hardening_Kinematic = Kinematic(E=E, H=H, Y_0 = Y_0)

Stress_values = Hardening_Kinematic.run_model(strain_change = total_strain)


fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_list, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

-----------------------------------------------------------------------------------------------------------------------------

# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 3: Lecture #6 Isotropic Hardening Example (Lower Yield Stress)

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 5
H = E*E_t/(E-E_t)

Hardening_Isotropic = Isotropic(E=E, H=H, Y_0 = Y_0)

stress_values = Hardening_Isotropic.hardening_model(strain_change = total_strain)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_values, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

-----------------------------------------------------------------------------------------------------------------------------

# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 4: Lecture #6 Isotropic Hardening Example (Higher Yield Stress)

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 150
H = E*E_t/(E-E_t)

Hardening_Isotropic = Isotropic(E=E, H=H, Y_0 = Y_0)

stress_values = Hardening_Isotropic.hardening_model(strain_change = total_strain)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_values, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

-----------------------------------------------------------------------------------------------------------------------------

# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 5: Lecture #6 Isotropic Hardening Example (Lower Yield Stress)

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 5
H = E*E_t/(E-E_t)

Hardening_Isotropic = Isotropic(E=E, H=H, Y_0 = Y_0)

stress_values = Hardening_Isotropic.hardening_model(strain_change = total_strain)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_values, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

-----------------------------------------------------------------------------------------------------------------------------

# Import necessary pacakges
import numpy as np
from hardening_model import Isotropic
import matplotlib.pyplot as plt

# Example 6: Lecture #6 Isotropic Hardening Example (Higher Yield Stress)

# Define functions and user inputs
strain_set_1 = np.linspace(0,0.05,1000)
strain_set_2 = np.linspace(0.05,-0.05,2000)
strain_set_3 = np.linspace(-0.05,0.075,2500)
strain_set_4 = np.linspace(0.075,-0.025,2000)
total_strain = np.concatenate((strain_set_1,strain_set_2,strain_set_3,strain_set_4),axis=0)

# Material Properties: E = Elastic Modulus, E_t = Tangent Modulus, Y_0 = Initial Stress, H = Plastic Modulus
E = 1000
E_t = 100
Y_0 = 150
H = E*E_t/(E-E_t)

Hardening_Isotropic = Isotropic(E=E, H=H, Y_0 = Y_0)

stress_values = Hardening_Isotropic.hardening_model(strain_change = total_strain)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(total_strain, stress_values, label='Stress-Strain Curve', color='b', linewidth=2)
ax.set_xlabel('Strain', fontsize=12)
ax.set_ylabel('Stress', fontsize=12)
ax.set_title('Stress vs. Strain', fontsize=14)
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

---------------------------------------------------------------------------------------------------------------------------
