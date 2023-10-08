import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Matplotlib to interactive mode
plt.ion()

st.title('HackUTA 2023')

df = pd.read_csv('https://raw.githubusercontent.com/HackUTA-23/utd-grades/master/raw_data/Fall%202022.csv')
# combine subject, catalog, and section columns into one column
df['course'] = df['Subject'] + ' ' + df['Catalog Nbr'] + ' ' + df['Section']
# remove the subject, catalog, and section columns, since they are not needed anymore
df = df.drop(columns=['Subject', 'Catalog Nbr', 'Section'])
df = df.drop(columns=['P', 'CR', 'NC', 'I', 'W', 'Instructor 1', 'Instructor 2', 'Instructor 3', 'Instructor 4', 'Instructor 5', 'Instructor 6'])
# set the course column as the index
df = df.set_index('course')

# add a dropdown with all the courses
course = st.selectbox('Select a course', df.index)

# Streamlit plot for the selected course
# color the grades different color
color = ['green', 'blue', 'orange', 'red']
# 'A+', 'A', 'A-' should be green, 'B+', 'B', 'B-' should be blue, 'C+', 'C', 'C-' should be orange, 'D+', 'D', 'D-' should be red, 'F' should be black
df.loc[course].plot.bar(color=color)

plt.xticks(rotation=0)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Grade Distribution for ' + course)
st.pyplot(plt)  # Display the Matplotlib figure in Streamlit

# Optional: If you still want to use Matplotlib for more customization, you can use plt functions like below:
# plt.bar(df.columns, df.iloc[0])
# plt.xlabel('Grades')
# plt.ylabel('Number of Students')
# plt.title('Grade Distribution for ' + df.index[0])
# st.pyplot(plt)  # Display the Matplotlib figure in Streamlit

# Optionally, you can disable interactive mode after plotting if you don't plan to create more plots
# plt.ioff()
