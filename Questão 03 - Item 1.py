import numpy as np
import matplotlib.pyplot as plt

# Define the characteristic polynomial (s + 1)^2
def characteristic_polynomial(s):
    return (s + 1)**2

# Generate a range of s values
s_values = np.linspace(-5, 5, 1000)

# Calculate the magnitude of the characteristic polynomial for each s value
magnitude = np.abs(characteristic_polynomial(s_values))

# Plot the system mode
plt.figure(figsize=(8, 6))
plt.plot(s_values, magnitude, label='Magnitude of (s + 1)^2')
plt.axvline(x=-1, color='red', linestyle='--', label='System Mode at s = -1')
plt.xlabel('s')
plt.ylabel('Magnitude')
plt.title('System Mode Plot')
plt.legend()
plt.grid(True)
plt.show()