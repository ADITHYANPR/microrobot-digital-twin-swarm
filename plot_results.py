import numpy as np
import matplotlib.pyplot as plt

task_error = np.load("task_error.npy")
twin_error = np.load("twin_error.npy")

plt.figure()
plt.plot(task_error)
plt.xlabel("Time step")
plt.ylabel("Distance to target")
plt.title("Task Error Over Time")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(twin_error)
plt.xlabel("Time step")
plt.ylabel("Mean Twin Error")
plt.title("Digital Twin Error Over Time")
plt.grid(True)
plt.show()