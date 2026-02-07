# Human-Intent–Driven Digital Twin Control of Magnetic Microrobot Swarms

This repository presents a **fully software-based control framework** for
**heterogeneous magnetic microrobot swarms**, driven by **human intent** and
enhanced through an **adaptive digital twin**.

The project integrates physics-based swarm simulation, online digital-twin
adaptation, and twin-predictive control, and is validated through
quantitative experiments and an ablation study.

This work is designed to be **research-oriented, modular, and extensible**,
while remaining entirely simulation-based.

---

## ✨ Key Contributions

- Physics-based microrobot swarm simulation (overdamped microscale dynamics)
- Modeling of **heterogeneous microrobots** (variable drag and magnetic response)
- **Adaptive digital twin** with online parameter correction
- **Human-intent abstraction** (goal-level control instead of low-level forces)
- **Twin-predictive control** using forward simulation
- Quantitative performance evaluation
- Ablation study:
  - No digital twin
  - Static digital twin
  - Adaptive digital twin (proposed method)

---

## 🧠 System Overview

The framework follows a closed-loop architecture:

Human Intent
↓
Intent Abstraction Layer
↓
Digital Twin (Predictive + Adaptive)
↓
Global Magnetic Control
↓
Heterogeneous Microrobot Swarm
↑
State Feedback



Unlike conventional simulators, the **digital twin actively participates in
control decisions**, predicting future swarm behavior before actions are applied.


---


## 📁 Project Structure



microrobot-digital-twin-swarm/
│
├── src/
│ ├── control/ # Predictive and baseline controllers
│ ├── intent/ # Human intent abstraction
│ ├── models/ # Microrobot models
│ ├── simulation/ # Swarm physics, digital twin, metrics
│ │
│ ├── run_experiment.py # Main experiment runner
│ ├── run_ablation.py # Ablation study runner
│ ├── plot_results.py # Task & twin error plots
│ └── plot_ablation.py # Ablation comparison plot
│
├── README.md
└── .gitignore



---


## ⚙️ Requirements


- Python **3.9 or higher**
- NumPy
- Matplotlib


Install dependencies:
```bash
pip install numpy matplotlib
▶️ How to Run
1️⃣ Run the main experiment
cd src
python -m run_experiment
2️⃣ Plot task error and digital twin error
python plot_results.py
3️⃣ Run the ablation study
python -m run_ablation
4️⃣ Plot ablation comparison
python plot_ablation.py
📊 Evaluation Metrics

Task Error
Euclidean distance between the swarm center and the target

Digital Twin Error
Mean position mismatch between the real swarm and the digital twin

Ablation Performance
Comparison across:

No digital twin

Static digital twin

Adaptive digital twin

📌 Key Findings

Human-intent abstraction enables intuitive, high-level swarm control

Digital twins improve control performance when used predictively

Online adaptation is essential for handling swarm heterogeneity

Adaptive twin-based control consistently outperforms baseline methods

🚧 Limitations

Centralized magnetic actuation limits individual robot control

Residual steady-state error exists due to heterogeneity

Entirely simulation-based (no physical hardware validation)

These are explicit design choices, not implementation shortcomings.

🔮 Future Extensions

Integration with real magnetic microrobot platforms

3D swarm simulation

Learning-based digital twin adaptation

Vision- or gesture-based intent input

Multi-objective task specification

🎓 Academic Use

Suitable for:

Final-year undergraduate projects

Research prototypes

Digital twin and swarm robotics coursework

Human–robot interaction studies

📜 License

Released for academic and educational use.
You are free to fork, extend, and cite this work.

✨ Acknowledgement

This project was developed as a step-by-step, research-oriented implementation
combining concepts from microrobotics, digital twins, control systems,
and human-in-the-loop robotics.
