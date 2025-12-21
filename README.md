# ECG Arrhythmia Analysis

his project explores ECG (electrocardiogram) signal analysis using the
MIT-BIH Arrhythmia Database. The objective is to understand ECG signals,
segment heartbeats, extract meaningful features, and prepare data for
classifying normal versus arrhythmic heartbeats using machine learning.

---

## Project Overview

Loads ECG signals (100_ekg.csv) and heartbeat annotations (100_annotations_1.csv)

Visualizes heartbeats labeled as normal (N) or arrhythmic (A)

Segments ECG signals around annotated R-peaks

Extracts statistical features from each heartbeat:

mean: average voltage (baseline)

std: signal variability

max: R-peak amplitude

min: Q/S wave depth

Computes RR intervals (time between consecutive heartbeats) in seconds

Builds a feature matrix (X) and label vector (y) for machine-learning models

 Note:
The current implementation focuses on a single patient (record 100).
This choice is intentional and is used to validate the signal processing and feature extraction pipeline before extending the approach to multiple patients.

---

## Dataset
The MIT-BIH Arrhythmia Database is used in this project.

- Source: PhysioNet / Kaggle
- Each ECG record contains **two leads**
- One lead is often MLII, while the second lead varies by patient
  (e.g., V1, V2, V5)

In the current experiment (patient 100), the available leads are:
- **MLII**
- **V5**

### Dataset Access

The dataset is **not included** in this repository due to size.
Download it from:
https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023
**Instructions:**

1. Download the ZIP file.  
2. Extract it into a folder named `mit-bih/` in your project directory.  
3. The Python scripts will read files like `mit-bih/100_ekg.csv` and `mit-bih/100_annotations_1.csv`.

---




