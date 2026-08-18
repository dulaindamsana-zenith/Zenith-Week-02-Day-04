# Zenith-Week-02-Day-04
# 🛡️ Project Zenith v4.0 | Day 004: Linux File System & Permission Validator

> **Operator**: Dula (Dulain Damsana)  
> **Target**: Quantum Cyber Physics Foundation — Year 1 / Month 1 / Week 1  
> **Environment**: Linux Mint XFCE (LTS) — 100% Terminal Native CLI  

---

## 📌 Operational Objective
Automated Bash verification engine designed to programmatically construct nested directory hierarchies, audit octal file permissions (`chmod 755 / 644`), write directory tree logs, and enforce strict execution boundaries inside the Linux Mint XFCE shell environment.

---

## ⚙️ Technical Specifications & Environment
- **Operating System**: Linux Mint XFCE (LTS) 🐧
- **Shell Interface**: GNU Bash v5+ 🐚
- **Execution Engine**: Terminal-First Sandbox Container (Strict 120-Minute Isolation) ⏱️
- **Core Commands Utilized**: `mkdir`, `chmod`, `ls`, `tree`, `cat`, `tee`, `chmod`, `stat`

---

## 🚀 Script Features & Execution Logic
1. **Automated Directory Setup**: Recursively builds system workspace folders (`bin/`, `logs/`, `config/`, `backup/`).
2. **Permission Boundary Audit**: Enforces strict security flags (`700` for private scripts, `644` for log assets, `755` for execution binaries).
3. **Directory Tree Logging**: Extracts detailed directory structures using `tree` and `ls -la` pipelines, outputting real-time reports to `/logs/system_audit.log`.
4. **Execution Integrity Verification**: Validates file ownership and status before writing final operational metrics.

---

## 📂 Repository Structure
```text
day-004-zenith_roadmap/
├── README.md
├── .gitignore
└── LICENSE
└── zenith_leger.log
└── Day_Project.py
└── lucid.py
└── task_1.py
└── task_2.py
└── task_3.py
└── task_4.py
└── task_5.py
└── v_or_m.py
