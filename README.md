# Customer_Churn_Predictor_Model
Production-style customer churn prediction using Logistic Regression and Random Forest with clean pipelines, batch inference, and real-world ML practices.

# Customer Churn Prediction (Production-Style ML Project)

This repository demonstrates an **end-to-end, production-style machine learning system** for predicting customer churn using **classical ML models**.  
The focus of this project is not just model accuracy, but **real-world ML engineering practices** such as clean preprocessing pipelines, data leakage prevention, batch inference, and model comparison.


## Project Overview

Customer churn prediction helps businesses identify users who are likely to stop using a product or service.  
This project builds a churn prediction system that:

- Uses **tabular customer behavior data**
- Applies **robust preprocessing with pipelines**
- Trains and compares **Logistic Regression** and **Random Forest**
- Supports **batch inference on new customer data**
- Outputs **business-friendly churn risk buckets**

The design mirrors how churn models are built and used in real companies.


## Key Concepts Demonstrated

- Proper **train vs inference data separation**
- Data leakage prevention using `Pipeline` and `ColumnTransformer`
- Handling categorical and numerical features safely
- Batch prediction workflow (CSV → CSV)
- Production-oriented project structure
- Responsible dataset usage and licensing awareness

## Features Used

### Numeric Features
- Age
- Days since last login
- Average time spent
- Average transaction value
- Login frequency
- Wallet points
- Customer tenure (days)

### Categorical Features
- Gender
- Region category
- Membership type
- Referral status
- Offer preferences
- Platform and internet type
- Complaint history
- Feedback
- Last visit time bucket


## Models Used

### Logistic Regression
- Strong baseline
- Highly interpretable
- Stable and production-friendly

### Random Forest
- Captures non-linear relationships
- Handles feature interactions automatically
- Used only if it provides meaningful improvement

The final model choice is based on **validation performance**, not complexity.


## How to Run

- install everything mentioned in requirements.txt
- run train.py from root after putting a train.csv(in data folder) file with the columns marked in *features used* section above
- run python predict.py from root folder

## Input:

data/sample_input.csv (randomly generated unseen data, you can use your own set of unseen data here)

## Output:

data/predictions.csv with:

- churn probability
- churn risk bucket (Low, Medium, High)
- this mirrors real-world batch scoring jobs used in production.

No preprocessing on validation or test data

No target leakage

Safe handling of unseen categories

Metrics beyond accuracy (ROC-AUC, recall)

Clear separation of concerns in code

## Why Classical ML (Not LLMs)?

This project intentionally uses classical ML models because:

- tabular churn data is best handled by structured models
- logistic Regression and tree models are more interpretable
- LLMs are better suited for text understanding and explanation, not probability estimation
- LLMs can complement this system later as an explanation layer, not as the predictor.

## 📜 Data License & Attribution

This project was trained using data sourced from the Hugging Face dataset:

- **Dataset**: `d0r1h/customer_churn`
- **Source**: https://huggingface.co/datasets/d0r1h/customer_churn
- **License**: Apache License, Version 2.0

The Apache License 2.0 permits use, modification, and redistribution of the dataset,
provided that proper attribution is given and the license terms are preserved.

All data preprocessing steps (cleaning, feature engineering, column selection, and
transformations) were performed by the author of this project and constitute
derivative work based on the original dataset.

This repository fully adheres to the requirements of the Apache License 2.0:
- Attribution to the original dataset author is preserved
- The original license terms are acknowledged
- Any modifications to the data are clearly stated
- No warranties or guarantees are implied regarding the dataset

For the complete license text, see:
http://www.apache.org/licenses/LICENSE-2.0
