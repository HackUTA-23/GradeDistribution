import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Matplotlib to interactive mode
plt.ion()

st.title('Hackuta 2023')

df = pd.read_csv('utd-grades/raw_data/Fall 2022.csv')
# combine subject, catalog, and section columns into one column
df['course'] = df['Subject'] + ' ' + df['Catalog Nbr'] + ' ' + df['Section']
# remove the subject, catalog, and section columns, since they are not needed anymore
df = df.drop(columns=['Subject', 'Catalog Nbr', 'Section'])
df = df.drop(columns=['P', 'CR', 'NC', 'I', 'W', 'Instructor 1', 'Instructor 2', 'Instructor 3', 'Instructor 4', 'Instructor 5', 'Instructor 6'])
# set the course column as the index
df = df.set_index('course')

# Streamlit plot
st.write("## Grade Distribution for " + df.index[0])
st.bar_chart(df.iloc[0])

# Optional: If you still want to use Matplotlib for more customization, you can use plt functions like below:
# plt.bar(df.columns, df.iloc[0])
# plt.xlabel('Grades')
# plt.ylabel('Number of Students')
# plt.title('Grade Distribution for ' + df.index[0])
# st.pyplot(plt)  # Display the Matplotlib figure in Streamlit

# Optionally, you can disable interactive mode after plotting if you don't plan to create more plots
# plt.ioff()
