import streamlit as st
import pickle
import numpy as np

# Saved AI model ko load kar rahe hain
model = pickle.load(open('diabetes_model.sav', 'rb'))

# Website ka Title aur Theme
st.set_page_config(page_title="Sanjivani", page_icon="🏥", layout="centered")
st.title('Sanjivani: Diabetes Risk Predictor 🏥')
st.markdown("---")
st.write('This AI model predicts the likelihood of diabetes based on laboratory metrics. Enter the details below:')

# User se inputs lene ke liye boxes
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Pregnancies Count', min_value=0, max_value=20, value=0)
    glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=200, value=120)
    bp = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=150, value=70)
    skin = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, max_value=900, value=80)
    bmi = st.number_input('BMI Value (Weight in kg/(height in m)^2)', min_value=0.0, max_value=70.0, value=25.0)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, format="%.3f")
    age = st.number_input('Age of the Person', min_value=0, max_value=120, value=30)

st.markdown("---")

# Prediction Button
if st.button('Predict Diabetes Risk', use_container_width=True):
    # Inputs ko array me convert kar rahe hain
    features = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    # AI se predict karwa rahe hain
    prediction = model.predict(features)
    
    # Result display kar rahe hain
    if prediction[0] == 1:
        st.error('⚠️ High Risk: The AI predicts a high probability of diabetes. Please consult a medical professional.')
    else:
        st.success('✅ Low Risk: The AI predicts a low probability of diabetes. Keep maintaining a healthy lifestyle!')
