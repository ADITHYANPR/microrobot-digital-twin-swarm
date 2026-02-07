\# Human-Intent–Driven Digital Twin Control of Magnetic Microrobot Swarms



This repository contains a full software implementation of a

human-in-the-loop, digital-twin–based control framework for

heterogeneous magnetic microrobot swarms.



\## Features

\- Physics-based microrobot swarm simulation

\- Heterogeneous robot dynamics

\- Adaptive digital twin

\- Human intent abstraction

\- Twin-predictive control

\- Quantitative experiments and ablation study



\## Project Structure



microrobot\_swarm/

├── src/

│ ├── control/

│ ├── intent/

│ ├── models/

│ ├── simulation/

│ ├── run\_experiment.py

│ ├── run\_ablation.py

│ ├── plot\_results.py

│ ├── plot\_ablation.py





\## How to Run



```bash

cd src

python -m run\_experiment

python plot\_results.py

python -m run\_ablation

python plot\_ablation.py

