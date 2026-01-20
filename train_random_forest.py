import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


# PARAMETERS
window = 100          # samples around R-peak
fs = 360              # sampling frequency (not used yet)

# Patients you want to use (adjust range if needed)
patient_ids = [str(i) for i in range(100, 234)]


# HELPER FUNCTION: find ECG lead automatically
def get_signal_column(ekg):
    possible_leads = ["MLII", "MLI", "V1", "V2", "V3", "V4", "V5", "V6"]
    for lead in possible_leads:
        if lead in ekg.columns:
            return lead
    raise ValueError("No ECG signal column found")

# FEATURE EXTRACTION
def extract_features(beat, signal_col):
    return [
        beat[signal_col].mean(),
        beat[signal_col].std(),
        beat[signal_col].max(),
        beat[signal_col].min()
    ]


# GLOBAL DATA CONTAINERS
X = []
y = []

# LOOP OVER ALL PATIENTS
for pid in patient_ids:
    print(f"Processing patient {pid}...")

    try:
        ekg = pd.read_csv(f"D:/mit-bih/{pid}_ekg.csv")
        annotation = pd.read_csv(f"D:/mit-bih/{pid}_annotations_1.csv")
    except FileNotFoundError:
        print(f"Files missing for patient {pid}, skipping.")
        continue

    # Standardize sample column
    ekg = ekg.rename(columns={"Unnamed: 0": "sample"})

    # Detect ECG signal lead automatically
    try:
        signal_col = get_signal_column(ekg)
    except ValueError as e:
        print(f"{e} for patient {pid}, skipping.")
        continue

    # Loop over beats
    for _, row in annotation.iterrows():
        r_peak = row["index"]
        label = row["annotation_symbol"]

        beat = ekg[
            (ekg["sample"] >= r_peak - window) &
            (ekg["sample"] <= r_peak + window)
        ]

        if len(beat) == 2 * window + 1:
            features = extract_features(beat, signal_col)
            X.append(features)
            y.append(0 if label == "N" else 1)

# CREATE DATAFRAME
X = pd.DataFrame(X, columns=["mean", "std", "max", "min"])
y = pd.Series(y, name="label")

print("\nFinal dataset shape:", X.shape)
print("Label distribution:")
print(y.value_counts())

# TRAIN / TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain size:", X_train.shape)
print("Test size:", X_test.shape)

# MODEL
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

model.fit(X_train, y_train)


# EVALUATION
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
