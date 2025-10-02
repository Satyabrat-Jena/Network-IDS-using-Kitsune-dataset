# 🛡️ An Explainable and Tamper-Proof DDoS Detection Model

## Using Kitsune Dataset and Ethereum Blockchain

This repository contains the implementation and analysis for an advanced, real-time **Intrusion Detection System (IDS)** designed specifically for IoT networks. [cite_start]The system leverages hybrid Deep Learning architectures for high-accuracy detection and integrates with the Ethereum blockchain for immutable forensic logging[cite: 9, 22]. [cite_start]Crucially, it employs **SHAP-based Explainable AI (XAI)** to provide transparency into the detection process, addressing the "black box" problem common in deep learning models[cite: 8, 25].

---

## ✨ Key Features

* [cite_start]**Hybrid Deep Learning IDS:** Combines **CuDNN-LSTM** and **CNN-LSTM** models to effectively capture both spatial (CNN) and temporal (LSTM) patterns in network traffic for superior real-time attack classification[cite: 6, 19, 44, 45].
* [cite_start]**High Performance:** Achieved state-of-the-art results on the challenging **Kitsune IoT Network Attack Dataset** [cite: 7, 16][cite_start], demonstrating exceptional accuracy (0.9885) across multiple attack scenarios[cite: 184, 194, 204].
* [cite_start]**Explainable AI (XAI):** Utilizes **SHAP (SHapley Additive exPlanations)** to interpret model predictions [cite: 25, 51, 171][cite_start], showing exactly which network features contributed most to an attack decision[cite: 26, 172].
* [cite_start]**Tamper-Proof Logging:** Integrates with the **Ethereum Blockchain** via a **Solidity Smart Contract** to securely log all detected intrusion events, ensuring log data integrity and auditability against tampering[cite: 9, 22, 55, 181].

---

## 💻 Technical Architecture

The system operates in three main stages:

1.  [cite_start]**Detection Module:** Network packet data from the **Kitsune dataset** [cite: 7, 70] [cite_start]is preprocessed and fed into the hybrid deep learning model (**CNN-LSTM/CuDNN-LSTM**)[cite: 6, 155].
2.  [cite_start]**Interpretation Module (XAI):** Upon a successful attack detection, the **SHAP** algorithm generates an explanation detailing the feature contributions for that specific prediction[cite: 8, 244].
3.  [cite_start]**Logging Module (Blockchain):** The attack metadata (e.g., timestamp, source/destination IP) is recorded onto an Ethereum network (tested with **Ganache**) using **Web3.py** and a **Solidity** smart contract[cite: 22, 181, 323].

### Model Performance Snapshot (CNN-LSTM)

| Metric | Value |
| :--- | :--- |
| **Accuracy** | [cite_start]0.9885 [cite: 204] |
| **ROC-AUC** | [cite_start]0.9837 [cite: 204] |
| **F1-Score** | [cite_start]0.9731 [cite: 204] |

### Key XAI Insights

[cite_start]SHAP analysis highlighted features like **Feature 18 Timestep 9**, **Feature 35 Timestep 9**, and **Feature 45 Timestep 9** as having the most effect on the model's outputs, strongly correlating with attack behavior[cite: 246].

---

## 🛣️ Future Work

* [cite_start]**Federated Learning:** Future extensions could focus on applying **federated learning** for privacy-preserving detection across distributed systems[cite: 346, 367].
* [cite_start]**Cost Optimization:** Research on private blockchains is suggested for reducing transaction overhead and delays associated with blockchain integration[cite: 340, 364].
* [cite_start]**Enhanced Interpretability:** Widespread application of other XAI techniques such as **LIME** or attention mechanisms could further raise the level of interpretability[cite: 340].

---

## 👨‍💻 Authors

* [cite_start]**Manjit Kumar Nayak** [cite: 2]
* [cite_start]**Debasis Gountia** [cite: 2]
* [cite_start]**Satyabrat Jena** [cite: 2]
