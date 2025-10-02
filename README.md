🛡️ An Explainable and Tamper-Proof DDoS Detection Model
Using Kitsune Dataset and Ethereum Blockchain
This repository contains the implementation and analysis for an advanced, real-time Intrusion Detection System (IDS) designed specifically for IoT networks. The system leverages hybrid Deep Learning architectures for high-accuracy detection and integrates with the Ethereum blockchain for immutable forensic logging. Crucially, it employs SHAP-based Explainable AI (XAI) to provide transparency into the detection process, addressing the "black box" problem common in deep learning models.

✨ Key Features
Hybrid Deep Learning IDS: Combines CuDNN-LSTM and CNN-LSTM models to effectively capture both spatial (CNN) and temporal (LSTM) patterns in network traffic for superior real-time attack classification.

High Performance: Achieved state-of-the-art results on the challenging Kitsune IoT Network Attack Dataset, demonstrating exceptional accuracy across multiple attack scenarios (Mirai, SYN Flood, ARP MitM, etc.).

Explainable AI (XAI): Utilizes SHAP (SHapley Additive exPlanations) to interpret model predictions, showing exactly which network features (e.g., packet size, flow metrics) contributed most to an attack decision.

Tamper-Proof Logging: Integrates with the Ethereum Blockchain via a Solidity Smart Contract to securely log all detected intrusion events (timestamp, source/destination IP, attack type), ensuring log data integrity and auditability against tampering.

Real-Time Capability: Optimized for speed using GPU-accelerated CuDNN layers for deployment in dynamic network configurations.

💻 Technical Architecture
The system operates in three main stages:

Detection Module: Network packet data from the Kitsune dataset is preprocessed and fed into the hybrid deep learning model (CNN-LSTM/CuDNN-LSTM).

Interpretation Module (XAI): Upon a successful attack detection, the SHAP algorithm generates an explanation detailing the feature contributions for that specific prediction.

Logging Module (Blockchain): The attack metadata and key forensic details are recorded onto an Ethereum private blockchain (e.g., Ganache) using Web3.py and a Solidity smart contract.

Model Performance Snapshot (CNN-LSTM)
Metric

Value

Accuracy

98.85%

ROC-AUC

0.9837

F1-Score

0.9731

(Performance metrics based on multi-class classification on the Kitsune dataset.)

🛠️ Technologies & Dependencies
The project relies on the following major technologies:

Category

Technology

Purpose

Deep Learning

Python, TensorFlow/Keras

Model training and inference (CNN-LSTM, CuDNN-LSTM)

Data Science

NumPy, Pandas, Scikit-Learn

Data preprocessing, feature engineering, and model evaluation

Explainability

SHAP

Generating feature contribution explanations (XAI)

Blockchain

Solidity, Web3.py, Ganache

Smart contract development and integration for immutable logging

Data Source

Kitsune Dataset

Real-world IoT network traffic and attack data

🚀 Setup and Installation (Conceptual)
To set up this project, you would typically follow these steps:

Clone the Repository:

git clone [https://github.com/your-username/repo-name.git](https://github.com/your-username/repo-name.git)
cd repo-name


Environment Setup (Python):

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt 


Blockchain Setup:

Set up a local Ethereum development environment (e.g., using Ganache CLI or Desktop).

Compile and deploy the IntrusionLog.sol smart contract, noting the contract address and ABI.

Dataset Preparation:

Download and process the Kitsune dataset.

Run the provided feature extraction and preprocessing scripts.

👨‍💻 Authors
Satyabrat Jena
