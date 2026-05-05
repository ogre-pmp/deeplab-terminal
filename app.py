import streamlit as st
import pandas as pd
import hashlib

# ==========================================
# 1. SYSTEM CONFIGURATION & UI INJECTION
# ==========================================
def init_system():
    st.set_page_config(page_title="Deep Lab | Mentor View", page_icon="🟢", layout="centered")
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600&display=swap');
        
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
        
        .matrix-title {
            font-family: 'Courier Prime', monospace;
            color: var(--accent);
            font-size: 2.5rem;
            font-weight: 700;
            text-shadow: 0 0 10px #39FF14;
            letter-spacing: 3px;
        }
        
        /* Widget Styling */
        .dashboard-widget {
            background: #0A0A0A;
            border: 1px solid #111;
            border-radius: 4px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: border-color 0.3s ease;
        }
        .dashboard-widget:hover { border-color: #39FF14; }
        
        .metric-card { text-align: center; }
        .metric-card p { text-transform: uppercase; letter-spacing: 2px; font-size: 0.75rem; margin: 0; color: #888; }
        .metric-card h2 { font-family: 'JetBrains Mono', monospace; font-size: 2rem !important; margin: 0; }
        
        .accent-text { color: var(--accent); font-family: 'JetBrains Mono', monospace; }

        input, textarea, select { 
            background-color: var(--surface) !important; 
            color: var(--accent) !important; 
            border: 1px solid rgba(57, 255, 20, 0.3) !important; 
            border-radius: 2px !important;
            font-family: 'JetBrains Mono', monospace !important;
            text-align: center;
        }

        [data-testid="stSidebar"] {
            background-color: #030303;
            border-right: 1px solid #111;
        }
        
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
    st.markdown('<div class="matrix-title" style="font-size: 4.5rem; text-align: center;">THE DEEP LAB</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0A0A0; text-align: center; font-family: \'Courier Prime\', monospace;">Quantitative Market Research Terminal</p><br>', unsafe_allow_html=True)
    
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
                st.error("ACCESS DENIED: Invalid Credentials.")
        if st.button("BACK"): navigate("auth_gateway")

def view_signup():
    st.markdown("<h2>DEPLOY NEW NODE</h2>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        new_user = st.text_input("NEW IDENTIFIER")
        new_pwd = st.text_input("NEW KEY", type="password")
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
    st.markdown('<div class="matrix-title">THE DEEP LAB | MENTOR VIEW</div>', unsafe_allow_html=True)
    st.markdown(f"<p>Welcome back, {st.session_state.current_user}. System Status: Stable.</p>", unsafe_allow_html=True)
    st.divider()

    # --- MAIN LAYOUT ---
    col_main, col_metrics = st.columns([2, 1])

    with col_main:
        st.markdown('<div class="dashboard-widget"><h3>ANALYTICS OVERVIEW</h3>', unsafe_allow_html=True)
        # Using a TradingView iframe for the chart placeholder
        chart_widget = '<iframe src="https://s.tradingview.com/widgetembed/?symbol=NASDAQ%3ANQ1!&interval=D&theme=dark" width="100%" height="400" frameborder="0"></iframe>'
        st.markdown(chart_widget, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="dashboard-widget"><h3>STUDENT ACTIVITY FEED</h3>', unsafe_allow_html=True)
        # Student Feed placeholder
        feed_data = {'TIME': ['10:31', '10:15', '09:45'], 'EVENT': ['Student Achraf added a Master Playbook', 'Student 2 updated CSV data', 'Mentorship session scheduled']}
        df_feed = pd.DataFrame(feed_data)
        st.dataframe(df_feed, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_metrics:
        def metric_widget(title, value, unit="", accent=False):
            st.markdown(f"""
            <div class="dashboard-widget metric-card">
                <p>{title}</p>
                <h2 class="{'accent-text' if accent else ''}">{value}<span style="font-size: 1rem; color: #888;">{unit}</span></h2>
            </div>
            """, unsafe_allow_html=True)

        metric_widget("Total Students Managed", "12")
        metric_widget("Active live sessions", "3")
        metric_widget("Data Uploads (Last 24h)", "125", " CSVs")
        metric_widget("Overall Mentor Score", "91.2", " / 100", accent=True)

    st.divider()
    
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
    if current_view:
        current_view()
    else:
        navigate("landing")

if __name__ == "__main__":
    main()
