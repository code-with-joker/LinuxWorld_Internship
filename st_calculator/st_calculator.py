import streamlit as st

st.set_page_config(page_title="Smart Multi-Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Smart Multi-Calculator (Streamlit Version)")
st.write("A simple and attractive calculator with extra conversion features.")

# SELECT MAIN CATEGORY

choice = st.selectbox(
    "Choose Calculator Type:",
    [
        "Arithmetic Calculator",
        "Area of Square",
        "Temperature Conversion",
        "Weight Conversion",
    ]
)

# 1. ARITHMETIC CALCULATOR
if choice == "Arithmetic Calculator":
    st.subheader("Arithmetic Operations")

    num1 = st.number_input("Enter First Number")
    num2 = st.number_input("Enter Second Number")

    operator = st.selectbox("Choose Operation", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        if operator == "+":
            st.success(f"Result: {num1 + num2}")

        elif operator == "-":
            st.success(f"Result: {num1 - num2}")

        elif operator == "*":
            st.success(f"Result: {num1 * num2}")

        elif operator == "/":
            if num2 == 0:
                st.error("Cannot divide by zero")
            else:
                st.success(f"Result: {num1 / num2}")


# 2. AREA OF SQUARE
elif choice == "Area of Square":
    st.subheader("Area of Square Calculator")

    side = st.number_input("Enter Side of Square")

    if st.button("Find Area"):
        st.success(f"Area of Square: {side * side}")


# 3. TEMPERATURE CONVERSION
elif choice == "Temperature Conversion":
    st.subheader("Temperature Converter")

    choose = st.radio("Choose Conversion Type:", ["Celsius -> Fahrenheit", "Fahrenheit -> Celsius"])

    temp = st.number_input("Enter Temperature")

    if st.button("Convert"):
        if choose == "Celsius -> Fahrenheit":
            result = (temp * 9/5) + 32
            st.success(f"{temp}°C = {result}°F")

        else:
            result = (temp - 32) * 5/9
            st.success(f"{temp}°F = {result}°C")


# 4. WEIGHT CONVERSION
elif choice == "Weight Conversion":
    st.subheader("Weight Converter")

    choose = st.radio("Choose Conversion Type:", ["KG -> Gram", "Gram -> KG"])

    weight = st.number_input("Enter Weight")

    if st.button("Convert"):
        if choose == "KG -> Gram":
            st.success(f"{weight} KG = {weight * 1000} Gram")

        else:
            st.success(f"{weight} Gram = {weight / 1000} KG")
