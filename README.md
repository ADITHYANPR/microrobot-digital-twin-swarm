# 🧲 Human-Intent–Driven Digital Twin Control of Microrobot Swarms

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Research](https://img.shields.io/badge/Type-Research%20Simulation-purple?style=for-the-badge)
![Digital Twin](https://img.shields.io/badge/Digital-Twin-green?style=for-the-badge)
![Swarm Robotics](https://img.shields.io/badge/Swarm-Robotics-red?style=for-the-badge)
![Control](https://img.shields.io/badge/Predictive-Control-orange?style=for-the-badge)

### 🧠 Human-in-the-Loop Predictive Control Framework for Heterogeneous Magnetic Microrobot Swarms

*A research-oriented simulation platform integrating digital twins, predictive control, and intent-driven swarm robotics.*

</div>

---

# 🌌 Overview

Microrobot swarms operate in a world where classical control becomes unreliable.

At microscopic scales:

- Individual robot actuation becomes infeasible
- Fluid dynamics are highly overdamped
- Noise dominates motion behavior
- Swarms exhibit strong heterogeneity
- Precise force-level control becomes ineffective

This project introduces a **Human-Intent–Driven Digital Twin Framework** that replaces low-level force control with:

✅ High-level human goals  
✅ Adaptive digital twin prediction  
✅ Look-ahead predictive control  
✅ Swarm-level magnetic actuation  

Instead of controlling *forces*, the framework controls *intent*.

---

# 🧠 Core Architecture

```text
Human Intent (Goal)
        ↓
Intent Abstraction Layer
        ↓
Adaptive Digital Twin
        ↓
Predictive Controller
(Look-Ahead Simulation)
        ↓
Global Magnetic Actuation
        ↓
Heterogeneous Microrobot Swarm
        ↑
State Feedback
```

---

# 🚀 Key Contributions

## 🔹 Physics-Based Swarm Simulation
- Simulates magnetic microrobot swarm dynamics
- Models overdamped microscale environments
- Includes stochastic disturbances and nonlinear behavior

## 🔹 Explicit Heterogeneity Modeling
Each robot possesses unique:
- Drag coefficients
- Magnetization strengths
- Motion responses

This mimics real-world manufacturing inconsistencies in microrobotics.

## 🔹 Adaptive Digital Twin
The digital twin continuously:
- Predicts swarm evolution
- Corrects parameter mismatch online
- Reduces simulation-reality divergence

## 🔹 Human-Intent–Driven Control
Users specify:
- Desired swarm goals
- Target locations
- High-level objectives

The framework autonomously determines control actions.

## 🔹 Predictive Control Strategy
The controller:
- Simulates future swarm trajectories
- Evaluates candidate magnetic actions
- Selects the optimal actuation signal

## 🔹 Full Ablation Study
Compares:
1. No Digital Twin
2. Static Digital Twin
3. Adaptive Digital Twin

with quantitative performance evaluation.

---

# 🧬 Repository Structure

```bash
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
```

---

# ⚙️ Requirements

## 🔧 Dependencies

- Python >= 3.9
- numpy
- matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

# ▶️ Running the Project

## 🔹 Main Experiment

```bash
cd src
python -m run_experiment
```

## 🔹 Plot Results

```bash
python plot_results.py
```

## 🔹 Run Ablation Study

```bash
python -m run_ablation
```

## 🔹 Plot Ablation Results

```bash
python plot_ablation.py
```

---

# 📊 Evaluation Metrics

---

## 🎯 Metric 1: Task Error

Measures how accurately the swarm reaches the desired target.

### Swarm Center

```math
c(t) = \frac{1}{N} \sum p_i(t)
```

### Task Error

```math
E_{task}(t) = ||c(t) - g||
```

### 📌 Interpretation

- Lower value → better goal achievement
- Faster decay → faster convergence
- Non-zero steady-state error → heterogeneity + actuation limitations

---

## 🪞 Metric 2: Digital Twin Error

Measures fidelity between the real swarm and digital twin prediction.

### Twin Error

```math
E_{twin}(t) =
\frac{1}{N}
\sum ||p_i^{real}(t) - p_i^{twin}(t)||
```

### 📌 Interpretation

- Lower value → higher model fidelity
- Bounded error → stable abstraction
- Decreasing error → successful online adaptation

---

## 🧪 Metric 3: Ablation Study

### Compared Controllers

| Controller | Description |
|---|---|
| No Twin | Reactive control without prediction |
| Static Twin | Fixed-parameter digital twin |
| Adaptive Twin | Online-updating predictive twin |

### Compared Metrics

- Convergence speed
- Final task error
- Control stability

### Expected Performance

```text
Adaptive Twin > Static Twin > No Twin
```

---

# 📈 Experimental Findings

The experiments demonstrate that:

✅ Human intent enables intuitive swarm-level control  
✅ Predictive control outperforms reactive strategies  
✅ Online adaptation is critical under heterogeneity  
✅ Adaptive twins significantly reduce steady-state error  
✅ Predictive simulation improves swarm convergence speed  

The adaptive digital twin consistently achieved:

- Fastest convergence
- Lowest task error
- Highest control stability

---

# 🌟 Advantages

- 🧠 High-level human control abstraction
- 🔮 Predictive decision-making framework
- ⚡ Robust against swarm heterogeneity
- 🧩 Modular and extensible architecture
- 🧪 Research-oriented experimentation platform
- 🤖 Hardware-ready design philosophy

---

# ⚠️ Limitations

- Centralized magnetic actuation only
- Residual steady-state error persists
- Simulation-only validation
- No real hardware integration yet

---

# 🔭 Future Work

## Planned Extensions

- Real magnetic microrobot hardware integration
- 3D swarm environments
- Learning-based twin adaptation
- Vision / gesture-based intent input
- Multi-goal cooperative swarm control
- Reinforcement-learning-assisted predictive control

---

# 🎓 Intended Use

This repository is suitable for:

- Final-year engineering projects
- Research internships
- Swarm robotics coursework
- Digital twin research
- Human-robot interaction studies
- Academic GitHub portfolios
- Predictive control experimentation

---

# 📚 Research Themes

This project sits at the intersection of:

- 🧲 Microrobotics
- 🪞 Digital Twins
- 🎯 Predictive Control
- 🤝 Human-Robot Interaction
- 🧠 Intelligent Systems
- 🌊 Microscale Physics
- 🐝 Swarm Intelligence

---

# 📄 License

This project is intended for:

- Academic use
- Educational purposes
- Research experimentation

You are free to:
- Fork
- Modify
- Extend
- Build upon the framework

---

# 🙌 Acknowledgement

Developed as a research-oriented simulation framework combining:

- Magnetic microrobotics
- Adaptive digital twins
- Predictive swarm control
- Human-in-the-loop systems

Designed to explore the future of intelligent microscale collective robotics.

---

<div align="center">

## 🧲 From Human Intent → Predictive Intelligence → Swarm Behavior

*Where digital twins become the nervous system of microrobot swarms.*

</div>
