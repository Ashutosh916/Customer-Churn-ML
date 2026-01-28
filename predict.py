import pandas as pd
import joblib

from src.utils import churn_risk_bucket

pipeline = joblib.load("churn_model.joblib")

df = pd.read_csv("data/sample_input.csv")

probs = pipeline.predict_proba(df)[:, 1]

df["churn_probability"] = probs
df["churn_risk_bucket"] = df["churn_probability"].apply(churn_risk_bucket)

df.to_csv("data/predictions.csv", index=False)