import streamlit as st
import hashlib

# ==========================================
# 1. SYSTEM CONFIGURATION & UI INJECTION
# ==========================================
def init_system():
    st.set_page_config(page_title="Deep Lab | Terminal", page_icon="🟢", layout="centered")
    
    # Ultra-Neon Matrix CSS Injection
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap');
        
        :root {
            --bg-color: #000000;
            --accent: #39FF14;
            --surface: #050505;
            --text-main: #FFFFFF;
            --text-muted: #A0A0A0;
        }
        
        .stApp { 
            background-color: var(--bg-color); 
            background-image: radial-gradient(circle at center, rgba(10,30,10,0.4) 0%, rgba(0,0,0,1) 70%);
        }
        
        /* --- Matrix Landing Page Specifics --- */
        .matrix-title {
            font-family: 'Courier Prime', monospace;
            color: var(--accent);
            font-size: 4.5rem;
            font-weight: 700;
            text-align: center;
            text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 40px #39FF14, 0 0 80px rgba(57,255,20,0.4);
            letter-spacing: 6px;
            margin-bottom: 5px;
            margin-top: 10vh;
        }
        
        .matrix-subtitle {
            font-family: 'Courier Prime', monospace;
            color: var(--text-muted);
            text-align: center;
            font-size: 1.1rem;
            letter-spacing: 2px;
            margin-bottom: 50px;
        }

        /* --- Institutional UI Elements --- */
        h2, h3 { 
            font-family: 'JetBrains Mono', monospace; 
            color: var(--text-main) !important; 
            font-weight: 700;
            text-align: center;
        }
        
        .accent-text { color: var(--accent); }
        p { color: var(--text-muted); text-align: center; font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; }
        
        /* Hollow Glowing Button */
        .stButton>button { 
            background-color: #000000; 
            color: var(--accent); 
            border: 2px solid var(--accent); 
            border-radius: 4px; 
            width: 100%; 
            padding: 15px; 
            font-family: 'Courier Prime', monospace;
            font-size: 1rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            box-shadow: 0 0 10px rgba(57, 255, 20, 0.2) inset, 0 0 10px rgba(57, 255, 20, 0.2);
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover { 
            background-color: rgba(57, 255, 20, 0.1);
            color: var(--accent);
            box-shadow: 0 0 20px rgba(57, 255, 20, 0.6) inset, 0 0 20px rgba(57, 255, 20, 0.6);
            border-color: var(--accent);
            transform: scale(1.02);
        }
        
        input { 
            background-color: var(--surface) !important; 
            color: var(--accent) !important; 
            border: 1px solid rgba(57, 255, 20, 0.3) !important; 
            border-radius: 2px !important;
            font-family: 'JetBrains Mono', monospace !important;
            text-align: center;
        }
        input:focus { border-color: var(--accent) !important; box-shadow: 0 0 10px rgba(57,255,20,0.2) !important; }
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
    st.markdown('<div class="matrix-title">THE DEEP LAB</div>', unsafe_allow_html=True)
    st.markdown('<div class="matrix-subtitle">Quantitative Market Research & Data-Driven Trading Terminal</div>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("ACCESS TERMINAL"):
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
