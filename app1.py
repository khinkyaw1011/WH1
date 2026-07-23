import streamlit as st
from starter import generate_password
from starter import evaluate_password
from language import lang
# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="🔐 Password Strength Checker",
    page_icon="🔐",
    layout="centered",
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

.title{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:#fff;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.password-box{
    margin-top:15px;
}

.check-item{
    padding:8px;
    border-radius:10px;
    background:#f5f5f5;
    margin-bottom:6px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    language = st.selectbox(
        "Language / 言語",
        ["English", "日本語"]
    )

    text = lang[language]

    st.title(text["settings"])
    st.divider()

    st.subheader(text["password_rules"])

    # min_length = st.slider(
    #     text["minimum_length"],
    #     8,
    #     24,
    #     12
    # )

    require_number = st.checkbox(
        text["require_number"],
        value=True
    )

    require_upper_lower = st.checkbox(
        text["require_upper_lower"],
        value=True
    )

    require_length = st.checkbox(
        text["require_length"],
        value=True
    )

    require_not_common = st.checkbox(
        text["require_not_common"],
        value=True
    )

    require_not_repeated = st.checkbox(
        text["require_not_repeated"],
        value=True
    )

    st.divider()
# -------------------------------
# Main Card
# -------------------------------

st.markdown(
    f'<div class="title">{text["title"]}</div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="subtitle">{text["subtitle"]}</div>',
    unsafe_allow_html=True,
)

st.set_page_config(page_title="Password Checker")


# Initialize session state
if "password" not in st.session_state:
    st.session_state.password = ""

# Generate Password button
if st.button("🎲 Generate Password", use_container_width=True):
    st.session_state.password = generate_password()

# Password input (automatically filled)
password = st.text_input(
    text["password"],
    key="password",
    type="password"
)

# Check Password button
if st.button(text["check"], use_container_width=True):

    if password == "":
        st.warning(text["empty"])
    else:
        result = evaluate_password(password, language)

        st.subheader(text["result"])

        st.write(f"{text['strength']}: **{result['level']}**")
        st.write(f"{text['score']}: **{result['score']}**")

        st.subheader(text["reason"])
        for message in result["messages"]:
            st.write("✅", message)

st.divider()

st.subheader(text["suggestions"])

st.info(text["tips"])



