import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Deep Lab | Hub", page_icon="🟢", layout="wide")

# 2. Visual Theme (Neon Green)
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #39FF14 !important; font-family: 'Courier New', Courier, monospace; text-shadow: 0 0 5px #39FF14; }
    p, .stMarkdown, li { color: #E0E0E0; }
    .stButton>button { background-color: #000000; color: #39FF14; border: 2px solid #39FF14; border-radius: 8px; width: 100%; font-size: 18px; font-weight: bold; transition: 0.3s; box-shadow: 0 0 10px #39FF14; }
    .stButton>button:hover { background-color: #39FF14; color: #000000; box-shadow: 0 0 20px #39FF14; }
    .stTextInput>div>div>input { color: #39FF14; background-color: #111111; border: 1px solid #39FF14; }
    .tl-box { border: 1px solid #39FF14; padding: 20px; border-radius: 10px; background-color: #0a0a0a; text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. ROLE-BASED LOGIN SYSTEM ---
# هنا نحددو شكون Mentor وشكون Student
USERS = {
    "Rayane": {"password": "DeepLabAdmin", "role": "mentor"},
    "Student1": {"password": "Trader2026", "role": "student"},
    "Student2": {"password": "Trader2027", "role": "student"}
}

def check_password():
    def password_entered():
        user = st.session_state["username"]
        passwd = st.session_state["password"]
        
        if user in USERS and USERS[user]["password"] == passwd:
            st.session_state["password_correct"] = True
            st.session_state["role"] = USERS[user]["role"] # نسجلو دور المستخدم
            st.session_state["current_user"] = user        # نسجلو اسمو
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center;'>🟢 SECURE LOGIN</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 style='text-align: center;'>🟢 SECURE LOGIN</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered)
            st.error("❌ Access Denied: Incorrect credentials.")
        return False
    else:
        return True

# --- 4. MAIN DASHBOARDS (Mentor vs Student) ---
if check_password():
    user_role = st.session_state["role"]
    user_name = st.session_state["current_user"]
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(f"🟢 THE DEEP LAB | {user_role.upper()} VIEW")
        st.markdown(f"Welcome back, **{user_name}**.")
    with col2:
        if st.button("Logout"):
            st.session_state.clear()
            st.experimental_rerun()
            
    st.divider()

    # ==========================================
    # واجهة الـ MENTOR (أنت)
    # ==========================================
    if user_role == "mentor":
        st.subheader("🛠️ Admin Dashboard")
        st.write("As a mentor, you can see the performance of all students and upload master data.")
        
        # مثال: مكان رفع ملفات TradeLocker
        st.markdown("### 📥 Upload Student Data (TradeLocker CSV)")
        uploaded_file = st.file_uploader("Upload Trade history", type=['csv'])
        if uploaded_file is not None:
            st.success("File uploaded and assigned successfully!")
            
        # تقدر تزيد هنا إحصائيات عامة تاع كل الطلبة

    # ==========================================
    # واجهة الـ STUDENT (الطلبة)
    # ==========================================
    elif user_role == "student":
        st.subheader("📈 My Portfolio")
        st.write("Here you can track your personal performance and access trading tools.")
        
        # الطالب يشوف غير إحصائياتو الخاصة
        st.markdown("""
        <div class="tl-box">
            <h3 style="color: #E0E0E0;">Your TradeLocker Stats</h3>
            <p>Win Rate: --% | Drawdown: --% | Profit: $--</p>
        </div>
        """, unsafe_allow_html=True)
