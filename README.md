# 📘 PeakLoadNet – Energy Demand Prediction

This project predicts **National Energy Demand** using Machine Learning techniques.  
It includes complete data preprocessing, model training, evaluation, and deployment as a real-time API using Flask and Render.

---

## 🚀 Project Overview

The objective of this project is to analyze historical energy demand data and build a machine learning model that can predict future energy demand based on features such as:

- Temperature  
- Humidity  
- Wind Speed  
- Solar Radiation  
- Historical Energy Demand  

The final trained model is deployed as a **REST API**, allowing external applications to send input features and receive predicted demand values.

---

## 🧠 Machine Learning Models Used

### ✔ Linear Regression *(Final deployed model)*  
- Lightweight  
- Fast inference  
- Very small file size (<200 KB)  
- Ideal for cloud deployment (Render)

### ❌ Random Forest (Not deployed due to size limits)  
A Random Forest model was also trained, but model file size exceeded Render’s 20MB free limit.  
Therefore, Linear Regression was selected for deployment.

---

## 📊 Key Features

- Performed full dataset cleaning and preprocessing  
- Resolved data leakage issues  
- Converted datetime column and extracted usable features  
- Created train/test split (80/20)  
- Trained and evaluated multiple ML models  
- Generated Actual vs Predicted comparison visualizations  
- Calculated regression metrics (MAE, MSE, RMSE, R² Score)  
- Exported final model using `.joblib` format  
- Built a Flask backend for prediction  
- Deployed API on Render Cloud Platform  

---

## 🌐 Live API URL

 backend is live and publicly accessible at:
 
https://aicte-energy-peakloadnet-neural-network-5juq.onrender.com/
