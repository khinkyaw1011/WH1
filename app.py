import streamlit as st
from starter import evaluate_password, generate_password
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
html, body, [class*="st-"] {
  font-family: "Montserrat", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}

.stApp {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    
}
/* Button */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Password Checker")
st.title("🔐B2 Password Checker")

# Initialize session state
if "password" not in st.session_state:
    st.session_state.password = ""

# Generate Password button
if st.button("Generate Password"):
    st.session_state.password = generate_password()

# Password input (automatically filled)
password = st.text_input(
    "Enter your password",
    key="password",
    type="password"
)

# Check Password button
if st.button("Check Password"):

    if password == "":
        st.warning("Please enter a password.")
    else:
        result = evaluate_password(password)

        st.subheader("Result")
        st.write(f"Strength: **{result['level']}**")
        st.write(f"Score: **{result['score']}**")

        st.subheader("Reason")
        for message in result["messages"]:
            st.write("✅", message)


