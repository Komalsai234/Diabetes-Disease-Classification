import numpy as np
import streamlit as st
import joblib
from streamlit_extras.switch_page_button import switch_page
import time

weights, bias, hyperparams = joblib.load('hyperparameters.joblib')

def sigmoid(z):
    a=np.zeros([1,1])
    a=1/(1+np.exp(-z))
    return a
    
def ReLU(z):
    return np.maximum(z, 0)

def tanh(z):
    z=(np.exp(z)-np.exp(-z))/(np.exp(z)+np.exp(-z))
    z=1-z**2
    return z

def forward_propagation(weights, bias, hyperparams, x):
    z = []    
    a = []
    i = 0
    while i <= hyperparams['no_hidden_layers']:
        if i == 0:
            z.append(np.matmul(weights[i].T,x) + bias[i])   
        else:
            z.append(np.matmul(weights[i].T, a[i - 1]) + bias[i]) 
        if i == hyperparams['no_hidden_layers']:   
            if(hyperparams['output_activation_function'] == 'sigmoid'):
                a.append(sigmoid(z[i]))
            elif(hyperparams['output_activation_function'] == 'tanh'):
                a.append(tanh(z[i]))
            elif(hyperparams['output_activation_function'] == 'relu'):
                a.append(ReLU(z[i]))
        else:      
            if(hyperparams['activation_function_'+str(i)] == 'sigmoid'):
                a.append(sigmoid(z[i]))
            elif(hyperparams['activation_function_'+str(i)] == 'tanh'):
                a.append(tanh(z[i]))
            elif(hyperparams['activation_function_'+str(i)] == 'relu'):
                a.append(ReLU(z[i]))
        
        i+=1
    
    return z, a


def diabetes_pred(input_data):
    data = np.array(input_data).reshape(-1, 1) 
    z, a = forward_propagation(weights, bias, hyperparams, data)
    predicted_output = np.max(a[hyperparams['no_hidden_layers']])
    return 1 if predicted_output >= 0.5 else 0
    
st.subheader("Enter the details of the patients")

st.subheader(" ")
    
col1, col2 = st.columns(2)
    
col3,col4 = st.columns(2)
    
col5,col6 = st.columns(2)
    
with col1:
    age = st.number_input('Enter the Age',0,100,0,1,'%d')
    
with col2:
    bmi = st.number_input('Enter the BMI',0.0,100.0,0.0,1.0,'%f')
        
with col1:
    glucose = st.number_input('Enter the Glucose Level',0,200,0,1,'%d')
        
with col2:
    BP = st.number_input('Enter the Blood Pressure (BP)',0,150,0,1,'%d')
        
with col3:
    insulin = st.number_input('Enter the Insulin level',0,1000,0,1,'%d')
        
with col4:
    pregnancies = st.number_input('No.of Childrens for the paitents',0,10,0,1,'%d')

with col5:
    SkinThickness = st.number_input('Enter the Thickness of Skin',0,100,0,1,'%d')

with col6:
    dpf = st.number_input('Enter the Diabetes Pedigree Function',0.0,5.0,0.0,0.001,'%f')
        
button = st.button("Predict")

if button:
    data = np.array([pregnancies, glucose, BP, SkinThickness, insulin, bmi, dpf, age])
    prediction = diabetes_pred(data) 
    st.session_state['prediction'] = prediction
  
    with st.spinner('Wait for it...'):
        time.sleep(3)
    
    switch_page("results")
