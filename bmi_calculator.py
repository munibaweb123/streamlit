# body mass index calculator
# bmi = weight in kg/ (height in meters^2)
import streamlit as st

"""
# BMI Calculator
"""
weight = st.number_input('Enter weight/mass in kgs')

status = st.radio('select your height format',('m','ft','cm'))

if (status == 'cm'):
    "height in centimeters"
    try:
        height = st.number_input('Enter height in meters')

        bmi = weight / ((height/100)**2)
    except:
        "write accurate height"
elif (status == 'ft'):
    "height in feet"
    try:
        height = st.number_input('Enter height in feet')

        bmi = weight / ((height/3.28)**2)
    except:
        "write accurate height"
else:
    "height in meter"
    height = st.number_input('Enter height in meters')
    try:
        bmi = weight/(height**2)
    except:
        "your height is zero, write accurate height in meters"




if(st.button('Calculate BMI')):
    st.text(f"your bmi (body mass index is: {bmi})")
    if(bmi <= 16):
        st.error('you are extremely under weight')
    elif(bmi >= 16 and bmi <=18.5):
        st.warning('you are under weight')
    elif(bmi >= 18.5 and bmi <= 25):
        st.success('you are healthy')
    elif(bmi >= 25 and bmi <= 30):
        st.warning('you are over weight')
    else:
        st.error('you are extremely over weight')





