import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="GPA", page_icon="📈")

st.markdown("# GPA")
st.sidebar.header("GPA")
st.write(
    """This illustrates averaging GPA distribution for a course over the past 5 years. It aggregates the GPA distribution for a specific course over the years which makes it easier to identify grade inflation or deflation in a course."""
)

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

csv_options = ['Fall 2022', 'Fall 2021', 'Fall 2020', 'Fall 2019', 'Fall 2018', 'Fall 2017']

df_2022 = pd.read_csv('csv/' + csv_options[0] + '.csv')
df_2021 = pd.read_csv('csv/' + csv_options[1] + '.csv')
df_2020 = pd.read_csv('csv/' + csv_options[2] + '.csv')
df_2019 = pd.read_csv('csv/' + csv_options[3] + '.csv')
df_2018 = pd.read_csv('csv/' + csv_options[4] + '.csv')
df_2017 = pd.read_csv('csv/' + csv_options[5] + '.csv')

# do the same for all other dataframes
def preprocess_dataframe(df):
    df['course'] = df['Subject'] + ' ' + df['Catalog Number']
    df = df[['course', 'Section', 'A', 'A-', 'A+', 'B', 'B-', 'B+', 'C', 'C-', 'C+', 'D', 'D-', 'D+', 'F']]
    df = df.set_index('course')
    return df

df_2022 = preprocess_dataframe(df_2022)
df_2021 = preprocess_dataframe(df_2021)
df_2020 = preprocess_dataframe(df_2020)
df_2019 = preprocess_dataframe(df_2019)
df_2018 = preprocess_dataframe(df_2018)
df_2017 = preprocess_dataframe(df_2017)

df_2022 = df_2022.groupby('course').mean()
df_2021 = df_2021.groupby('course').mean()
df_2020 = df_2020.groupby('course').mean()
df_2019 = df_2019.groupby('course').mean()
df_2018 = df_2018.groupby('course').mean()
df_2017 = df_2017.groupby('course').mean()

common_courses = set(df_2022.index) & set(df_2021.index) & set(df_2020.index) & set(df_2019.index) & set(df_2018.index) & set(df_2017.index)

# delete all courses not in common_courses

df_2022 = df_2022.loc[common_courses]
df_2021 = df_2021.loc[common_courses]
df_2020 = df_2020.loc[common_courses]
df_2019 = df_2019.loc[common_courses]
df_2018 = df_2018.loc[common_courses]
df_2017 = df_2017.loc[common_courses]

years = [df_2022, df_2021, df_2020, df_2019, df_2018, df_2017]

for df in years:
    df['As'] = df[['A', 'A+', 'A-']].fillna(0).sum(axis=1)
    df['Bs'] = df[['B', 'B+', 'B-']].fillna(0).sum(axis=1)
    df['Cs'] = df[['C', 'C+', 'C-']].fillna(0).sum(axis=1)
    df['Ds'] = df[['D', 'D+', 'D-']].fillna(0).sum(axis=1)
    df['Fs'] = df['F'].fillna(0)

# get percent As, Bs, Cs, Ds, Fs
for df in years:
    sum = df['As'] + df['Bs'] + df['Cs'] + df['Ds'] + df['Fs']
    df['A%'] = round(df['As'] / sum * 100)
    df['B%'] = round(df['Bs'] / sum * 100)
    df['C%'] = round(df['Cs'] / sum * 100)
    df['D%'] = round(df['Ds'] / sum * 100)
    df['F%'] = round(df['Fs'] / sum * 100)

# Now calculate average GPA of each course for each year
for df in years:
    df['GPA'] = (df['As'] * 4 + df['Bs'] * 3 + df['Cs'] * 2 + df['Ds'] * 1 + df['Fs'] * 0) / (df['As'] + df['Bs'] + df['Cs'] + df['Ds'] + df['Fs'])

for df in years:
    df.sort_index(inplace=True)

# plot the year as x-axis and GPA as y-axis with a line plot. get the GPA for ACCT 2301 for years 2017, 2018, 2019, 2020, 2021, 2022 and plot it
gpa_course = st.selectbox('Select a course for GPA', sorted(common_courses))
gpa_2022 = df_2022.loc[gpa_course]['GPA']
gpa_2021 = df_2021.loc[gpa_course]['GPA']
gpa_2020 = df_2020.loc[gpa_course]['GPA']
gpa_2019 = df_2019.loc[gpa_course]['GPA']
gpa_2018 = df_2018.loc[gpa_course]['GPA']
gpa_2017 = df_2017.loc[gpa_course]['GPA']

for df in years:
    # drop all columns except course and grades
    df.drop(columns=['A', 'A-', 'A+', 'B', 'B-', 'B+', 'C', 'C-', 'C+', 'D', 'D-', 'D+', 'F'], inplace=True)

# Create a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Scaled GPA
axes[0].plot([2022, 2021, 2020, 2019, 2018, 2017], [gpa_2022, gpa_2021, gpa_2020, gpa_2019, gpa_2018, gpa_2017])
# Show values on each point rounded to 2 decimal places
for x, y in zip([2022, 2021, 2020, 2019, 2018, 2017], [gpa_2022, gpa_2021, gpa_2020, gpa_2019, gpa_2018, gpa_2017]):
    axes[0].text(x, y, str(round(y, 2)))
axes[0].set_xlabel('Year')
axes[0].set_ylabel('GPA')
axes[0].set_title('GPA for ' + gpa_course + ' Scaled')

