import streamlit as st 
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as  plt
import plotly
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
#importing data
data = pd.read_csv("Salary_data.csv",error_bad_lines=False)
#Title to the web app
st.title("Salary Predictor")
#Creating linear regression model
x = np.array(data['YearsExperience']).reshape(-1,1)
lr = LinearRegression() 
#Fitting the model
lr.fit(x,np.array(data['Salary']))
#Adding radioboxes to navigation bar 
nav = st.sidebar.radio("About us",["Home","Prediction","Contribute"])
#Adding Functionalities to these radioboxes
if nav=='Home':
    st.image("data_for_app//Research-img.png",width = 500)
    if st.checkbox("Show Dataset"):
        st.table(data)
        st.header("Graph of the existing dataset")  
    val = st.slider("Filter data using years",min_value=0,max_value=20)
    data = data.loc[data['YearsExperience']>=val]
    plt.figure(figsize=(10,5))
    plt.scatter(data["YearsExperience"],data["Salary"])
    plt.ylim(0)
    plt.xlabel("Years of Experience")
    plt.tight_layout()
    st.pyplot()
if nav=='Prediction':
    st.image("data_for_app//salary.jpg",width = 500)
    st.header("Know Your Salary")
    val = st.number_input("Enter years of experience",0.00,20.00,step=0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    #AAdding the button for prediction
    if st.button("Predict"):
        st.success(f"Your predicted salary is: {round(pred)}")
if nav=='Contribute':
    st.image("data_for_app//contribute.jpeg",width = 500)
    st.header("Contribute to the database")
    ex = st.number_input("Enter years of experience",0.00,20.00,step=0.25)
    sal_yearly = st.number_input("Enter yearly salary",0.00,1000000.00,step=1000.00)
    if st.button("Submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal_yearly]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data_for_app//Salary_data.csv",mode='a',header=False,index=False)
        st.success("Thanks For your contribution")