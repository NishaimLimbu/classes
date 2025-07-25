import streamlit as st
import joblib 
import numpy as np

#load the trained titanic model
model = joblib.load('titanic_model.pkl')

#App title
st.title('Titanic Survived Prediction')

# User inputs
st.header('Enter Passengers Details')

pclass=st.selectbox('Passenger Class (Pclass)',[1,2,3])
sex=st.radio('Gender',{'Male','Female'})
sex={'Male':1,'Female':0}[sex]
age=st.slider('Passenger Age',1,100,25)
sibsp=st.number_input('Passenger siblings and sposue', 0,10,2 )
parch=st.number_input('Passenger Parents or children', 0,10,2 )
fare=st.number_input('Passenger fare', 0.0,600.0,32.0 )

#prepare input
input_data=np.array([[pclass, sex, age, sibsp, parch, fare]])

#predict
if st.button('predict survival'):
    prediction = model.predict(input_data)
    result = 'Survived' if prediction[0] == 1 else 'Not-Sruvived'
    st.success(f"prediction: {result}")