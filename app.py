import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Deep Lab Terminal", page_icon="🟢", layout="centered")

# 2. تصميم Neo-Minimalist (Clean, Sharp, High-End)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@300;400&display=swap');

    /* خلفية سوداء عميقة */
    .stApp { background-color: #050505; }

    /* تنسيق النصوص - Inter للجمالية و JetBrains للـ Quant vibe */
    h1, h2, h3 { 
        font-family: 'Inter', sans-serif; 
        color: #FFFFFF !important; 
        letter-spacing: -1px;
        text-align: center;
        font-weight: 600;
    }
    
    .neo-text {
        color: #39FF14;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.4); /* Glow خفيف بزاف */
        font-family: 'JetBrains Mono', monospace;
    }

    p { color: #888888; text-align: center; font-family: 'Inter', sans-serif; }

    /* الأزرار Neo-Style (بدون Shadow ثقيل) */
    .stButton>button { 
        background-color: transparent; 
        color: #39FF14; 
        border: 1px solid rgba(57, 255, 20, 0.3); 
        border-radius: 4px; 
        width: 100%; 
        padding: 12px; 
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stButton>button:hover { 
        background-color: rgba(57, 255, 20, 0.05);
        border: 1px solid #39FF14;
        color: #39FF14;
        box-shadow: 0 0 15px rgba(57, 255, 20, 0.2); /* نيون خفيف جدا عند اللمس */
        transform: translateY(-2px);
    }

    /* تنسيق خانات الإدخال - احترافية */
    input { 
        background-color: #0A0A0A !important; 
        color: #FFFFFF !important; 
        border: 1px solid #222222 !important; 
        border-radius: 4px !important;
        font-family: 'Inter', sans-serif !important;
    }
    input:focus {
        border-color: #39FF14 !important;
        box-shadow: none !important;
    }

    /* أنيميشين الانتقال */
    .fade-in {
        animation: fadeIn 0.8s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* إخفاء شريط الـ Streamlit اللي فوق */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. المنطق الخلفي (Auth Logic) ---
if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "users_db" not in st.session_state:
    st.session_state.users_db = {"Rayane": "DeepLabAdmin"}

# --- 4. الواجهات الاحترافية ---

# المرحلة 1: Welcome Screen
if st.session_state.step == "welcome":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1>THE <span class="neo-text">DEEP</span> LAB</h1>', unsafe_allow_html=True)
    st.markdown("<p>Proprietary Quantitative Research & Execution Terminal</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INITIALIZE TERMINAL"):
            st.session_state.step = "auth_choice"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# المرحلة 2: Auth Choice
elif st.session_state.step == "auth_choice":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h2>SYSTEM AUTHENTICATION</h2>", unsafe_allow_html=True)
    st.markdown("<p>Select your access protocol</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("LOGIN"):
            st.session_state.step = "login"
            st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("SIGN UP"):
            st.session_state.step = "signup"
            st.rerun()
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("RETURN", type="secondary"):
            st.session_state.step = "welcome"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# المرحلة 3: Login
elif st.session_state.step == "login":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h2>ACCESS GATE</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("IDENTIFIER")
        pwd = st.text_input("ENCRYPTED KEY", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("AUTHORIZE"):
            if user in st.session_state.users_db and st.session_state.users_db[user] == pwd:
                st.session_state.step = "dashboard"
                st.session_state.logged_user = user
                st.rerun()
            else:
                st.error("Invalid Access Key.")
        if st.button("BACK"):
            st.session_state.step = "auth_choice"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# المرحلة 4: Sign Up
elif st.session_state.step == "signup":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h2>NEW PROTOCOL</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        new_user = st.text_input("NEW IDENTIFIER")
        new_pwd = st.text_input("NEW ENCRYPTED KEY", type="password")
        if st.button("CREATE PROFILE"):
            if new_user and new_pwd:
                st.session_state.users_db[new_user] = new_pwd
                st.success("Profile Created. Return to Login.")
                st.session_state.step = "login"
                st.rerun()
        if st.button("BACK"):
            st.session_state.step = "auth_choice"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# المرحلة 5: Dashboard
elif st.session_state.step == "dashboard":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown(f"<h2>TERMINAL <span class='neo-text'>ONLINE</span></h2>", unsafe_allow_html=True)
    st.markdown(f"<p>Welcome, {st.session_state.logged_user}. System status: Stable.</p>", unsafe_allow_html=True)
    st.divider()
    # هنا نحطو الـ Analytics والـ TradeLocker Tracker
    if st.button("TERMINATE SESSION"):
        st.session_state.step = "welcome"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
