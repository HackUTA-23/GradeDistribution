import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.write("# Welcome to Grade Information! 👋")

st.markdown(
    """
    ## Inspiration 🤯
    Our app was born from the realization that many students often feel overwhelmed and uncertain about their choices when it comes to class registration. By offering clear, data-driven insights into grade distributions and GPA trends, our app helps students to make confident, informed decisions about their studies 

    ## What it does 💡
    The "Student Grade Distribution Application" offers an intuitive visualization of grade distribution over the years, filterable by courses. Users can not only see the grade spread ranging from A+ to F but can also track the average GPA trend of a course over time. This insight helps students make informed decisions while selecting courses, and faculty can also benefit from understanding grading patterns.

    ## How we built it 🛠️
    We extracted raw online data from UT Dallas and loaded the flat files into Python using Google Colab. The primary data processing was achieved with libraries like numpy and pandas. We then visualized the data using matplotlib.

    The web application was constructed using Streamlit, chosen for its compatibility with our Python libraries and its ability to quickly create a functional web app. We incorporated a sidebar in the design for organized content presentation.
"""
)