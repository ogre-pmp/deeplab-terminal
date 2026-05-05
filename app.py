import streamlit as st
import hashlib

# ==========================================
# 1. SYSTEM CONFIGURATION & UI INJECTION
# ==========================================
def init_system():
    st.set_page_config(page_title="Deep Lab | Terminal", page_icon="🟢", layout="centered")
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');
        
        :root {
            --bg-color: #030303;
            --accent: #39FF14;
            --surface: #0A0A0A;
            --text-main: #FFFFFF;
            --text-muted: #888888;
        }
        
        .stApp { background-color: var(--bg-color); }
        
        h1, h2, h3 { 
            font-family: 'Inter', sans-serif; 
            color: var(--text-main) !important; 
            font-weight: 800;
            letter-spacing: -1px;
            text-align: center;
        }
        
        .accent-text { color: var(--accent); font-family: 'JetBrains Mono', monospace; }
        
        p { color: var(--text-muted); text-align: center; font-family: 'Inter', sans-serif; font-size: 0.95rem; }
        
        .stButton>button { 
            background-color: transparent; 
            color: var(--accent); 
            border: 1px solid rgba(57, 255, 20, 0.3); 
            border-radius: 2px; 
            width: 100%; 
            padding: 12px; 
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .stButton>button:hover { 
            background-color: var(--accent);
            color: var(--bg-color);
            border-color: var(--accent);
            box-shadow: 0 0 15px rgba(57, 255, 20, 0.2);
        }
        
        input { 
            background-color: var(--surface) !important; 
            color: var(--text-main) !important; 
            border: 1px solid #1A1A1A !important; 
            border-radius: 2px !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.9rem !important;
        }
        input:focus { border-color: var(--accent) !important; box-shadow: none !important; }
        hr { border-color: #111; margin: 2rem 0; }
        header, footer { visibility: hidden; }
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SECURITY & AUTHENTICATION MODULE
# ==========================================
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    if "users_db" not in st.session_state:
        st.session_state.users_db = {"Rayane": hash_password("DeepLabAdmin")}

def verify_credentials(user: str, pwd: str) -> bool:
    if user in st.session_state.users_db:
        return st.session_state.users_db[user] == hash_password(pwd)
    return False

# ==========================================
# 3. ROUTING & STATE MANAGEMENT
# ==========================================
def navigate(route: str):
    st.session_state.route = route
    st.rerun()

if "route" not in st.session_state:
    st.session_state.route = "landing"

# ==========================================
# 4. VIEW CONTROLLERS (UI Components)
# ==========================================
def view_landing():
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1>THE <span class="accent-text">DEEP</span> LAB</h1>', unsafe_allow_html=True)
    st.markdown("<p>Proprietary Quantitative Research Terminal</p><br>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("INITIALIZE PROTOCOL"):
            navigate("auth_gateway")

def view_auth_gateway():
    st.markdown("<h2>SYSTEM AUTHENTICATION</h2>", unsafe_allow_html=True)
    st.markdown("<p>Select your access tier.</p><br>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        if st.button("EXISTING NODE [LOGIN]"): navigate("login")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("NEW NODE [SIGN UP]"): navigate("signup")
        st.markdown("<hr>", unsafe_allow_html=True)
        if st.button("ABORT"): navigate("landing")

def view_login():
    st.markdown("<h2>ACCESS GATEWAY</h2>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        user = st.text_input("IDENTIFIER")
        pwd = st.text_input("ENCRYPTED KEY", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("AUTHORIZE CONNECTION"):
            if verify_credentials(user, pwd):
                st.session_state.current_user = user
                navigate("dashboard")
            else:
                st.error("ACCESS DENIED: Invalid Node Credentials.")
        if st.button("BACK"): navigate("auth_gateway")

def view_signup():
    st.markdown("<h2>DEPLOY NEW NODE</h2>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        new_user = st.text_input("NEW IDENTIFIER")
        new_pwd = st.text_input("NEW ENCRYPTED KEY", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("REGISTER IDENTITY"):
            if new_user and new_pwd:
                if new_user in st.session_state.users_db:
                    st.error("IDENTIFIER ALREADY EXISTS.")
                else:
                    st.session_state.users_db[new_user] = hash_password(new_pwd)
                    st.success("NODE DEPLOYED. PROCEED TO LOGIN.")
                    navigate("login")
        if st.button("BACK"): navigate("auth_gateway")

def view_dashboard():
    st.markdown("<h2>TERMINAL <span class='accent-text'>ONLINE</span></h2>", unsafe_allow_html=True)
    st.markdown(f"<p>Operator: {st.session_state.current_user} | Status: Secure</p>", unsafe_allow_html=True)
    st.divider()
    
    st.info("QUANTITATIVE DATA STREAM PENDING INTEGRATION...")
    
    if st.button("TERMINATE SESSION"):
        st.session_state.current_user = None
        navigate("landing")

# ==========================================
# 5. MAIN APPLICATION LOOP
# ==========================================
def main():
    init_system()
    init_db()
    
    routes = {
        "landing": view_landing,
        "auth_gateway": view_auth_gateway,
        "login": view_login,
        "signup": view_signup,
        "dashboard": view_dashboard
    }
    
    current_view = routes.get(st.session_state.route)
    current_view()

if __name__ == "__main__":
    main()
