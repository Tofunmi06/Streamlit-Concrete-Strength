import streamlit as st
import numpy as np
import joblib



# Load trained model
model = joblib.load('Concrete_model.pkl')

st.title('Concrete Strength Predictor')

st.write("Enter concrete mix details to predict compressive strength in MPa")

# Inputs

cement = st.number_input('Cement (Kg/m3)')
slag = st.number_input('Blast Furnance Slag (Kg/m3)')
flyash = st.number_input('FlyAsh(Kg/m3)')
water = st.number_input('water(Kg/m3)')
sp = st.number_input('Superplasticizer (Kg/m3)')
coarse = st.number_input('Coarse aggregate (Kg/m3)')
fine = st.number_input('Fine aggregate (Kg/m3)')
age = st.number_input('Age (days)')

if st.button('Predict Strength'):
    inputs = np.array([[cement,slag,flyash,water,sp,coarse,fine,age]])
    prediction = model.predict(inputs)[0]
    st.success(f'Predicted Strength: {prediction:.2f} MPa')