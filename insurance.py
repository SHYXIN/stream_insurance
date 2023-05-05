import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("导航", ["简介", "预测保险费"])
df = pd.read_csv('insurance.csv')

if nav == "简介":
    st.title("健康保险保费预测器")
    st.text(" ")
    st.text(" ")
    st.image('health_insurance.jpeg', width=600)

df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)

df.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)

df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

x = df.drop(columns='charges', axis=1)

y = df['charges']

rfr = RandomForestRegressor()

rfr.fit(x, y)

if nav == "预测保险费":
    st.title("输入特征")

    age = st.number_input("年龄: ", step=1, min_value=0)

    sex = st.radio("性别", ("男", "女"))

    if sex == "男":
        s = 0
    if sex == "女":
        s = 1
    bmi = st.number_input("BMI: ", min_value=0)

    children = st.number_input("孩子的数量: ", step=1, min_value=0)

    smoke = st.radio("是否吸烟", ("是", "否"))

    if smoke == "是":
        sm = 0
    if smoke == "否":
        sm = 1

    region = st.selectbox('区域', ('东南片区', '西南片区', '东北片区', '西北片区'))

    if region == "东南片区":
        reg = 0
    if region == "西南片区":
        reg = 1
    if region == "东北片区":
        reg = 2
    if region == "西北片区":
        reg = 3

    if st.button("开始预测"):
        st.subheader("预测的保险费用")
        st.text(rfr.predict([[age, s, bmi, children, sm, reg]]))
