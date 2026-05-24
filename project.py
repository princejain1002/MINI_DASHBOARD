import streamlit as st
import math
import random

st.title("MINI DASHBOARD")
st.write("Choose the activity of your choice")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🧮Calculator",
    "📖Diary",
    "🎲Game",
    "⏰Clock",
    "📃To-DO-List",
    "🔑Password generator",
    "📑UNIT Converter"
])

# tabs for dashboard

with tab1:

    st.header("🧮 Scientific Calculator")

    # Functions for calc
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def power(a, b):
        return a ** b

    def root(x):
        return math.sqrt(x)

    def sine(x):
        return math.sin(math.radians(x))

    def cosine(x):
        return math.cos(math.radians(x))

    def tangent(x):
        return math.tan(math.radians(x))

    def logarithm(x):
        return math.log10(x)

    
    operation = st.selectbox(
        "Choose Operation",
        [
            "+ Addition",
            "- Subtraction",
            "× Multiplication",
            "÷ Division",
            "^ Power",
            "√ Square Root",
            "sin",
            "cos",
            "tan",
            "log"
        ]
    )

    # User input
    num1 = st.text_input("Enter First Number")

    # Second number only for some operations
    if operation in [
        "+ Addition",
        "- Subtraction",
        "× Multiplication",
        "÷ Division",
        "^ Power"
    ]:
        num2 = st.text_input("Enter Second Number")

    # Calculate button
    if st.button("Calculate"):

        try:

            num1 = float(num1)

            if operation in [
                "+ Addition",
                "- Subtraction",
                "× Multiplication",
                "÷ Division",
                "^ Power"
            ]:
                num2 = float(num2)

            # Calculations
            if operation == "+ Addition":
                result = add(num1, num2)

            elif operation == "- Subtraction":
                result = subtract(num1, num2)

            elif operation == "× Multiplication":
                result = multiply(num1, num2)

            elif operation == "÷ Division":
                result = divide(num1, num2)

            elif operation == "^ Power":
                result = power(num1, num2)

            elif operation == "√ Square Root":
                result = root(num1)

            elif operation == "sin":
                result = sine(num1)

            elif operation == "cos":
                result = cosine(num1)

            elif operation == "tan":
                result = tangent(num1)

            elif operation == "log":
                result = logarithm(num1)

            st.success(f"Result = {result}")

        except:
            st.error("Please enter valid numbers")

#Diary tab

with tab2:

    st.header("📖 Secret Diary")
    PASSWORD = "1234"

    # Password input
    password = st.text_input(
        "Enter Password",
        type="password"
    )

    # Check password
    if password == PASSWORD:
        st.success("Access Granted 🔓")
        # Write diary
        diary_text = st.text_area(
            "Dear Diary....."
        )

        if st.button("💾 Save Note"):

            file = open("diary.txt", "a")

            file.write(diary_text + "\n")
            file.write("-------------------\n")
            file.close()
            st.success("Your Diary is Saved")
        if st.button("📂 Open Diary"):

            try:

                file = open("diary.txt", "r")

                content = file.read()

                file.close()

                st.text_area(
                    "Your Diary",
                    content,
                    height=300
                )

            except:

                st.error("No content Found")

       #edit option

        st.subheader("✏️Edit Diary")
        try:

            file = open("diary.txt", "r")
            old_content = file.read()
            file.close()

        except:
            old_content = ""

        edited_content = st.text_area(
            "Edit Here",
            old_content,
            height=300
        )

        if st.button("✅ Save Edited Notes"):

            file = open("diary.txt", "w")

            file.write(edited_content)

            file.close()

            st.success("Diary Updated")

        if st.button("🗑️ Delete Diary"):

            file = open("diary.txt", "w")

            file.write("")

            file.close()

            st.warning("Diary Deleted")

    # Wrong password
    elif password != "":

        st.error("Wrong Password ❌")
