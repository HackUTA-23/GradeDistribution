import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Matplotlib to interactive mode
plt.ion()

# Define the custom color mapping dictionary
color_map = {
    'A+': 'green', 'A': 'green', 'A-': 'green',
    'B+': 'blue', 'B': 'blue', 'B-': 'blue',
    'C+': 'orange', 'C': 'orange', 'C-': 'orange',
    'D+': 'red', 'D': 'red', 'D-': 'red',
    'F': 'black'
}

st.title('HackUTA 2023')

csv_options = ['Fall 2022', 'Fall 2021', 'Fall 2020', 'Fall 2019', 'Fall 2018', 'Fall 2017']
csv = st.selectbox('Select a semester', csv_options)

df = pd.read_csv('csv/' + csv + '.csv')
# combine subject, catalog, and section columns into one column
df['course'] = df['Subject'] + ' ' + df['Catalog Number'] + ' ' + df['Section']
# remove the subject, catalog, and section columns, since they are not needed anymore
# drop all columns except course and grades
df = df[['course', 'A', 'A-', 'A+', 'B', 'B-', 'B+', 'C', 'C-', 'C+', 'D', 'D-', 'D+', 'F']]
# set the course column as the index
df = df.set_index('course')

# add a dropdown with all the courses
course = st.selectbox('Select a course', df.index)

# Streamlit plot for the selected course
# color the grades using the custom color mapping dictionary
colors = [color_map[grade] for grade in df.loc[course].index]
df.loc[course].plot.bar(color=colors)

plt.xticks(rotation=0)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Grade Distribution for ' + course)
st.pyplot(plt)  # Display the Matplotlib figure in Streamlit

# graph the same data as percentage


# Optionally, you can disable interactive mode after plotting if you don't plan to create more plots
# plt.ioff()
