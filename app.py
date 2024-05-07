import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

#Import data set
pets = pd.read_excel('pets_cleaned.xlsx')

#title
st.title('Long Beach Animal Shelter Outcomes')

#st.dataframe(pets)
st.sidebar.header("Pick an outcome")

selected_outcome = st.sidebar.selectbox('outcomes',sorted(pets['Outcome Type'].unique()))

# Filter data based on selection
filtered_data = pets[pets['Outcome Type'] == selected_outcome]

# Plot
fig, ax = plt.subplots()
sns.countplot(data=filtered_data, x='Animal Type', ax=ax)
ax.set_title(f'Count Plot for Outcome {selected_outcome}')

# Show plot
st.pyplot(fig)


