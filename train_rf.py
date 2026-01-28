import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib

from src.config import TARGET, NUMERIC_FEATURES, CATEGORICAL_FEATURES
from src.preprocess import build_preprocessor
from src.model import build_rf_pipeline

df = pd.read_csv("data/train.csv")

X = df.drop(columns=[TARGET])
y = df[TARGET]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

preprocessor = build_preprocessor(NUMERIC_FEATURES, CATEGORICAL_FEATURES)
pipeline = build_rf_pipeline(preprocessor)

pipeline.fit(X_train, y_train)

val_probs = pipeline.predict_proba(X_val)[:, 1]
print("ROC-AUC:", roc_auc_score(y_val, val_probs))

joblib.dump(pipeline, "churn_model.joblib")
print("Model saved as churn_model.joblib")