# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# show the title
st.title('Titanic App by Gaojiong Wu')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plt.style.use('seaborn-v0_8')
axes[0].boxplot(df[df['Pclass'] == 1]['Fare'])
axes[0].set_xlabel('Pclass = 1')
axes[0].set_ylabel('Fare')
axes[0].set_xticklabels(['Fare'])

axes[1].boxplot(df[df['Pclass'] == 2]['Fare'])
axes[1].set_xlabel('Pclass = 2')
axes[1].set_xticklabels(['Fare'])

axes[2].boxplot(df[df['Pclass'] == 3]['Fare'])
axes[2].set_xlabel('Pclass = 3')
axes[2].set_xticklabels(['Fare'])
st.pyplot(plt)
