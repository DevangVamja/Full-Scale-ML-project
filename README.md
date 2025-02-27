# 📌 Full-Scale ML Project

🚀 **End-to-End Machine Learning Pipeline with Scalable Deployment**


## 📖 Overview

This repository demonstrates a **full-scale, end-to-end machine learning project**, covering everything from **data ingestion** to **model deployment**. The goal is to create a **scalable, production-ready ML pipeline** that ensures reproducibility, automation, and efficiency.

### 🔹 Key Features:
- ✅ **Automated Data Pipeline** – Efficient ingestion, cleaning, transformation, and feature engineering using **dbt, Pandas, and NumPy**.
- ✅ **Robust Model Training** – Hyperparameter tuning, cross-validation, and evaluation using **Scikit-learn, TensorFlow, and XGBoost**.
- ✅ **Model Serving & API** – Seamless deployment via **Flask & Docker** for real-time predictions.
- ✅ **CI/CD Integration** – Automated testing, monitoring, and deployment with **GitHub Actions & Kubernetes**.
- ✅ **Cloud Integration** – Scalable storage and computing with **AWS/GCP**.

---

## 🏗️ Project Structure

```plaintext
Full-Scale-ML-Project/
│── data/               # Raw and processed datasets
│── notebooks/          # Jupyter Notebooks for EDA & prototyping
│── src/                # Source code for pipeline & models
│   ├── components/     # Various components for Data ingestion & preprocessing
│   ├── data_pipeline/  # test and train pipelines for seamless integration
│── Dockerfile          # Containerization setup
│── requirements.txt    # Dependencies
│── app.py              # Flask app Endpoints
│── README.md           # Project documentation
│── setup.py            # For easy setup on local machine
```

---

## ⚙️ Installation & Setup

### 📌 Step 1: Clone the Repository

```bash
git clone https://github.com/DevangVamja/Full-Scale-ML-project.git
cd Full-Scale-ML-project
```

### 📌 Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 📌 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### **1️⃣ Launching Flask App**
Run the Flask app to start the servers:

```bash
python app.py
```

### **2️⃣ Data Ingestion, Transformation and Model Training**
Use "Train Model" button to run the train pipeline to clean, preprocess, and generate feature sets and Train the model with hyperparameter tuning:
or use Saved model to start predictions with "Predict Performance" button


### **3️⃣ Model Evaluation**

After the Model training, the R2 Score will be shown as accuracy and "Go to Prediction Page" will take you to prediction page.

### **4️⃣ Accessing the model**


Fill the all the fields in form and hit submit, the predicted Maths score will be displayed below the Form.



Access it at: **http://localhost:5000/**

---

## 🛠️ Technologies & Tools

✅ **Languages:** Python (Pandas, NumPy, Scikit-learn, TensorFlow, XGBoost)  
✅ **Model Deployment:** Docker, Kubernetes  
✅ **Cloud:** AWS S3, EC2, GCP AI Platform  
✅ **MLOps & CI/CD:** GitHub Actions, MLflow  

---

## 🏆 Future Improvements

- 🔹 **Fetching Data From MongoDB** for better Data Engineering

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project:

1. Fork the repo
2. Create a feature branch (`feature-xyz`)
3. Commit changes & open a PR

---

## 📬 Contact

👤 **Devang Vamja**  
📧 [devangvamja2000@gmail.com](mailto:devangvamja2000@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/DevangVamja)  

---
