# 🎓 Student Placement Prediction Dashboard

An interactive **Streamlit-based web app** that predicts whether a student is likely to be placed based on academic and skill factors.

## 🚀 Features
- Predict placement likelihood using trained Random Forest model  
- Visualize data insights (Bar & Pie Charts)  
- Animated gradient background with modern UI  
- Generate downloadable placement report (PDF)  
- Supports CSV dataset uploads for analysis  

## 🧠 Tech Stack
- **Python**
- **Streamlit**
- **Scikit-learn**
- **Plotly**
- **Pandas**
- **Joblib**
- **FPDF**

## 📂 Files Included
- `app.py` → Main dashboard code  
- `Placement_Data_with_Branch.csv` → Dataset used  
- `random_forest_model.pkl` → Trained ML model  
- `branch_encoder.pkl`, `intern_encoder.pkl` → Encoders for categorical data  
- `requirements.txt` → Dependencies list  

## 🖥️ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
