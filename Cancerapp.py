import streamlit as st

st.title("Welcome to Cancer App")

Age=st.slider("Select Age=",20,80)
Gender=st.slider("Select Gender=",0,1)
BMI=st.slider("Select BMI=",15.003,39.9587)
Smoking=st.slider("Select Smoking=",0,1)
GeneticRisk=st.slider("Select GeneticRisk=",0,2)
PhysicalActivity=st.slider("Select PhysicalActivity=",0.00241005,9.99461)
Alcohollntake=st.slider("Select Alocohollntake=",0.00121467,1.2106)
CancerHistory=st.slider("Select CancerHistory=",0,1)


import pickle
model=pickle.load(open("Cancer.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[Age,Gender,BMI,Smoking,GeneticRisk,PhysicalActivity,Alcohollntake,CancerHistory]])
    st.success("The Cancer is "+ str(prd[0]))

