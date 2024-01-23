import numpy as np
import pandas as pd
import joblib
import streamlit as st



def predicit_heartdisease(input):
    model = joblib.load('model.sav')
    input_array = np.asarray(input)
    input_reshaped = input_array.reshape(1,-1)
    prediction = model.predict(input_reshaped)
    return prediction[0]

def main():
    st.title("HeartWatch: Predicting Heart Health")
    age= st.text_input("Age")
    sex= st.number_input("Sex",min_value=0,max_value=1)
    cp= st.number_input("Chest pain type",min_value=0,max_value=3)
    trestbps= st.number_input("resting blood pressure")
    chol= st.number_input("serum cholestoral in mg/dl",)
    fbs= st.number_input("fasting blook sugar > 120 mg/dl",min_value=0,max_value=1)
    restecg= st.number_input("resting electrocardiographic results",min_value=0,max_value=2)
    thalach= st.number_input("maximum heart rate achieved")
    exang= st.number_input("exercise induced angina",min_value=0,max_value=1)
    oldpeak= st.number_input("ST depression induced by exercice relative to rest")
    slope= st.number_input("The slope of the peak exercise ST segment")
    ca= st.number_input("Number of major vessels (0-3) colored by flourosopy",min_value=0,max_value=4)
    thal= st.number_input("Thal",min_value=0,max_value=3)
    diagnosis = ""
    if st.button("Test Result"):
        diagnosis = predicit_heartdisease([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        if(diagnosis==0):
            st.success("This person doesn't have heart disease")
        else:
            st.warning("This person have heart disease")  
    st.snow()        

if __name__ == "__main__":
    main()
    
    