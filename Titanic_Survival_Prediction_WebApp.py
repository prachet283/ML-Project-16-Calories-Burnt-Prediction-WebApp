# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:10:03 2024

@author: prachet
"""

import numpy as np
import pickle
import streamlit as st

#loading. the saved model
loaded_model = pickle.load(open("C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-15-Titanic Survival Prediction using Machine Learning/titanic_survival_prediction_trained_model.sav",'rb'))

#creating a function for prediction

def titanic_survival_prediction(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    if(prediction[0]==0):
      return 'The Person did not Survived'
    else:
      return 'The Person has Survived'
  
    
  
def main():
    
    #giving a title
    st.title('Titanic Survival Prediction Web App')
    
    #getting input data from user
    
    option1 = st.selectbox('Passenger class',('First class', 'Second class','Third class'))
    if option1 == 'First class':
        pclass = 1
    elif option1 == 'Second class':
        pclass = 2
    else:
        pclass = 3
    
    option2 = st.selectbox('Gender',('Male', 'Female'))
    if option2 == 'Male':
        sex = 0
    else:
        sex = 1
    
    age = st.number_input("Age of the person")
    
    sibsp = st.number_input("No of Siblings")
    
    parch = st.number_input("Parch")
    
    fare = st.number_input("Fare")
    
    option3 = st.selectbox('Embarked',('Southampton','Cherbourg', 'Queenstown'))
    if option3 == 'Southampton':
        embarked = 0
    elif option3 == 'Cherbourg':
        embarked = 1
    else:
        embarked = 2
    
    # code for prediction
    survived = ''
    
    #creating a button for Prediction
    if st.button('Survived Result'):
        survived = titanic_survival_prediction([pclass,sex,age,sibsp,parch,fare,embarked])
        
    st.success(survived)
    
    
    
if __name__ == '__main__':
    main()