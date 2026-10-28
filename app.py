import streamlit as st
import secrets
import string

# Set up bold, high-contrast page configuration
st.set_page_config(
    page_title="VAULT // BOLD PASSWORD ENGINE",
    page_icon="⚡",
    layout="centered"
)

# Deep Black, Neon Amber, and Stark White Bold Design Theme
st.markdown("""
<style>
    /* Global Background and Typography */
    .stApp {
        background-color: #0E0E10;
        color: #FFFFFF;
        font-family: 'Impact', 'Arial Black', sans-serif;
    }
    
    /* Header Customization */
    h1 {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        letter-spacing: -2px !important;
        text-transform: uppercase !important;
        color: #FFB800 !important;
        margin-bottom: 0px !important;
    }
    
    h3 {
        font-size: 1.5rem !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: #FFFFFF !important;
        border-bottom: 4px solid #FFB800;
        padding-bottom: 5px;
    }
    
    /* Custom High-Contrast Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: #1A1A1E;
        border: 2px solid #2A2A30;
        color: #8E8E93 !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 0px 30px;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFB800 !important;
        color: #000000 !important;
        border: 2px solid #FFB800 !important;
        transform: translateY(-2px);
        box-shadow: 0px 5px 0px #A67800;
    }
    
    /* Input field styling */
    .stTextInput input {
        background-color: #1A1A1E !important;
        color: #FFFFFF !important;
        border: 3px solid #2A2A30 !important;
        border-radius: 0px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        padding: 12px !important;
    }
    .stTextInput input:focus {
        border-color: #FFB800 !important;
        box-shadow: none !important;
    }
    
    /* Bold Brutalist Buttons */
    .stButton > button {
        width: 100%;
        background-color: #FFB800 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.3rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border: none !important;
        border-radius: 0px !important;
        padding: 15px !important;
        box-shadow: 0px 6px 0px #A67800 !important;
        transition: all 0.1s ease;
    }
    .stButton > button:hover {
        transform: translateY(2px);
        box-shadow: 0px 4px 0px #A67800 !important;
    }
    .stButton > button:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #A67800 !important;
    }
    
    /* Mega Display Output Block */
    .mega-output-box {
        padding: 25px;
        background-color: #1A1A1E;
        border: 4px solid #FFB800;
        color: #FFB800;
        font-family: 'Courier New', monospace;
        font-size: 2rem;
        font-weight: 900;
        text-align: center;
        word-break: break-all;
        margin-top: 20px;
        box-shadow: 0px 10px 0px rgba(255, 184, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# App Branding Layout
st.title("⚡ VAULT ENGINE")
st.markdown("<p style='font-size:1.1rem; font-weight:700; color:#8E8E93; text-transform:uppercase; letter-spacing:2px; margin-bottom:30px;'>Cryptographic Security // High-Contrast Design</p>", unsafe_allow_html=True)

def generate_random_password(length, use_upper, use_lower, use_digits, use_special):
    charset = ""
    if use_upper: charset += string.ascii_uppercase
    if use_lower: charset += string.ascii_lowercase
    if use_digits: charset += string.digits
    if use_special: charset += string.punctuation
    
    if not charset:
        return "ERROR: SELECT CHARSET"
        
    password = []
    if use_upper: password.append(secrets.choice(string.ascii_uppercase))
    if use_lower: password.append(secrets.choice(string.ascii_lowercase))
    if use_digits: password.append(secrets.choice(string.digits))
    if use_special: password.append(secrets.choice(string.punctuation))
    
    remaining_length = length - len(password)
    password += [secrets.choice(charset) for _ in range(max(0, remaining_length))]
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password[:length])

def strengthen_password(base_word):
    if not base_word:
        return "ERROR: EMPTY INPUT"
        
    leet_dict = {'a': '@', 'A': '4', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '$', 'S': '5', 't': '7', 'T': '7'}
    
    transformed = []
    for char in base_word:
        if char in leet_dict and secrets.choice([True, False]):
            transformed.append(leet_dict[char])
        else:
            transformed.append(char.upper() if secrets.choice([True, False]) else char.lower())
            
    secure_nums = "".join(secrets.choice(string.digits) for _ in range(3))
    secure_special = secrets.choice("!@#$%^&*")
    
    return "".join(transformed) + secure_nums + secure_special

# Brutalist Tab System Layout
tab1, tab2 = st.tabs(["01 // GENERATE RANDOM", "02 // ENHANCE PHRASE"])

with tab1:
    st.write("")
    st.subheader("PARAMETER CONFIGURATION")
    
    length = st.slider("TARGET LENGTH", min_value=8, max_value=64, value=16)
    
    col1, col2 = st.columns(2)
    with col1:
        uppercase = st.checkbox("UPPERCASE (A-Z)", value=True)
        lowercase = st.checkbox("LOWERCASE (a-z)", value=True)
    with col2:
        digits = st.checkbox("NUMBERS (0-9)", value=True)
        special = st.checkbox("SPECIAL (!@#$)", value=True)
        
    st.write("")
    if st.button("RUN ENGINE", key="run_gen"):
        result = generate_random_password(length, uppercase, lowercase, digits, special)
        st.markdown(f'<div class="mega-output-box">{result}</div>', unsafe_allow_html=True)

with tab2:
    st.write("")
    st.subheader("STRING REINFORCEMENT")
    
    base_input = st.text_input("INPUT WEAK BASE WORD:", placeholder="e.g., orange")
    
    st.write("")
    if st.button("MUTATE WORD", key="run_strengthen"):
        strengthened_result = strengthen_password(base_input)
        st.markdown(f'<div class="mega-output-box">{strengthened_result}</div>', unsafe_allow_html=True)
