# Telco Customer Churn Prediction

## Project Overview
This project analyzes telecom customer data to identify customer churn patterns and predict whether a customer is likely to leave the service.

It combines Python-based data analysis and machine learning, an interactive Streamlit application, and a Power BI dashboard to provide insights into customer behavior and retention.

## Project Objectives
- Analyze customer churn patterns.
- Perform data cleaning and preprocessing.
- Explore customer behavior through Exploratory Data Analysis (EDA).
- Build and evaluate machine learning models.
- Predict customer churn using a Random Forest model.
- Visualize business insights through Power BI.

## Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Power BI
- Jupyter Notebook

## Project Structure

```text
telco-customer-churn-prediction/
│
├── data/
├── notebooks/
│   ├── 01_DataLoading_and_EDA.ipynb
│   ├── 02_Feature_Engineering_and_Preprocessing.ipynb
│   ├── 03_Modeling_and_Evaluation.ipynb
│   ├── cleaned_telco.csv
│   ├── preprocessed_telco_churn.csv
│   └── best_random_forest.pkl
│
├── powerbi/
│   └── Dashboard.pbix
│
├── app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Key Features
- Customer churn analysis
- Customer segmentation and behavioral insights
- Machine learning-based churn prediction
- Interactive Streamlit application
- Three-page Power BI dashboard

## How to Run the Streamlit Application

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd telco-customer-churn-prediction-main
```

3. Create and activate a virtual environment.

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
streamlit run app.py
```

## Power BI Dashboard

The Power BI dashboard contains three pages:

1. Customer Churn Overview
2. Customer Churn Analysis
3. Customer Retention Insights

Open `powerbi/Dashboard.pbix` using Power BI Desktop to explore the dashboard.

## Future Improvements
- Improve model performance through hyperparameter tuning.
- Add more customer retention recommendations.
- Deploy the Streamlit application online.

## Author
Nikhitha Mohandas

B.Tech Computer Science and Engineering | Data Analytics

