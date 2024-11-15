
import streamlit as st
import guessinggame
from PIL import Image

st.set_page_config(page_title="Nattu`s Portfolio",    layout="centered")


def load_profile_image(image):
    try:
        st.image(image,width=700)
    except FileNotFoundError:
        st.error("Profile image not found.")
        return None

st.sidebar.title("WELCOME")
nav_options = ["Home", "About Me", "Skills", "Projects", "Guessing game", "Contact me"]
nav_choice = st.sidebar.radio("Select a page", nav_options)


if nav_choice == "Home":
    profile_image = load_profile_image("Nattu.jpg")
    st.title("Welcome to My Portfolio")
    st.write("My Name is Natarajan")
    st.write("I`m a First Year B.tech Student ")
    st.write("Here you can find information About my skills, projects, and ways to contact me.")
    st.write("---")

elif nav_choice == "About Me":
    profile_image = load_profile_image("Nattu.jpg")
    st.header("About Me")
    st.write("""
        I am a Student in an Artificial Intelligence and Data Science.
        \nI love Coding And Solving the Problems
        \nWhen I Got the Errors in My Problem Only I saw "ERROR MAKES CLEVER" Then i go to solve that.     
        \n- **Native:** Theni.
        \n- **Location:** KGiSL Institute Of Technology,Coimbatore. 
        \n- **Education:** UG Degree Ongoing in AI&DS.
        \n- **Intrest:** Intrest On Learn Something Worthful in my Free Time
        """)
    st.write("---")

elif nav_choice == "Skills":
    
    st.header("Skills")
    st.write("""
    - **Programming Languages:** Python.
    \n- **Web Development:** HTML,CSS.
    \n- **Frameworks:** Flask,Streamlit.
    \n- **Tools:** Git,Git Hub,Autocad.
             
    """)
    st.progress(85)
    st.write("In all of the above i have Learned 80%")
    profile_image = load_profile_image("images.jpeg")
    st.write("---")

elif nav_choice == "Projects":
    st.header("My Projects")
    st.write("Here are a few projects I’ve worked on:")
    
    # Project 1
    st.subheader("1.BASIC PYTHON PROJECTS: [Click here for source code](https://github.com/nattu-s28/Simple-Python-Projects.git)")
    st.subheader("DESCRIPTION:")
    st.write("Here are the some Python Basic Projects with only Using Python Basic Concepts.")
    st.write("PHONE BOOK PROJECT")
    st.image("Phonebook.png", width=700)
    st.write("---")
    st.write("SNAKES AND LADDERS PROJECT")
    st.image("Snakesandladders.png", width=700)  
    st.write("---")
    st.write("TIC TAC TOE PROJECT")
    st.image("tictactoe.png", width=700)  
    st.write("---")
    
    # Project 2
    st.subheader("2.MARKETING PAGE-Using Flask Framework: [Click here for source code](https://github.com/nattu-s28/Flask.git)")
    st.subheader("DESCRIPTION:")
    st.write("This is the Marketing page constructed by python and its Framework Flask,now its not full filed its on progresss...!")
    st.image("flaskmarket.png", width=700)
    st.write("---")

    # Project 3
    st.subheader("3.GUESSING GAME-Using Streamlit Framework: [Click here for source code](https://github.com/nattu-s28/Flask.git))")
    st.subheader("DESCRIPTION:")
    st.write("This is the Guessing game project using Python And Its Framework Streamlit its ")


elif nav_choice == "Guessing game":
    guessinggame.guessingame()

elif nav_choice == "Contact me":
    st.header("Contact Me")
    st.write("Feel free to reach out to me at:")
    
    st.write("Email: vnadarajan15@gmail.com")
    st.write("Phone no: 9360067866")

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    if st.button("Send"):
        st.write("Message sent! Thank you for reaching out.")
