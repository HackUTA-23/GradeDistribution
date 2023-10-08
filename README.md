# GradeDistribution

## Inspiration 🤯
Our app was born from the realization that many students often feel overwhelmed and uncertain about their choices when it comes to class registration. By offering clear, data-driven insights into grade distributions and GPA trends, our app helps students to make confident, informed decisions about their studies

## What it does 💡
The "Student Grade Distribution Application" offers an intuitive visualization of grade distribution over the years, filterable by courses. Users can not only see the grade spread ranging from A+ to F but can also track the average GPA trend of a course over time. This insight helps students make informed decisions while selecting courses, and faculty can also benefit from understanding grading patterns.

## How we built it 🛠️
We extracted raw online data from UT Dallas and loaded the flat files into Python using Google Colab. The primary data processing was achieved with libraries like numpy and pandas. We then visualized the data using matplotlib.

The web application was constructed using Streamlit, chosen for its compatibility with our Python libraries and its ability to quickly create a functional web app. We incorporated a sidebar in the design for organized content presentation.

View More info on the [Devpost](https://devpost.com/software/grade-information?ref_content=my-projects-tab&ref_feature=my_projects)


# Installation Steps
First clone the repository with 

`git clone https://github.com/HackUTA-23/GradeDistribution.git`

Now install all the required libraries with 

`pip install -r requirements.txt`

Now you may notice a couple of python and ipynb files. Here is the file structure for the python files that we will be working with:

```
Welcome.py
csv/
  | Fall 2017.csv
  | Fall 2018.csv
  | Fall 2019.csv
  | Fall 2020.csv
  | Fall 2021.csv
  | Fall 2022.csv
pages/
  | 1_💯_Grades.py
  | 2_📈_GPA.py
Welcome.py
```

To start the streamlit application and open it on a `localhost` server, start welcome.py with:

`streamlit run Welcome.py`

<img width="1680" alt="Screenshot 2023-10-08 at 10 54 40 AM" src="https://github.com/HackUTA-23/GradeDistribution/assets/9218849/01a0698f-3b02-460a-bc93-0b9d1a40993b">


# How it works
The streamlit application is split into multiple pages depending on whether you want to analyze grades or GPA.

The Welcome page is the starting page of the application and the pages under `pages/` are used for the data querying and visualization.

The CSV files were obtained from UT Dallas raw grade distribution files and we used pandas and matplotlib to filter and visualize the data.


# Contributing and Pull Request 
If interested in contributing to our codebase, feel free to check out the issues tab to report your first issue! Also pull requests must be linked to an issue to keep everything tidy 🧹
