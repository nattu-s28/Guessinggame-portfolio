def guessingame():
        

    import streamlit as st
    import random
    st.sidebar.header("Welcome To Guesssing game")
    page=st.sidebar.radio("Modes",["Rules","User guessing game","machine guessing game"])

    if page=='Rules':
        st.write("""
            *Rules for User Guessing Mode:*
            1. The computer will choose a number within a certain range.
            2. Your Will Try is to guess the number in as few attempts as possible.
            3. After each guess, Computer will be told to you your guess was too high or too low.
            4. Try to achieve the optimal number of attempts!""")
        st.write("""
            *Rules for Machine Guessing Mode:*
            1. You think of a number within a certain range.
            2. The machine will try to guess your number, and you will provide feedback if it's too high or too low.
            3. The machine will use binary search to find your number quickly.
            """)
        st.write("---")


    elif page=='User guessing game':

        # Title
        st.title("User Guessing Game ")

        start_range=st.number_input("Enter starting range:",min_value=0)
        end_range=st.number_input("Enter ending range:",min_value=0)
        if start_range>=end_range:
            st.write("starting range is less than ending range")
        else:
            if'number_to_guess' not in st.session_state:
                st.session_state.number_to_guess = random.randint(start_range,end_range)
                st.session_state.attempts = 0
                st.session_state.game_started=True

        # Instructions
        st.write(f"I'm thinking of a number between {start_range} and {end_range} . Can you guess it?")

        # Input for the guess
        guess = st.number_input("Enter your guess:",min_value=0)

        # Button to submit the guess
        if st.button("Guess"):
            st.session_state.attempts += 1

            # Check if the guess is correct, too low, or too high
            if guess < st.session_state.number_to_guess:
                st.write(" Too low! Try again.")
            elif guess > st.session_state.number_to_guess:
                st.write("Too high! Try again.")
            else:
                st.write(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts!")

    elif page=='machine guessing game':

        if "min_value" not in st.session_state:
            st.session_state.min_value = 1
            st.session_state.max_value = 100
            st.session_state.attempts = 0
            st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
            st.session_state.game_active = False

        # Title
        st.title("Machine Guessing Game")
        st.write("Think of a number within the range you set, and the machine will try to guess it!")

        # Step 1: Get the range from the player
        min_value = st.number_input("Enter the minimum value for the range:",min_value=0)
        max_value = st.number_input("Enter the maximum value for the range:",min_value=0)

        # Start the game
        if st.button("Start Game"):
            if min_value >= max_value:
                st.write("Minimum value must be less than the maximum value.")
            else:
                
                st.session_state.min_value = min_value
                st.session_state.max_value = max_value
                st.session_state.attempts = 1
                st.session_state.machine_guess = (min_value + max_value) // 2
                st.session_state.game_active = True
                st.write(f"The machine's guess is {st.session_state.machine_guess}")

        if st.session_state.game_active:
            feedback = st.selectbox("How is the machine's guess?", ("Correct", "Too Low", "Too High"))

            if st.button("Submit Feedback"):
                if feedback == "Correct":
                    st.write(f"The machine guessed it! The number was {st.session_state.machine_guess}.")
                    st.write(f"Attempts: {st.session_state.attempts}")
                    st.session_state.game_active = False  # End the game
                else:
                    # Update the range based on feedback
                    if feedback == "Too Low":
                        st.session_state.min_value = st.session_state.machine_guess + 1
                    elif feedback == "Too High":
                        st.session_state.max_value = st.session_state.machine_guess - 1

                    # Make a new guess
                    st.session_state.machine_guess = (st.session_state.min_value + st.session_state.max_value) // 2
                    st.session_state.attempts += 1
                    st.write(f"The machine's new guess is {st.session_state.machine_guess}")
