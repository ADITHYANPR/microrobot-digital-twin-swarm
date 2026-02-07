# 🧲 Human-Intent–Driven Digital Twin Control of Microrobot Swarms

```text
PROJECT TYPE:
- Research-grade
- Simulation-based
- Human-in-the-loop
- Digital Twin + Predictive Control

DOMAIN:
- Magnetic Microrobot Swarms

MOTIVATION:
- Individual microrobot actuation is impossible
- Robots are heterogeneous
- Microscale dynamics are noisy and overdamped
- Low-level force control is ineffective


SOLUTION:
- Replace force-level control with human intent
- Use adaptive digital twin for prediction
- Select actions via predictive control
CORE ARCHITECTURE:


Human Intent (Goal)
      ↓
Intent Abstraction Layer
      ↓
Adaptive Digital Twin
      ↓
Predictive Controller (Look-Ahead Simulation)
      ↓
Global Magnetic Actuation
      ↓
Heterogeneous Microrobot Swarm
      ↑
State Feedback
KEY CONTRIBUTIONS:
- Physics-based microrobot swarm simulation
- Explicit modeling of heterogeneity (drag, magnetization)
- Adaptive digital twin with online parameter correction
- Human-intent–driven swarm control
- Twin-predictive control strategy
- Quantitative evaluation
- Full ablation study
REPOSITORY STRUCTURE:


microrobot-digital-twin-swarm/
│
├── src/
│   ├── control/              # Predictive & baseline controllers
│   ├── intent/               # Human intent abstraction
│   ├── models/               # Microrobot models
│   ├── simulation/           # Swarm physics, digital twin, metrics
│   │
│   ├── run_experiment.py     # Main experiment
│   ├── run_ablation.py       # Ablation study
│   ├── plot_results.py       # Task & twin error plots
│   └── plot_ablation.py      # Ablation comparison
│
├── README.md
└── .gitignore

# REQUIREMENTS:
- Python >= 3.9
- numpy
- matplotlib
pip install numpy matplotlib

# HOW TO RUN:
cd src
python -m run_experiment
python plot_results.py
python -m run_ablation
python plot_ablation.py
EVALUATION METRICS:

# METRIC 1: TASK ERROR
Given:
- N robots
- p_i(t): position of robot i at time t
- g: target position


Swarm center:
c(t) = (1/N) * Σ p_i(t)


Task Error:
E_task(t) = || c(t) - g ||

# INTERPRETATION:
- Lower value = better goal achievement
- Faster decay = faster convergence
- Non-zero steady-state = heterogeneity + actuation limits
METRIC 2: DIGITAL TWIN ERROR
Given:
- p_i_real(t): real robot position
- p_i_twin(t): digital twin position


# Twin Error:
E_twin(t) = (1/N) * Σ || p_i_real(t) - p_i_twin(t) ||

# INTERPRETATION:
- Lower value = higher model fidelity
- Bounded error = stable abstraction
- Reduction over time = successful adaptation
METRIC 3: ABLATION STUDY


# COMPARED CONTROLLERS:
1. No Digital Twin
2. Static Digital Twin
3. Adaptive Digital Twin

# COMPARED METRICS:
- Convergence speed
- Final task error
- Stability of control

# EXPECTED PERFORMANCE ORDER:
Adaptive Twin > Static Twin > No Twin
EXPERIMENTAL FINDINGS:
- Human intent enables intuitive swarm-level control
- Predictive control outperforms reactive control
- Online adaptation is essential for heterogeneity
- Adaptive digital twin achieves:
  - Fastest convergence
  - Lowest steady-state error

# ADVANTAGES:
- High-level human control (no force tuning)
- Predictive decision making
- Robust to robot heterogeneity
- Modular and extensible architecture
- Hardware-ready design

# LIMITATIONS:
- Centralized magnetic actuation
- Residual steady-state error
- Simulation-only validation

# FUTURE WORK:
- Real magnetic microrobot hardware integration
- 3D swarm environments
- Learning-based digital twin adaptation
- Vision / gesture-based intent input
- Multi-goal swarm control

# INTENDED USE:
- Final-year engineering projects
- Research internships
- Digital twin coursework
- Swarm robotics & HRI studies
- Academic GitHub portfolios

# LICENSE:
- Academic and educational use
- Free to fork, modify, and extend

# ACKNOWLEDGEMENT:
- Developed as a research-oriented project
- Combines microrobotics, digital twins,
  predictive control, and human-in-the-loop systems
