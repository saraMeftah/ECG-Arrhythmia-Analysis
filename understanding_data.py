import pandas as pd
import matplotlib.pyplot as plt
import math

# load ECG signal
ekg = pd.read_csv("D:/mit-bih/100_ekg.csv")


print(ekg.columns)
print(ekg.head())

annotation = pd.read_csv("D:/mit-bih/100_annotations_1.csv")

print(annotation.head())
r_peak_N1 = 1515
r_peak_A = 2044
r_peak_N = 1809
r_peak_N2 = 2402

window = 100  # samples before and after
ekg = ekg.rename(columns={"Unnamed: 0": "sample"})
ekg = ekg.rename(columns={"MLII": "ML2"})
beat = ekg[
    (ekg["sample"] >= r_peak_N - window) &
    (ekg["sample"] <= r_peak_N + window)
]
beat_N1=  ekg[
    (ekg["sample"] >= r_peak_N1 - window) &
    (ekg["sample"] <= r_peak_N1 + window)
]
beat_A = ekg[
    (ekg["sample"] >= r_peak_A - window) &
    (ekg["sample"] <= r_peak_A + window)
]
beat_N =  ekg[
    (ekg["sample"] >= r_peak_N - window) &
    (ekg["sample"] <= r_peak_N + window)
]
beat_N2 =  ekg[
    (ekg["sample"] >= r_peak_N2 - window) &
    (ekg["sample"] <= r_peak_N2 + window)
]

#print(beat)
plt.figure()
plt.plot(beat_N1["ML2"], label = "Normal (N)")
plt.plot(beat_A["ML2"], label = "Arrhythmia (A)")
plt.plot(beat_N["ML2"], label = "Normal (N)")
plt.plot(beat_N2["ML2"], label = "Normal (N)")
plt.legend()
plt.title("Normal vs Arrythmia heartbeat")
plt.show()

def extract_features(beat):
    return {
        "mean": beat["ML2"].mean(),
        "std": beat["ML2"].std(),
        "max": beat["ML2"].max(),
        "min": beat["ML2"].min()
    }
print(extract_features(beat))

rr = annotation["index"].diff() / 360  
annotation["RR_sec"] = rr

print(annotation.head())








