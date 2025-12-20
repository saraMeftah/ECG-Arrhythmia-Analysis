# ECG Arrhythmia Analysis

This project analyzes ECG data from the MIT-BIH Arrhythmia Database to visualize heartbeats, extract features, and prepare data for classification of normal vs arrhythmic heartbeats.

---

## Project Overview

- Loads ECG signals (`100_ekg.csv`) and heartbeat annotations (`100_annotations_1.csv`).  
- Visualizes multiple heartbeats, comparing normal (N) vs arrhythmic (A) beats.  
- Extracts key features from each heartbeat:  
  - **mean**: average voltage (baseline)  
  - **std**: standard deviation (irregularity)  
  - **max**: R-peak height  
  - **min**: Q/S wave depth  
- Calculates **RR intervals** (time between consecutive R-peaks) in seconds.  
- Prepares a dataset (`X` and `y`) for ML-based heartbeat classification.

---

## Dataset

The dataset is **not included directly** due to size. Download it from:

[MIT-BIH Arrhythmia Dataset (Google Storage)](https://storage.googleapis.com/kaggle-data-sets/3504103/12526755/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20251218%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251218T223129Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8c5ead519b4f979ba69bc7f829b037582a82befb6be7f5a3b351cbdce6ce178a1d84b35c1ee250c6857fe4767cb945b0d06494ca05d0e1b038d43030f22e955342314235da2123bf15a2a566532063fe4e330aad0a4be176297924da01903a4002b66122652ca0fbf26d1d8078620a5d3864ab842e76454d596542fb2f0b0794c0d63946700d27ac32854713875c658e54c286cd2722361e0052d2ddcabeb7b0591fd4cac2104e5fa25829cebb100fd3d06b4cd4d885c9062c4112cea8fea478df76abf3a1f1dce979fe67d63877f468c60aff3e364f712340c796f67cdd740e00a1888f1794eb78219d4abaeb580e07d57d2f2e1e5f5965420d8abe4955f31e)

**Instructions:**

1. Download the ZIP file.  
2. Extract it into a folder named `mit-bih/` in your project directory.  
3. The Python scripts will read files like `mit-bih/100_ekg.csv` and `mit-bih/100_annotations_1.csv`.

---

## Usage

1. Install dependencies:

```bash
pip install pandas matplotlib

---
##  Run script
python understanding_data.py