#CLOCK
# CLOCK
with tab4:

    import time
    from datetime import datetime

    st.header("⏰ Digital Clock")

    # Button
    if st.button("Show Clock"):

        # Empty placeholder
        clock = st.empty()

        # Show clock for 5 seconds
        for i in range(5):

            current_time = datetime.now().strftime("%H:%M:%S")

            clock.markdown(
                f"""
                <div style="
                    background: linear-gradient(#0e6ba8,#0a2472,#001c55);
                    padding: 40px;
                    border-radius: 20px;
                    text-align: center;
                    color: #ccdbdc;
                    font-size: 60px;
                    font-weight: bold;
                    box-shadow: 0px 0px 20px #888;
                ">
                    {current_time}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(1)

        # Remove clock after 5 sec
        clock.empty()
    #to do listt
with tab5:

    st.header("📃 To-Do List")

    file_name = "tasks.txt"
    task = st.text_input("Enter New Task")

    if st.button("➕ Add Task"):

        if task != "":
            with open(file_name, "a") as file:
                file.write(task + "\n")
            st.success("Task Added")
        else:
            st.warning("Please Enter Task")
    st.subheader("📋 Your Tasks")
    try:
        with open(file_name, "r") as file:

            tasks = file.readlines()
        if tasks:

            count = 1
            for task in tasks:
                st.write(f"{count}. {task}")
                count = count + 1
        else:
            st.info("No Tasks Yet")
    except:

        st.info("No Tasks Found")
    st.subheader("🗑️ Delete Task")

    delete_task = st.number_input(
        "Enter Task Number",
        min_value=1,
        step=1
    )
    if st.button("Delete Task"):
        try:
            with open(file_name, "r") as file:
                tasks = file.readlines()
            tasks.pop(delete_task - 1)
            with open(file_name, "w") as file:
                file.writelines(tasks)
            st.success("Task Deleted")
        except:
            st.error("Invalid Task Number")
    st.subheader("📋 Your Tasks")
    try:
        with open(file_name, "r") as file:

            tasks = file.readlines()
        if tasks:

            count = 1
            for task in tasks:
                st.write(f"{count}. {task}")
                count = count + 1
        else:
            st.info("No Tasks Yet")
    except:

        st.info("No Tasks Found")
    if st.button("❌ Clear All Task"):

        with open(file_name, "w") as file:

            file.write("")
        st.warning("All Tasks Cleared")

# PASSWORD generator
with tab6:

    st.header("🔑 Password Generator")
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@#$%&*!"

    all_characters = letters + numbers + symbols
    length = st.slider(
        "Select Password Length",
        4,
        20,
        8
    )
    if st.button("Generate Password"):
        password = ""
        for i in range(length):

            password += random.choice(all_characters)

        st.success(f"Generated Password: {password}")
# UNIT convertor
# UNIT CONVERTER

with tab7:

    st.header("📑 Unit Converter")

    # Dropdown menu
    conversion = st.selectbox(
        "Choose Conversion",
        [
            "Kilometer to Meter",
            "Meter to Kilometer",
            "Kilogram to Gram",
            "Gram to Kilogram",
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius"
        ]
    )

    value_str = st.text_input("Enter Value")

    if st.button("Convert"):

        try:
            value = float(value_str) 

            # Kilometer Meter
            if conversion == "Kilometer to Meter":
                result = value * 1000
                st.success(f"{value} km = {result} m")

            # Meter Kilometer
            elif conversion == "Meter to Kilometer":
                result = value / 1000
                st.success(f"{value} m = {result} km")

            # Kilogram Gram
            elif conversion == "Kilogram to Gram":
                result = value * 1000
                st.success(f"{value} kg = {result} g")

            # Gram Kilogram
            elif conversion == "Gram to Kilogram":
                result = value / 1000
                st.success(f"{value} g = {result} kg")

            # Celsius Fahrenheit
            elif conversion == "Celsius to Fahrenheit":
                result = (value * 9/5) + 32
                st.success(f"{value}°C = {result}°F")

            # Fahrenheit Celsius
            elif conversion == "Fahrenheit to Celsius":
                result = (value - 32) * 5/9
                st.success(f"{value}°F = {result}°C")

        except:
            st.error("Please enter a valid numeric value")
#games
with tab3:

    st.header("🎲 Number Guessing Game")
    st.write("Guess a number between 1 and 100")
    if "secret_number" not in st.session_state:

        st.session_state.secret_number = random.randint(1, 3)
    # User input
    guess = st.text_input("Enter Your Guess")

    # Check button
    if st.button("Check Guess"):

        try:
            guess = int(guess)
            if guess == st.session_state.secret_number:
                st.success("🎉 Correct Guess")
                st.balloons()
            
                st.session_state.secret_number = random.randint(1, 3)

            # Too high
            elif guess > st.session_state.secret_number:

                st.warning("📈 Too High!")
            # Too low
            else:
                st.warning("📉 Too Low!")
        except:

            st.error("⚠️ Please Enter Valid Number")