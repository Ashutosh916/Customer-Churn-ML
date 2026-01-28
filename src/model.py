from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def build_logistic_pipeline(preprocessor):
    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", LogisticRegression(max_iter=3000, class_weight="balanced"))
        ]
    )

def build_rf_pipeline(preprocessor):
    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                n_jobs=-1
            ))
        ]
    )