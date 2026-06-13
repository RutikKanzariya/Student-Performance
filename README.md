# 🎓 Student Performance Predictor

## 📌 Project Overview

The Student Performance Predictor is an end-to-end Machine Learning project that predicts whether a student is likely to **Pass** or **Fail** based on demographic and educational factors.

This project demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, hyperparameter tuning, model deployment, and web application development using Streamlit.

---

## 🚀 Live Demo

Add your deployment link here after deployment:

```text
https://student-performance-ceswav6lfmucggd37qgkyi.streamlit.app/
```

---

## 📊 Dataset

Dataset: Student Performance Dataset

Features:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course

Target Variable:

* Pass (1)
* Fail (0)

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

### Tools

* Jupyter Notebook
* Git
* GitHub

---

## 🔄 Machine Learning Lifecycle

### 1. Data Collection

* Loaded the Student Performance Dataset.

### 2. Exploratory Data Analysis (EDA)

* Head, Tail
* Shape
* Info
* Data Types
* Missing Value Analysis
* Statistical Summary
* Histograms
* Boxplots
* Countplots
* Correlation Analysis

### 3. Data Preprocessing

* Checked Missing Values
* Removed Duplicates
* Feature Engineering
* Label Creation (Pass/Fail)

### 4. Encoding

* One-Hot Encoding using Pandas

### 5. Feature Scaling

* StandardScaler

### 6. Train-Test Split

* Training Data: 80%
* Testing Data: 20%

### 7. Model Training

The following models were trained:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes
* Decision Tree
* Random Forest
* Support Vector Classifier (SVC)

### 8. Model Evaluation

Metrics Used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Classification Report
* Cross Validation

### 9. Hyperparameter Tuning

Used GridSearchCV for Logistic Regression optimization.

Best Parameters:

```python
{
    'C': 0.01,
    'solver': 'liblinear'
}
```

---

## 📈 Model Performance

### Logistic Regression

Accuracy: 69%

Cross Validation Mean Score:

```text
0.6866
```

---

## 📂 Project Structure

```text
StudentPerformancePredictor/
│
├── app.py
├── StudentPerformance.ipynb
├── student_model.pkl
├── scaler.pkl
├── Featurename.pkl
├── requirements.txt
├── README.md
│
└── dataset/
    └── StudentsPerformance.csv
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/RutikKanzariya/StudentPerformance.git
```

Move to project directory:

```bash
cd StudentPerformance
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 Features

* End-to-End ML Project
* Data Analysis and Visualization
* Multiple Model Comparison
* Hyperparameter Tuning
* Model Serialization using Joblib
* Interactive Streamlit Web Application
* Ready for Deployment

---

## 📚 Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* One-Hot Encoding
* Standardization
* Model Training
* Model Evaluation
* Cross Validation
* Hyperparameter Tuning
* Streamlit Deployment
* Git & GitHub

---

## 👨‍💻 Author

Rutik Kanzariya

GitHub:
https://github.com/RutikKanzariya

---

## ⭐ Future Improvements

* FastAPI Integration
* Docker Containerization
* CI/CD Pipeline
* Cloud Deployment
* Advanced Feature Engineering
* Improved Model Performance
