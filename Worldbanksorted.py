import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

df=pd.read_csv('World_Bank_India',skiprows=4)
df_1=df.T
r=['Indicator Name','2010','2011','2012','2013','2014','2015','2016','2017','2018']
df_2=df_1.loc[r,[28,31,25]]
new_header=df_2.iloc[0]
df_2.columns=new_header
df_3=df_2.drop('Indicator Name')
df_3
