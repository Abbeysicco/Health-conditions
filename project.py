import pandas as pd
import numpy as np 
import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

st.header('Welcome to Nutrition Facts/ Health conditions')
st.text_input("Enter Patient's Name:", key="name")

Ages = st.number_input("Enter Patient's Age", min_value=0, max_value=100, format="%d")
Gender = st.number_input("Enter Patient's Gender (0=Female, 1=Male)", min_value=0, max_value=1, format="%d")
Height = st.number_input("Enter Patient's Height (in cm)", min_value=0.0, max_value=500.0, step=0.1, format="%.2f") 
Weight = st.number_input("Enter Patient's Weight (in kg)", min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Activity_Level = st.number_input("Enter Patient's Activity Level (0-4)", min_value=0, max_value=4, format="%d")
Dietary_Preference = st.number_input("Enter Patient's Dietary Preference (0-3)", min_value=0, max_value=3, format="%d")
Daily_Calorie_Target = st.number_input("Enter Patient's Daily Calorie Target", min_value=0.0, max_value=5000.0, step=0.1, format="%.2f") 
Protein=st.number_input("Enter Patient's Protein",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Sugar=st.number_input("Enter Patient's Sugar",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Sodium=st.number_input("Enter Patient's Sodium",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Calories=st.number_input("Enter Patient's Calories",min_value=0.0, max_value=5000.0, step=0.1, format="%.2f")
Carbohydrates=st.number_input("Enter Patient's Carbohydrates",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Fiber=st.number_input("Enter Patient's Fiber",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Fat=st.number_input("Enter Patient's Fat",min_value=0.0, max_value=500.0, step=0.1, format="%.2f")
Breakfast_Suggestion=st.number_input("Enter Patient's Breakfast Suggestion",min_value=0, max_value=500, format="%d")
Lunch_Suggestion=st.number_input("Enter Patient's Lunch Suggestion",min_value=0, max_value=500, format="%d")
Dinner_Suggestion=st.number_input("Enter Patient's Dinner Suggestion",min_value=0, max_value=500, format="%d")
Snack_Suggestion=st.number_input("Enter Patient's Snack Suggestion",min_value=0, max_value=500, format="%d")

#load model
with open('project_model.pickle', 'rb') as loaded_model:
    model = pickle.load(loaded_model) 

with open('mlb_model.pickle', 'rb') as loaded_mlb:  
    mlb = pickle.load(loaded_mlb)


def predict_value(user_input_value):  
    try:  
        # Convert user input to a NumPy array and reshape  
        user_input = np.array(user_input_value)  
        user_input_reshaped = user_input.reshape(1, -1)  

        # Predicting the output  
        predicted = model.predict(user_input_reshaped)  

        # Displaying the predicted labels  
        results = []  # Store results to return  
        diseases = mlb.classes_    
        for i, disease in enumerate(diseases):  
            if predicted[0][i] == 1:  
                results.append(f"Yes, Affected by {disease}")  
            else:  
                results.append(f"No, Not Affected by {disease}")  

        return results  # Return the results  

    except Exception as e:  
        return [f"An error occurred during prediction: {e}"]  # Return error message as a list  

def main():  
    if st.button('Get Nutrition Facts / Health Conditions'):  
        user_input_values = [  
            Ages, Gender, Height, Weight, Activity_Level, Dietary_Preference,   
            Daily_Calorie_Target, Protein, Sugar, Sodium, Calories,   
            Carbohydrates, Fiber, Fat, Breakfast_Suggestion,   
            Lunch_Suggestion, Dinner_Suggestion, Snack_Suggestion  
        ]  
        
        predictions = predict_value(user_input_values)  
        for prediction in predictions:  
            st.success(prediction)  

if __name__ == "__main__":
    main()

if 'name' in st.session_state:  
    st.write(f"Nice working with you @ {st.session_state.name}") 
