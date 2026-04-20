# 🧠 Daily Reflection Tree (Deterministic Decision System)

This project implements a **deterministic decision tree-based reflection system** designed to guide users through structured self-analysis of their day.

---

## 🚀 Overview

The system simulates a guided reflection process using a **fixed set of questions and predefined paths**, ensuring:

* Consistent outputs
* Logical flow
* No ambiguity
* No runtime AI dependency

Each user response leads to a **deterministic next step**, forming a structured reflection journey.

---

## 🎯 Objective

The goal of this system is to:

* Improve self-awareness
* Encourage structured thinking
* Analyze behavior through key psychological dimensions

---

## 🧩 Core Design (3 Axes)

The reflection tree is built on three key dimensions:

### 1️⃣ Locus of Control

* Internal vs External control
* Did the user take responsibility or blame external factors?

---

### 2️⃣ Contribution vs Entitlement

* What did the user contribute?
* Did they expect something in return?

---

### 3️⃣ Perspective / Radius

* Focus on self vs others
* Impact on team, colleagues, or customers

---

## ⚙️ How It Works

1. System starts with a greeting
2. Asks structured questions
3. User selects predefined options
4. Based on input → next node is selected
5. Reflection messages are shown
6. Ends with a summary

👉 Same input → same output (Deterministic System)

---

## 📁 Project Structure

```
assignment/
│
├── reflection-tree.json   # Decision tree structure
├── agent.py               # Python CLI agent
├── write-up.md            # Design explanation
├── README.md              # Project documentation
```

---

## 🧪 Running the Project

### Requirements:

* Python installed

### Run:

```
python agent.py
```

---

## 🧠 Example Flow

```
Start → Q1 → Q2 → Reflection → Contribution → Perspective → Summary → End
```

---

## ✨ Key Features

* Deterministic decision system
* Structured question flow
* Clear separation of logic and data
* No AI hallucination (controlled flow)
* Simple CLI-based interaction

---

## ⚠️ Design Constraints

* No free-text input
* Only predefined options
* No runtime AI usage
* Fixed transitions between nodes

---

## 🔮 Future Improvements

* Deeper branching logic
* Personalized reflection summaries
* Web-based UI
* Data tracking and analytics

---

## 👨‍💻 Author

Abhishek Yadav

---

## 📌 Note

This project was created as part of a **role-simulation assignment**, focusing on problem-solving, structured thinking, and system design rather than complex implementation.

---
