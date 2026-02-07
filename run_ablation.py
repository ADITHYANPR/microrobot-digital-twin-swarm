import numpy as np

from simulation.swarm import Swarm
from simulation.digital_twin import DigitalTwin
from control.predictive_controller import PredictiveController
from simulation.metrics import swarm_center_error

num_robots = 10
dt = 0.1
steps = 200
target = np.array([5.0, 5.0])

def run_case(case_type):
    real_swarm = Swarm(num_robots)
    controller = PredictiveController()

    if case_type == "no_twin":
        twin = None
    else:
        twin = DigitalTwin(num_robots)

    errors = []

    for _ in range(steps):
        if case_type == "no_twin":
            center = real_swarm.get_positions().mean(axis=0)
            direction = target - center
            norm = np.linalg.norm(direction)
            force = direction / norm if norm != 0 else np.zeros(2)
        else:
            force = controller.select_force(twin, target, dt)
            twin.step(force, dt)

            if case_type == "adaptive_twin":
                twin.adapt(real_swarm.get_positions())

        real_swarm.step(force, dt)

        error = swarm_center_error(real_swarm.get_positions(), target)
        errors.append(error)

    return np.array(errors)

np.save("ablation_no_twin.npy", run_case("no_twin"))
np.save("ablation_static_twin.npy", run_case("static_twin"))
np.save("ablation_adaptive_twin.npy", run_case("adaptive_twin"))

print("Ablation experiment completed.")