# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:39:41 2024

@author: prachet
"""

import numpy as np
import pickle
import streamlit as st

#loading. the saved model
loaded_model = pickle.load(open("calories_burnt_prediction_model.sav",'rb'))


#creating a function for prediction

def calorie_burnt_prediction(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    return prediction[0]


def main():
    
    #giving a title
    st.title('Calorie Burnt Prediction Web App')
    
    option = st.selectbox('Gender',('Male', 'Female'))
    gender = 1 if option == 'Female' else 0
    age = st.number_input("Age of the person")
    height = st.number_input("Height of the person")
    weight = st.number_input("Weight of the person")
    duration = st.number_input("Duration of Exercise in mins")
    heart_rate = st.number_input("Heart_Rate of the person")
    body_temp = st.number_input("Body Temperature of the person")
    
    
    # code for prediction
    calorie = ''
    
    #creating a button for Prediction
    if st.button('Predict House Price'):
        calorie = calorie_burnt_prediction((gender,age,height,weight,duration,heart_rate,body_temp))
        
    st.success('Calories Burnt: '+ str(calorie)+'cal')
    
    
    
if __name__ == '__main__':
    main()
