# AI-Based Phishing Detection System

## Project Overview
This project uses machine learning to identify phishing and legitimate websites by analyzing URL features. It extracts 15 features from a URL and predicts whether the website is Legitimate or Phishing.

## Objectives
- Detect phishing websites using machine learning.
- Extract 15 features from website URLs.
- Classify URLs as legitimate or phishing.
- Display prediction results using a web dashboard.

## Technologies Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Joblib

## Dataset Description
- Dataset source: Kaggle
- Total records used: 1,000
- Legitimate URLs: 500
- Phishing URLs: 500
- URL features: 15

## Machine Learning Algorithms
1. Random Forest
2. Decision Tree
3. Logistic Regression

Random Forest achieved the best performance in our current experiment.

## Project Files
- app.py
- train.py
- predict.py
- features.py
- dataset.csv
- model.pkl
- requirements.txt

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## Conclusion
The AI-Based Phishing Detection System uses URL-based features and machine learning to identify potentially fraudulent websites. It provides a simple dashboard to help users check URLs. The prediction is not a guarantee of website safety.

## Developer
GitHub: https://github.com/bhoomikamamani53-uxbhoomika
