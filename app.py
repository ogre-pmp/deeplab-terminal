import streamlit as st

# 1. إعدادات الصفحة والثيم النيون
st.set_page_config(page_title="Deep Lab | Terminal", page_icon="🟢", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #39FF14 !important; font-family: 'Courier New', Courier, monospace; text-shadow: 0 0 10px #39FF14; text-align: center; }
    p { color: #E0E0E0; text-align: center; }
    .stButton>button { 
        background-color: #000000; color: #39FF14; border: 2px solid #39FF14; 
        border-radius: 10px; width: 100%; padding: 10px; font-weight: bold;
        box-shadow: 0 0 10px #39FF14; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #39FF14; color: #000000; box-shadow: 0 0 20px #39FF14; }
    input { background-color: #111111 !important; color: #39FF14 !important; border: 1px solid #39FF14 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. إدارة الحالة (Session State) ---
if "step" not in st.session_state:
    st.session_state.step = "welcome"  # البداية من صفحة الترحيب
if "users_db" not in st.session_state:
    # قاعدة بيانات مؤقتة (في الحقيقة نحتاجو Database بصح هادي للمثال)
    st.session_state.users_db = {"Rayane": "DeepLabAdmin"} 

# --- 3. الواجهات ---

# المرحلة 1: صفحة الـ Access Terminal
if st.session_state.step == "welcome":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("THE DEEP LAB")
    st.markdown("### QUANTITATIVE TRADING TERMINAL")
    st.markdown("<p>Enter the matrix to access proprietary trading tools and analytics.</p>", unsafe_allow_html=True)
    if st.button("ACCESS TERMINAL"):
        st.session_state.step = "auth_choice"
        st.rerun()

# المرحلة 2: اختيار Login أو Sign Up
elif st.session_state.step == "auth_choice":
    st.title("AUTHENTICATION")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("LOGIN"):
            st.session_state.step = "login"
            st.rerun()
    with col2:
        if st.button("SIGN UP"):
            st.session_state.step = "signup"
            st.rerun()
    if st.button("← Back"):
        st.session_state.step = "welcome"
        st.rerun()

# المرحلة 3: صفحة الـ LOGIN
elif st.session_state.step == "login":
    st.title("LOGIN")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("SUBMIT"):
        if user in st.session_state.users_db and st.session_state.users_db[user] == pwd:
            st.success(f"Welcome back {user}!")
            st.session_state.step = "dashboard"
            st.rerun()
        else:
            st.error("Invalid credentials!")
    if st.button("← Back"):
        st.session_state.step = "auth_choice"
        st.rerun()

# المرحلة 4: صفحة الـ SIGN UP
elif st.session_state.step == "signup":
    st.title("CREATE ACCOUNT")
    new_user = st.text_input("Choose Username")
    new_pwd = st.text_input("Create Password", type="password")
    confirm_pwd = st.text_input("Confirm Password", type="password")
    
    if st.button("REGISTER"):
        if new_user in st.session_state.users_db:
            st.error("Username already exists!")
        elif new_pwd != confirm_pwd:
            st.error("Passwords do not match!")
        elif new_user and new_pwd:
            st.session_state.users_db[new_user] = new_pwd
            st.success("Account created! Please login.")
            st.session_state.step = "login"
            st.rerun()
    if st.button("← Back"):
        st.session_state.step = "auth_choice"
        st.rerun()

# المرحلة 5: الـ Dashboard (بعد الدخول)
elif st.session_state.step == "dashboard":
    st.title("🟢 TERMINAL ACTIVE")
    st.markdown(f"### Hello, {st.session_state.get('username', 'Trader')}")
    st.write("Your trading analytics and PMP tools are now unlocked.")
    if st.button("LOGOUT"):
        st.session_state.step = "welcome"
        st.rerun()
