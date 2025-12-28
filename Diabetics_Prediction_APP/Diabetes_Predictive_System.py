import numpy as np
import pickle

# loading the saved model

loaded_model = pickle.load(open('C:/Users/palla/OneDrive/Desktop/Diabetics_Prediction_APP/trained_model.sav','rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

# change this data into numpy array because the processing in numpy array is more
# efficient and easy

input_data_as_np_array=np.asarray(input_data)

# reshape the array as we are predicting for one instance
# if we do not reshape then the model expects 768 inputs

input_data_reshaped = input_data_as_np_array.reshape(1,-1)
# 1 row and as many columns as needed

# we cannot give this data directly to our model becoz while training our model

predicition = loaded_model.predict(input_data_reshaped)
print(predicition)
if predicition[0]==0:
  print("The person is not Diabetic")
else:
  print("The person is Diabetic")