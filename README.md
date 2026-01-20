# ECG Arrhythmia Analysis

This project explores ECG (electrocardiogram) signal analysis using the
MIT-BIH Arrhythmia Database. The objective is to understand ECG signals,
segment heartbeats, extract meaningful features, and classify normal
versus arrhythmic heartbeats using machine learning.

---

## Project Structure

- `understanding_data.py`  
  Used to visualize ECG signals, inspect heartbeats, and understand
  the effect of arrhythmia on ECG morphology.

- `build_dataset.py`  
  Builds a baseline machine learning dataset and model using a
  single patient (record 100). This step validates segmentation and
  feature extraction.

- `train_random_forest.py`  
  Final model that processes multiple patients, automatically handles
  heterogeneous ECG leads, and performs Random Forest classification.

---

## Dataset

The MIT-BIH Arrhythmia Database is used in this project.

- Source: PhysioNet / Kaggle
- Each ECG record contains **two leads**
- One lead is often **MLII**, while the second lead varies by patient
  (e.g., V1, V2, V5)

---

## Results

Using a Random Forest classifier on multiple patients:

- **Accuracy:** 93%
- **F1-score (Arrhythmic class):** 0.90
- **Recall (Arrhythmic class):** 87%

These results show that increasing data diversity across patients
significantly improves classification performance.

---

## Dataset Access

The dataset is **not included** in this repository due to its size.

Download it from:  
https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023

**Instructions:**

1. Download the ZIP file  
2. Extract it into a folder named `mit-bih/` in your project directory  
3. The Python scripts will read files such as:
   - `mit-bih/100_ekg.csv`
   - `mit-bih/100_annotations_1.csv`

---

## Conclusion

This project demonstrates that careful ECG preprocessing and data
diversity can be more important than complex models for arrhythmia
detection.
