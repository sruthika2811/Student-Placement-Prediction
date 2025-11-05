import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from fpdf import FPDF

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="🎓 Student Placement Prediction Dashboard",
    layout="wide",
)

# ===================== CUSTOM CSS =====================
st.markdown("""
    <style>
    /* Animated gradient background */
    body {
        background: linear-gradient(270deg, #89f7fe, #66a6ff);
        background-size: 600% 600%;
        animation: gradientShift 12s ease infinite;
    }
    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #f5faff;
        color: #000;
        font-size: 16px;
        font-weight: bold;
    }

    h1,h2,h3 {
        color: #0c2461;
        text-align: center;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
    }

    .placed {background-color: #2ecc71;}
    .not-placed {background-color: #e74c3c;}
    </style>
""", unsafe_allow_html=True)

# ===================== LOAD MODELS =====================
rf_model = joblib.load("random_forest_model.pkl")
branch_encoder = joblib.load("branch_encoder.pkl")
intern_encoder = joblib.load("intern_encoder.pkl")

# ===================== SIDEBAR INPUT =====================
st.sidebar.header("🧾 Enter Student Details")
branch_display = ['CSE', 'IT', 'ECE', 'EEE', 'MECH', 'AI&DS']
intern_display = ['Yes', 'No']

cgpa = st.sidebar.number_input("CGPA (0 - 10)", min_value=0.0, max_value=10.0, step=0.1)
branch = st.sidebar.selectbox("Branch", branch_display)
major_projects = st.sidebar.slider("Major Projects Completed", 0, 5, 1)
mini_projects = st.sidebar.slider("Mini Projects Completed", 0, 10, 2)
communication = st.sidebar.slider("Communication Skill Rating (1-10)", 1, 10, 7)
internship = st.sidebar.selectbox("Internship Completed?", intern_display)

# ===================== MAIN PAGE =====================
st.title("🎓 Student Placement Prediction Dashboard")
st.markdown("#### Predict placement outcomes and visualize your dataset insights interactively!")

# Encode inputs
encoded_branch = branch_encoder.transform([branch])[0] if branch in branch_encoder.classes_ else 0
encoded_internship = intern_encoder.transform([internship])[0] if internship in intern_encoder.classes_ else 0

input_data = pd.DataFrame({
    'CGPA': [cgpa],
    'Branch': [encoded_branch],
    'Major Projects': [major_projects],
    'Mini Projects': [mini_projects],
    'Communication Skill Rating': [communication],
    'Internship': [encoded_internship]
})

# ===================== PREDICTION =====================
if st.sidebar.button("🔍 Predict Placement"):
    prediction = rf_model.predict(input_data)[0]

    if prediction == 1:
        st.markdown('<div class="result-box placed">✅ The student is LIKELY TO BE PLACED!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box not-placed">❌ The student is NOT LIKELY TO BE PLACED.</div>', unsafe_allow_html=True)

    # ===================== SUGGESTIONS =====================
    st.subheader("💡 Suggestions for Improvement")
    if cgpa < 6.5:
        st.write("- 📘 Improve CGPA with consistent academic performance.")
    if communication < 6:
        st.write("- 🎤 Enhance communication and presentation skills.")
    if major_projects < 1 or mini_projects < 2:
        st.write("- 💻 Take part in more projects or internships.")
    if internship == 'No':
        st.write("- 💼 Do at least one internship for real-world exposure.")
    else:
        st.write("- 🌟 Great! Keep enhancing your technical expertise.")

    # ===================== VISUALS =====================
    st.subheader("📊 Student Performance Overview")

    chart_data = pd.DataFrame({
        'Category': ['CGPA', 'Communication', 'Projects', 'Internship'],
        'Score': [cgpa, communication, major_projects + mini_projects, 10 if internship == 'Yes' else 5]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(chart_data, x='Category', y='Score',
                      color='Score', color_continuous_scale='Viridis',
                      title='Performance Summary')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        pie_data = pd.DataFrame({
            'Placement Status': ['Placed', 'Unplaced'],
            'Count': [70, 30]  # Example data
        })
        fig2 = px.pie(pie_data, names='Placement Status', values='Count',
                      color='Placement Status',
                      color_discrete_sequence=['#2ecc71', '#e74c3c'],
                      title='Overall Placement Ratio')
        st.plotly_chart(fig2, use_container_width=True)

    # ===================== PDF EXPORT =====================
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Student Placement Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"CGPA: {cgpa}", ln=True)
    pdf.cell(200, 10, txt=f"Branch: {branch}", ln=True)
    pdf.cell(200, 10, txt=f"Communication: {communication}/10", ln=True)
    pdf.cell(200, 10, txt=f"Internship: {internship}", ln=True)
    pdf.cell(200, 10, txt=f"Prediction: {'Placed' if prediction==1 else 'Not Placed'}", ln=True)

    pdf.output("Student_Placement_Report.pdf")
    st.success("📄 Report saved as 'Student_Placement_Report.pdf' in your folder.")

# ===================== DATASET UPLOAD & INSIGHTS =====================
st.markdown("---")
st.header("📂 Upload Placement Dataset for Insights")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset loaded successfully!")
    st.dataframe(df.head())

    if "PlacementStatus" in df.columns:
        col3, col4 = st.columns(2)

        with col3:
            fig_pie = px.pie(df, names="PlacementStatus",
                             title="🎯 Placement Distribution",
                             color_discrete_sequence=px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig_pie, use_container_width=True)

        with col4:
            fig_bar = px.bar(df, x="Branch", color="PlacementStatus",
                             title="🏫 Branch-wise Placement Comparison",
                             color_discrete_sequence=px.colors.qualitative.Set3)
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("⚠️ 'PlacementStatus' column not found in the dataset.")
else:
    st.info("📥 Upload a dataset to explore placement insights.")
