import joblib
import pandas as pd
from pathlib import Path
from features import extract_features

# Load the trained model
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
model = joblib.load(MODEL_PATH)

# The 15 features used in our project
FEATURE_NAMES = [
    "url_length",
    "host_length",
    "num_dots",
    "num_hyphens",
    "num_digits",
    "num_special",
    "has_at",
    "has_ip",
    "is_shortener",
    "double_slash_in_path",
    "num_subdomains",
    "path_depth",
    "is_https",
    "keyword_count",
    "host_entropy"
]


def predict_url(url):

    # Check URL input
    if not isinstance(url, str) or not url.strip():
        raise ValueError("Please enter a valid URL.")

    url = url.strip()

    # Extract URL features
    extracted = extract_features(url)

    # Prepare features in the same order as training
    if isinstance(extracted, dict):
        row = extracted
    elif hasattr(extracted, "to_dict"):
        row = extracted.to_dict()
    else:
        row = dict(zip(FEATURE_NAMES, extracted))

    # Use training feature names if available
    columns = list(
        getattr(model, "feature_names_in_", FEATURE_NAMES)
    )

    missing = [name for name in columns if name not in row]

    if missing:
        raise ValueError(
            f"Missing features: {missing}. "
            "Check features.py and train.py."
        )

    data = pd.DataFrame(
        [[row[name] for name in columns]],
        columns=columns
    )

    # Predict URL category
    prediction = model.predict(data)[0]

    if prediction in (1, "1", "phishing", "Phishing"):
        result = "Phishing"
    elif prediction in (0, "0", "legitimate", "Legitimate"):
        result = "Legitimate"
    else:
        result = str(prediction)

    # Calculate phishing probability
    phishing_probability = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(data)[0]
        classes = list(model.classes_)

        phishing_indices = [
            i for i, label in enumerate(classes)
            if str(label).lower() in ("1", "phishing")
        ]

        if phishing_indices:
            phishing_probability = float(
                probabilities[phishing_indices[0]]
            )

    return result, phishing_probability


# Run the program directly
if __name__ == "__main__":

    url = input("Enter website URL: ")

    try:
        result, probability = predict_url(url)

        print("\n----- PHISHING DETECTION RESULT -----")
        print("URL:", url)
        print("Prediction:", result)

        if probability is not None:
            print(
                "Phishing probability:",
                f"{probability * 100:.2f}%"
            )

        print("------------------------------------")

    except Exception as error:
        print("Error:", error)
        