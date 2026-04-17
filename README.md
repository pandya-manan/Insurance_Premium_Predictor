# 🏥 Insurance Premium Prediction System

An end-to-end Machine Learning project that predicts insurance premiums based on customer demographics, lifestyle, and medical history.
The project includes **data cleaning, feature engineering, model comparison, and deployment using Streamlit**.

---

## 🚀 Live Demo

*(Add your deployed link here after deployment)*

---

## 📌 Problem Statement

Shield Insurance is expanding into a new market and wants to estimate **annual insurance premiums** based on customer data.

The goal is to:

* Build a predictive model
* Minimize prediction error
* Ensure business reliability (low high-error percentage)

---

## 📊 Dataset Features

The dataset includes:

* **Demographics**: Age, Gender, Region, Marital Status
* **Financial**: Income (Lakhs)
* **Health**: BMI Category, Smoking Status, Medical History
* **Lifestyle**: Physical Activity, Stress Level
* **Other**: Number of Dependants, Employment Status
* **Target**: Annual Premium Amount

---

## 🧹 Data Cleaning

Performed extensive data cleaning:

* Removed invalid **age values (>100)**
* Removed unrealistic **dependants (e.g., 456, 230)**
* Handled missing values in:

  * Smoking Status
  * Employment Status
* Removed redundant feature: `income_level`

---

## ⚙️ Feature Engineering

### 🔥 Lifestyle Risk Score

Created a new feature using business logic:

* Physical Activity:

  * High = 0, Medium = 1, Low = 4
* Stress Level:

  * Low = 0, Medium = 1, High = 4

**Final Score = Activity + Stress**

---

### 🏥 Medical History Processing

Converted multi-label text into structured features:

* diabetes
* high_bp
* heart_disease
* thyroid

Also created:

👉 `disease_count` (total number of diseases)

---

### 🧠 Encoding Strategy

| Feature Type | Method           |
| ------------ | ---------------- |
| Binary       | Label Encoding   |
| Ordinal      | Manual Mapping   |
| Nominal      | One-Hot Encoding |

---

## 🤖 Model Training

Trained multiple models:

### 1. Linear Regression

* Baseline model
* R² ≈ 0.96

### 2. Random Forest

* R² ≈ 0.9919

### 3. XGBoost (Final Model)

* R² ≈ **0.9939**
* Best performance

---

## 📈 Model Evaluation

| Metric   | Value  |
| -------- | ------ |
| MAE      | ₹569   |
| RMSE     | ₹699   |
| R² Score | 0.9939 |

---

## 📊 Business Metric

Percentage of predictions with **>10% error**:

👉 **6.87%**

✔ ~93% predictions are within acceptable range

---

## 🌐 Deployment

Built an interactive web app using Streamlit:

### Features:

* User-friendly input UI
* Real-time premium prediction
* Handles all feature transformations internally

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📂 Project Structure

```
📁 Insurance-Premium-Predictor
│
├── app.py
├── model.pkl
├── features.pkl
├── requirements.txt
├── premiums_with_life_style.ipynb
├── README.md
```

---

## 💡 Key Learnings

* Importance of **data cleaning and validation**
* Feature engineering using **business logic**
* Model comparison and selection
* Handling categorical variables properly
* Deploying ML models with Streamlit

---

## 🚀 Future Improvements

* Add model explainability (SHAP)
* Improve UI/UX
* Add API backend
* Integrate real-time data

---

## 👨‍💻 Author

**Manan Pandya**

---

## ⭐ If you found this project useful, consider giving it a star!
