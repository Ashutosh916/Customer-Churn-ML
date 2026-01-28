TARGET = "churn_risk_score"

NUMERIC_FEATURES = [
    "age",
    "days_since_last_login",
    "avg_time_spent",
    "avg_transaction_value",
    "avg_login_frequency_days",
    "points_in_wallet",
    "customer_tenure_days"
]

CATEGORICAL_FEATURES = [
    "gender",
    "region_category",
    "membership_category",
    "joined_through_referral",
    "preferred_offer_type",
    "platform",
    "internet_type",
    "used_special_discount",
    "offer_application_preference",
    "past_complaint",
    "feedback",
    "last_visit_bucket"
]