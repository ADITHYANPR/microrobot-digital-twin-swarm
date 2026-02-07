import numpy as np

from simulation.swarm import Swarm
from simulation.digital_twin import DigitalTwin
from control.predictive_controller import PredictiveController
from simulation.metrics import swarm_center_error, twin_error

num_robots = 10
dt = 0.1
steps = 200
target = np.array([5.0, 5.0])

real_swarm = Swarm(num_robots)
twin = DigitalTwin(num_robots)
controller = PredictiveController()

task_errors = []
twin_errors = []

for _ in range(steps):
    force = controller.select_force(twin, target, dt)

    real_swarm.step(force, dt)
    twin.step(force, dt)
    twin.adapt(real_swarm.get_positions())

    real_pos = real_swarm.get_positions()
    twin_pos = twin.get_positions()

    task_errors.append(
        swarm_center_error(real_pos, target)
    )

    twin_errors.append(
        twin_error(real_pos, twin_pos)
    )

np.save("task_error.npy", np.array(task_errors))
np.save("twin_error.npy", np.array(twin_errors))

print("Experiment finished. Data saved.")