# Second subplot: Unscaled GPA
axes[1].plot([2022, 2021, 2020, 2019, 2018, 2017], [gpa_2022, gpa_2021, gpa_2020, gpa_2019, gpa_2018, gpa_2017], color='orange')
# Show values on each point rounded to 2 decimal places
for x, y in zip([2022, 2021, 2020, 2019, 2018, 2017], [gpa_2022, gpa_2021, gpa_2020, gpa_2019, gpa_2018, gpa_2017]):
    axes[1].text(x, y, str(round(y, 2)))
axes[1].set_xlabel('Year')
axes[1].set_ylabel('GPA')
axes[1].set_ylim(0, 4.0)
axes[1].set_title('GPA for ' + gpa_course + ' Unscaled')
# Display the plot in Streamlit
st.pyplot(fig)

# add table with all df_2022 values
st.write('Average # of people who got each score for ' + '['+ gpa_course + ']')
# create a new table with the year as the column and the Grades and GPA as the value for that class
df = pd.DataFrame(columns=['Year', 'As', 'Bs', 'Cs', 'Ds', 'Fs'])
df['Year'] = [2022, 2021, 2020, 2019, 2018, 2017]
df['Year'] = df['Year'].astype('string')
df = df.set_index('Year')

# round to nearest integer
df['As'] = [round(df_2022.loc[gpa_course]['As']), round(df_2021.loc[gpa_course]['As']), round(df_2020.loc[gpa_course]['As']), round(df_2019.loc[gpa_course]['As']), round(df_2018.loc[gpa_course]['As']), round(df_2017.loc[gpa_course]['As'])] 
df['Bs'] = [round(df_2022.loc[gpa_course]['Bs']), round(df_2021.loc[gpa_course]['Bs']), round(df_2020.loc[gpa_course]['Bs']), round(df_2019.loc[gpa_course]['Bs']), round(df_2018.loc[gpa_course]['Bs']), round(df_2017.loc[gpa_course]['Bs'])]
df['Cs'] = [round(df_2022.loc[gpa_course]['Cs']), round(df_2021.loc[gpa_course]['Cs']), round(df_2020.loc[gpa_course]['Cs']), round(df_2019.loc[gpa_course]['Cs']), round(df_2018.loc[gpa_course]['Cs']), round(df_2017.loc[gpa_course]['Cs'])]
df['Ds'] = [round(df_2022.loc[gpa_course]['Ds']), round(df_2021.loc[gpa_course]['Ds']), round(df_2020.loc[gpa_course]['Ds']), round(df_2019.loc[gpa_course]['Ds']), round(df_2018.loc[gpa_course]['Ds']), round(df_2017.loc[gpa_course]['Ds'])]
df['Fs'] = [round(df_2022.loc[gpa_course]['Fs']), round(df_2021.loc[gpa_course]['Fs']), round(df_2020.loc[gpa_course]['Fs']), round(df_2019.loc[gpa_course]['Fs']), round(df_2018.loc[gpa_course]['Fs']), round(df_2017.loc[gpa_course]['Fs'])]
st.write(df)

st.write('Percent grades and average GPA for ' + '['+ gpa_course + ']')
df = pd.DataFrame(columns=['Year', 'A%', 'B%', 'C%', 'D%', 'F%', 'GPA'])
df['Year'] = [2022, 2021, 2020, 2019, 2018, 2017]
df['Year'] = df['Year'].astype('string')
df = df.set_index('Year')

# round to two decimal places
df['A%'] = [df_2022.loc[gpa_course]['A%'], df_2021.loc[gpa_course]['A%'], df_2020.loc[gpa_course]['A%'], df_2019.loc[gpa_course]['A%'], df_2018.loc[gpa_course]['A%'], df_2017.loc[gpa_course]['A%']]
df['B%'] = [df_2022.loc[gpa_course]['B%'], df_2021.loc[gpa_course]['B%'], df_2020.loc[gpa_course]['B%'], df_2019.loc[gpa_course]['B%'], df_2018.loc[gpa_course]['B%'], df_2017.loc[gpa_course]['B%']]
df['C%'] = [df_2022.loc[gpa_course]['C%'], df_2021.loc[gpa_course]['C%'], df_2020.loc[gpa_course]['C%'], df_2019.loc[gpa_course]['C%'], df_2018.loc[gpa_course]['C%'], df_2017.loc[gpa_course]['C%']]
df['D%'] = [df_2022.loc[gpa_course]['D%'], df_2021.loc[gpa_course]['D%'], df_2020.loc[gpa_course]['D%'], df_2019.loc[gpa_course]['D%'], df_2018.loc[gpa_course]['D%'], df_2017.loc[gpa_course]['D%']]
df['F%'] = [df_2022.loc[gpa_course]['F%'], df_2021.loc[gpa_course]['F%'], df_2020.loc[gpa_course]['F%'], df_2019.loc[gpa_course]['F%'], df_2018.loc[gpa_course]['F%'], df_2017.loc[gpa_course]['F%']]
df['GPA'] = [gpa_2022, gpa_2021, gpa_2020, gpa_2019, gpa_2018, gpa_2017]

# round all cells to two decimal places
df['A%'] = df['A%'].round(2)
df['B%'] = df['B%'].round(2)
df['C%'] = df['C%'].round(2)
df['D%'] = df['D%'].round(2)
df['F%'] = df['F%'].round(2)
df['GPA'] = df['GPA'].round(2)

# Format the DataFrame for display in Streamlit
formatted_df = df.style.format({
    'A%': '{:.2f}',
    'B%': '{:.2f}',
    'C%': '{:.2f}',
    'D%': '{:.2f}',
    'F%': '{:.2f}',
    'GPA': '{:.2f}'
})
    


# Display the formatted DataFrame in Streamlit
st.write(formatted_df)
# df = df.round(2)
# st.table(df)










