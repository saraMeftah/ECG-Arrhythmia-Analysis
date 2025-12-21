import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

ekg = pd.read_csv("D:/mit-bih/100_ekg.csv")
annotation = pd.read_csv("D:/mit-bih/100_annotations_1.csv")


ekg = ekg.rename(columns={
    "Unnamed: 0": "sample",
    "MLII": "ML2"
})


window = 100        
fs = 360           


def extract_features(beat):
    return {
        "mean": beat["ML2"].mean(),
        "std": beat["ML2"].std(),
        "max": beat["ML2"].max(),
        "min": beat["ML2"].min()
    }


X = []
y = []

for _, row in annotation.iterrows():
    r_peak = row["index"]
    label = row["annotation_symbol"]

    beat = ekg[
        (ekg["sample"] >= r_peak - window) &
        (ekg["sample"] <= r_peak + window)
    ]

    
    if len(beat) == 2 * window + 1:
        features = extract_features(beat)
        X.append(list(features.values()))
        y.append(0 if label == "N" else 1)


X = pd.DataFrame(X, columns=["mean", "std", "max", "min"])
y = pd.Series(y, name="label")

print("X shape:", X.shape)
print("y shape:", y.shape)
print("\nLabel distribution:")
print(y.value_counts())

print("\nFirst 5 feature rows:")
print(X.head())
#print(y.head())


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced" 
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report:")
print(classification_report(y_test, y_pred))
