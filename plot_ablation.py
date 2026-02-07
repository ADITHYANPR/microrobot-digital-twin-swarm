import numpy as np
import matplotlib.pyplot as plt

no_twin = np.load("ablation_no_twin.npy")
static_twin = np.load("ablation_static_twin.npy")
adaptive_twin = np.load("ablation_adaptive_twin.npy")

plt.figure()
plt.plot(no_twin, label="No Digital Twin", linewidth=2)
plt.plot(static_twin, label="Static Digital Twin", linewidth=2)
plt.plot(adaptive_twin, label="Adaptive Digital Twin", linewidth=2)

plt.xlabel("Time step")
plt.ylabel("Distance to target")
plt.title("Ablation Study: Impact of Digital Twin")
plt.legend()
plt.grid(True)
plt.show()