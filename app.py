import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Deep Lab | Terminal", page_icon="🟢", layout="centered")

# 2. Ultra-Professional Neo-Dark CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=JetBrains+Mono:wght@300&display=swap');

    /* Deep Black Canvas */
    .stApp { background-color: #050505; }

    /* Typography */
    h1, h2, h3 { 
        font-family: 'Inter', sans-serif; 
        color: #FFFFFF !important; 
        font-weight: 700;
        letter-spacing: -1.5px;
        text-align: center;
    }
    
    .neo-accent {
        color: #39FF14;
        text-shadow: 0 0 10px rgba(57, 255, 20, 0.3);
        font-family: 'JetBrains Mono', monospace;
    }

    p { color: #666666; text-align: center; font-family: 'Inter', sans-serif; font-size: 0.9rem; }

    /* Professional Neo-Buttons */
    .stButton>button { 
        background-color: transparent; 
        color: #39FF14; 
        border: 1px solid rgba(57, 255, 20, 0.2); 
        border-radius: 2px; 
        width: 100%; 
        padding: 10px; 
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.5s ease;
    }
    
    .stButton>button:hover { 
        background-color: rgba(57, 255, 20, 0.02);
        border: 1px solid #39FF14;
        box-shadow: 0 0 20px rgba(57, 255, 20, 0.15);
        color: #39FF14;
    }

    /* Clean Input Fields */
    input { 
        background-color: #0A0A0A !important; 
        color: #FFFFFF !important; 
        border: 1px solid #1A1A1A !important; 
        border-radius: 2px !important;
        font-family: 'Inter', sans-serif !important;
    }
    input:focus {
        border-color: #39FF14 !important;
        box-shadow: none !important;
    }

    /* Minimalist Divider */
    hr { border: 0; border-top: 1px solid #111; margin: 30px 0; }

    /* Sidebar Clean-up */
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #111; }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. Auth Logic ---
if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "users_db" not in st.session_state:
    st.session_state.users_db = {"Rayane": "DeepLabAdmin"}

# --- 4. Navigation Control ---
def navigate_to(step):
    st.session_state.step = step
    st.rerun()

# --- 5. Professional Interfaces ---

# Welcome: Access Terminal Gate
if st.session_state.step == "welcome":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1>THE <span class="neo-accent">DEEP</span> LAB</h1>', unsafe_allow_html=True)
    st.markdown("<p>Proprietary Quantitative Strategy Terminal</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INITIALIZE TERMINAL"):
            navigate_to("auth_choice")

# Auth Choice: Login or Sign Up
elif st.session_state.step == "auth_choice":
    st.markdown("<h2>SYSTEM AUTH</h2>", unsafe_allow_html=True)
    st.markdown("<p>Identification Required</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("LOGIN PROTOCOL"):
            navigate_to("login")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("SIGN UP PROTOCOL"):
            navigate_to("signup")
        st.markdown("<br><hr>", unsafe_allow_html=True)
        if st.button("RETURN"):
            navigate_to("welcome")

# Login Interface
elif st.session_state.step == "login":
    st.markdown("<h2>ACCESS GATE</h2>", unsafe_allow_html=True)
    st.markdown("<p>Enter Encryption Key</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("IDENTIFIER")
        pwd = st.text_input("KEY", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("AUTHORIZE"):
            if user in st.session_state.users_db and st.session_state.users_db[user] == pwd:
                st.session_state.logged_user = user
                navigate_to("dashboard")
            else:
                st.error("Authentication Failed.")
        if st.button("BACK"):
            navigate_to("auth_choice")

# Sign Up Interface
elif st.session_state.step == "signup":
    st.markdown("<h2>NEW PROTOCOL</h2>", unsafe_allow_html=True)
    st.markdown("<p>Register New Identity</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        new_user = st.text_input("NEW IDENTIFIER")
        new_pwd = st.text_
