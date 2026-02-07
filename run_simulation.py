import numpy as np
import matplotlib.pyplot as plt

from simulation.swarm import Swarm
from simulation.digital_twin import DigitalTwin
from intent.intent_handler import IntentHandler
from control.controller import Controller

num_robots = 10
dt = 0.1
steps = 300

real_swarm = Swarm(num_robots)
twin = DigitalTwin(num_robots)
intent = IntentHandler()
controller = Controller()

def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        intent.set_target(event.xdata, event.ydata)

fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', on_click)

for _ in range(steps):
    if intent.has_target():
        target = intent.get_target()
        force = controller.compute_force(
            real_swarm.get_positions(),
            target
        )
    else:
        force = np.zeros(2)

    real_swarm.step(force, dt)
    twin.step(force, dt)
    twin.adapt(real_swarm.get_positions())

    plt.cla()
    rp = real_swarm.get_positions()
    tp = twin.get_positions()

    plt.scatter(rp[:, 0], rp[:, 1], label="Real")
    plt.scatter(tp[:, 0], tp[:, 1], marker='x', label="Twin")

    if intent.has_target():
        plt.scatter(target[0], target[1], c='red', marker='*', s=150)

    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.pause(0.05)

plt.show()