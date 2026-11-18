# # import libraries
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import warnings

# warnings.filterwarnings("ignore")

# # set title and layout
# st.set_page_config(page_title="Telco Customer Churn Prediction", layout="wide")
# st.title("📊 Telco Customer Churn Prediction App")

# # load data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
#     return df

# df = load_data()

# # show raw data
# st.subheader("🔍 Raw Data")
# st.dataframe(df.head())

# # churn distribution plot
# st.subheader("📌 Churn Distribution")
# fig1, ax1 = plt.subplots()
# sns.countplot(x="Churn", data=df, ax=ax1)
# st.pyplot(fig1)

# # churn by contract type
# st.subheader("📊 Churn by Contract Type")
# fig2, ax2 = plt.subplots()
# sns.countplot(x="Contract", hue="Churn", data=df, ax=ax2)
# st.pyplot(fig2)


# st.markdown("---")
# st.header("🔮 Predict Customer Churn")
# import joblib

# # Load model
# model = joblib.load("notebooks/best_logistic_regression.pkl")

# # Define feature columns (based on your preprocessed data)
# feature_columns = [
#     'gender',
#     'SeniorCitizen',
#     'Partner',
#     'Dependents',
#     'tenure',
#     'PhoneService',
#     'PaperlessBilling',
#     'MonthlyCharges',
#     'TotalCharges',
#     'MultipleLines_No phone service',
#     'MultipleLines_Yes',
#     'InternetService_Fiber optic',
#     'InternetService_No',
#     'OnlineSecurity_No internet service',
#     'OnlineSecurity_Yes',
#     'OnlineBackup_No internet service',
#     'OnlineBackup_Yes',
#     'DeviceProtection_No internet service',
#     'DeviceProtection_Yes',
#     'TechSupport_No internet service',
#     'TechSupport_Yes',
#     'StreamingTV_No internet service',
#     'StreamingTV_Yes',
#     'StreamingMovies_No internet service',
#     'StreamingMovies_Yes',
#     'Contract_One year',
#     'Contract_Two year',
#     'PaymentMethod_Credit card (automatic)',
#     'PaymentMethod_Electronic check',
#     'PaymentMethod_Mailed check'
# ]

# # Title
# st.set_page_config(page_title="Telco Churn Predictor", layout="centered")
# st.title("📊 Telco Customer Churn Prediction")

# # User Inputs
# gender = st.selectbox("Gender", [1, 0])
# senior = st.selectbox("Senior Citizen", [0, 1])
# partner = st.selectbox("Partner", ["Yes", "No"])
# dependents = st.selectbox("Dependents", ["Yes", "No"])
# tenure = st.slider("Tenure (months)", 0, 72, 12)
# phone_service = st.selectbox("Phone Service", ["Yes", "No"])
# paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
# monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
# total = st.number_input("Total Charges", 0.0, 10000.0, 3000.0)

# # Additional One-Hot Features
# multi_lines = st.selectbox("Multiple Lines", ["No phone service", "Yes", "No"])
# internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
# online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
# online_bak = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
# device_protect = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
# tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
# stream_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
# stream_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
# contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
# payment = st.selectbox("Payment Method", [
#     "Electronic check",
#     "Mailed check",
#     "Bank transfer (automatic)",
#     "Credit card (automatic)"
# ])

# # Manually build one-hot encoded features
# input_data = {}

# # Binary categories
# input_data['SeniorCitizen'] = senior
# input_data['tenure'] = tenure
# input_data['MonthlyCharges'] = monthly
# input_data['TotalCharges'] = total

# # One-hot encode 'gender'
# input_data['gender_Male'] = 1 if gender == 'Male' else 0
# input_data['gender_Female'] = 1 if gender == 'Female' else 0

# # Partner & Dependents
# input_data['Partner_Yes'] = 1 if partner == 'Yes' else 0
# input_data['Partner_No'] = 1 if partner == 'No' else 0
# input_data['Dependents_Yes'] = 1 if dependents == 'Yes' else 0
# input_data['Dependents_No'] = 1 if dependents == 'No' else 0

# # PhoneService & PaperlessBilling
# input_data['PhoneService_Yes'] = 1 if phone_service == 'Yes' else 0
# input_data['PhoneService_No'] = 1 if phone_service == 'No' else 0
# input_data['PaperlessBilling_Yes'] = 1 if paperless == 'Yes' else 0
# input_data['PaperlessBilling_No'] = 1 if paperless == 'No' else 0

# # Remaining one-hot fields
# input_data[f'MultipleLines_{multi_lines}'] = 1
# input_data[f'InternetService_{internet}'] = 1
# input_data[f'OnlineSecurity_{online_sec}'] = 1
# input_data[f'OnlineBackup_{online_bak}'] = 1
# input_data[f'DeviceProtection_{device_protect}'] = 1
# input_data[f'TechSupport_{tech_support}'] = 1
# input_data[f'StreamingTV_{stream_tv}'] = 1
# input_data[f'StreamingMovies_{stream_movies}'] = 1

# if contract == "One year":
#     input_data['Contract_One year'] = 1
# elif contract == "Two year":
#     input_data['Contract_Two year'] = 1

