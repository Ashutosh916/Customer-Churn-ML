from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def build_preprocessor(numeric_features, categorical_features):
    """
    Builds preprocessing pipeline:
    - numeric → passthrough
    - categorical → one-hot encoding
    """
    return ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )