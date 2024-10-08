import streamlit as st
from random import randint

# Used streamlit session state to store the random number so it doesn't reset on rerun
if 'randomNumber' not in st.session_state:
    st.session_state.randomNumber = randint(1, 10)

randomNumber = st.session_state.randomNumber

st.title("Shahmir Number Guessing Game!")
st.write(" ")

# Get the user's guess
userGuess = st.number_input("Guess the number between 1-10", step=1, min_value=1, max_value=10)

# Check the user's guess when they press the button
if st.button("Check"):
    st.write(" ")
    if userGuess > randomNumber:
        st.warning("Your guess is greater than the actual number.")
    elif userGuess < randomNumber:
        st.warning("Your guess is less than the actual number.")
    else:
        st.success(f"Congratulations! You guessed the right number, the number was {randomNumber}.")
else:
    st.write("Enter a number to play.")

