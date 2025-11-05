# 🎓 Student Placement Prediction Dashboard

An interactive **Streamlit web application** that predicts student placement chances based on CGPA, branch, projects, communication skills, and internship experience.

## 📖 About
This project is designed to help colleges and students predict placement chances using Data Science.  
The dashboard takes key inputs like CGPA, branch, projects, and internships, and predicts whether a student is likely to get placed.  
It also provides **data insights**, **suggestions for improvement**.

## ✨ Features
- 🎯 Predicts placement likelihood using trained Data Science model  
- 📊 Generates real-time charts and insights   
- 🎨 Beautiful gradient UI with interactive visuals  
- 🧠 Uses encoders for handling categorical data  
- 📁 Supports CSV upload for batch insights

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** – Web UI  
- **Scikit-learn** – Data Science  
- **Plotly** – Data Visualization  
- **Pandas** – Data Analysis   
- **Joblib** – Model and Encoder Saving  

## 📊 Dataset Info

The dataset (`Placement_Data_with_Branch.csv`) includes the following columns:

- **CGPA** — Student's CGPA (out of 10)  
- **Branch** — Department (CSE, IT, ECE, EEE, MECH, AI&DS)  
- **Major Projects** — Number of major projects completed  
- **Mini Projects** — Number of mini projects completed  
- **Communication Skill Rating** — Rating from 1 to 10  
- **Internship** — Whether the student completed an internship (Yes/No)  
- **Placement Status** — Target variable (Placed / Unplaced)

## 🖼️ Screenshots

### 🎯 Dashboard View
![Dashboard Screenshot](images/dashboard.png)

### 📊 Insights & Charts
![Charts Screenshot](images/insights.png)

### 📄 Generated PDF
![PDF Screenshot](images/pdf_report.png)

## 🚀 Future Enhancements
- Add login system for students and admin
- Store predictions in database
- Display placement analytics department-wise
- Integrate cloud hosting (Streamlit Cloud / HuggingFace)