# if payment == "Credit card (automatic)":
#     input_data['PaymentMethod_Credit card (automatic)'] = 1
# elif payment == "Electronic check":
#     input_data['PaymentMethod_Electronic check'] = 1
# elif payment == "Mailed check":
#     input_data['PaymentMethod_Mailed check'] = 1

# # Fill missing expected columns with 0
# for col in feature_columns:
#     if col not in input_data:
#         input_data[col] = 0

# # Final input DataFrame
# input_df = pd.DataFrame([input_data])[feature_columns]


# # Predict
# if st.button("Predict Churn"):
#     prediction = model.predict(input_df)[0]
#     if prediction == 1:
#         st.error("⚠️ The customer is likely to churn.")
#     else:
#         st.success("✅ The customer is not likely to churn.")
# # github link     
# st.markdown("---")
# st.markdown("[🔗 View Full Project on GitHub](https://github.com/shivharebhupendra/telco-customer-churn-prediction)")



# ==========================================
# TELCO CUSTOMER CHURN PREDICTION APP
# ==========================================

# 1. Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import warnings

from pathlib import Path

warnings.filterwarnings("ignore")


# 2. Project paths
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

MODEL_PATH = BASE_DIR / "notebooks" / "best_random_forest.pkl"

PREPROCESSED_PATH = BASE_DIR / "notebooks" / "preprocessed_telco_churn.csv"


# 3. Page configuration
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telco Customer Churn Prediction App")

st.markdown(
    "Explore customer churn patterns and predict "
    "whether a customer is likely to leave the service."
)


# 4. Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

    return df


# 5. Load trained model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# 6. Check files
if not DATA_PATH.exists():
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()

if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

if not PREPROCESSED_PATH.exists():
    st.error(f"Preprocessed dataset not found: {PREPROCESSED_PATH}")
    st.stop()


# 7. Load data and model
df = load_data()
model = load_model()

preprocessed_df = pd.read_csv(PREPROCESSED_PATH)


# 8. Identify model feature columns
if hasattr(model, "feature_names_in_"):

    feature_columns = list(model.feature_names_in_)

else:

    feature_columns = [
        col for col in preprocessed_df.columns
        if col not in ["Churn", "customerID"]
    ]


# ==========================================
# SECTION 1: DATA EXPLORATION
# ==========================================

st.header("🔍 Customer Data Exploration")

st.subheader("Raw Customer Data")

st.dataframe(df.head(), use_container_width=True)

st.write("Total Customers:", len(df))

st.write(
    "Total Churned Customers:",
    (df["Churn"] == "Yes").sum()
)


# ==========================================
# SECTION 2: CHURN DISTRIBUTION
# ==========================================

st.subheader("📌 Churn Distribution")

fig1, ax1 = plt.subplots(figsize=(7, 4))

sns.countplot(
    x="Churn",
    data=df,
    ax=ax1
)

ax1.set_title("Customer Churn Distribution")
ax1.set_xlabel("Churn")
ax1.set_ylabel("Number of Customers")

st.pyplot(fig1)
plt.close(fig1)


# ==========================================
# SECTION 3: CHURN BY CONTRACT TYPE
# ==========================================

st.subheader("📊 Churn by Contract Type")

fig2, ax2 = plt.subplots(figsize=(8, 4))

sns.countplot(
    x="Contract",
    hue="Churn",
    data=df,
    ax=ax2
)

ax2.set_title("Churn by Contract Type")
ax2.set_xlabel("Contract Type")
ax2.set_ylabel("Number of Customers")

st.pyplot(fig2)
plt.close(fig2)


# ==========================================
# SECTION 4: CUSTOMER CHURN PREDICTION
# ==========================================

st.markdown("---")

st.header("🔮 Predict Customer Churn")

st.write(
    "Enter the customer details below to predict "
    "whether the customer is likely to churn."
)


# 9. Collect customer information

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0, 72, 12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No phone service", "No", "Yes"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )


with col2:

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=3000.0
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


# ==========================================
# SECTION 5: PREPARE INPUT DATA
# ==========================================

if st.button("Predict Churn", type="primary"):

    # Create raw customer input
    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    # Apply one-hot encoding
    input_encoded = pd.get_dummies(input_data)

    # Match the model's training feature names and order
    input_encoded = input_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    try:

        # Make prediction
        prediction = model.predict(input_encoded)[0]

        st.markdown("---")
        st.subheader("Prediction Result")

        if str(prediction).strip().lower() in ["1", "yes", "true"]:

            st.error(
                "⚠️ The customer is likely to churn."
            )

        else:

            st.success(
                "✅ The customer is not likely to churn."
            )

        # Display prediction probability if supported
        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_encoded
            )[0]

            st.write("Prediction Probabilities:")

            for label, probability in zip(
                model.classes_, probabilities
            ):

                st.write(
                    f"{label}: {probability * 100:.2f}%"
                )

    except Exception as e:

        st.error("Prediction failed.")

        st.exception(e)


# ==========================================
# SECTION 6: GITHUB LINK
# ==========================================

st.markdown("---")

st.markdown(
    "[🔗 View Full Project on GitHub]"
    "(https://github.com/nikhitham055-cell/telco-customer-churn-prediction?utm_source=chatgpt.com)"
)
