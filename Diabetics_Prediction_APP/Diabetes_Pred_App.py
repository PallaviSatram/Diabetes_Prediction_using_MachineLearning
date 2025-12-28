import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/palla/OneDrive/Desktop/Diabetics_Prediction_APP/trained_model.sav','rb'))

# Creating a function for prediction

def diabetics_prediction(input_data):

  input_data_as_np_array=np.asarray(input_data)

  input_data_reshaped = input_data_as_np_array.reshape(1,-1)

  predicition = loaded_model.predict(input_data_reshaped)
  
  if predicition[0]==0:
    return "The person is not Diabetic"
  else:
    return "The person is Diabetic"

def main():

  # Giving a Title

  st.title('Diabetes Prediction Web App ')

  # getting the input data from the user

  Pregnancies = st.text_input('Number of Pregnancies ')
  Glucose = st.text_input('Glucose Level ')
  BloodPressure = st.text_input('Blood Pressure Value ')
  SkinThickness = st.text_input('Thickness of Skin ')
  Insulin = st.text_input('Insulin Level ')
  BMI = st.text_input('BMI Value ')
  DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value ')
  Age = st.text_input('Age of the Person ')

  # code for prediction

  diagnosis = ''

  # creating a button for prediction
  if st.button('Diabetes Test Result'):
    diagnosis = diabetics_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]) # order should be same
  st.success(diagnosis)

if __name__ == '__main__':
  main()







