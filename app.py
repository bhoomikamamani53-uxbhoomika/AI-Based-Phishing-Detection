
import streamlit as st
import joblib
from features import extract_features
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# Page settings
st.set_page_config(
    page_title="AI Phishing Detection System",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 AI-Based Phishing Detection System")
st.write("Check whether a website URL is Legitimate or Phishing.")

# URL input
url = st.text_input("Enter Website URL:")

if st.button("Check URL"):
    if url.strip():
        try:
            # Extract URL features
            features = extract_features(url)

            # Convert features into DataFrame
            input_data = pd.DataFrame([features])

            # Predict result
            prediction = model.predict(input_data)[0]

            # Get phishing probability
            probabilities = model.predict_proba(input_data)[0]
            phishing_probability = probabilities[1] * 100

            st.subheader("Detection Result")

            if prediction == 1:
                st.error("⚠️ Phishing Website")
            else:
                st.success("✅ Legitimate Website")

            st.write(
                f"Phishing Probability: {phishing_probability:.2f}%"
            )

            st.warning(
                "This is an ML prediction, not a guarantee of website safety."
            )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a website URL.")
