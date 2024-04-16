import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 5, 1000)

# Define the response function y(t)
y = np.exp(-t) + 17 * t * np.exp(-t)

# Plot the response
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='y(t)')
plt.xlabel('Time (t)')
plt.ylabel('Response y(t)')
plt.title('Response of the System')
plt.legend()
plt.grid(True)
plt.show()
