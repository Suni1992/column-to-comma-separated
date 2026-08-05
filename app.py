import streamlit as st

st.set_page_config(
    page_title="column to Comma Separated",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================
# CSS
# ==========================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#667eea,#764ba2);
}

/* Main Container */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.main-title {
    text-align:center;
    font-size:3rem;
    font-weight:700;
    color:white;
    margin-bottom:5px;
}

.subtitle {
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:30px;
}

/* Cards */
.card {
    background:white;
    padding:5px;
    border-radius:20px;
    box-shadow:0 8px 20px rgba(0,0,0,.25);
    margin-bottom:20px;
}

/* Inputs */
.stTextInput input {
    border-radius:10px !important;
}

.stTextArea textarea {
    border-radius:10px !important;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius:10px;
}

/* Buttons */
.stButton > button {
    width:100%;
    border:none;
    border-radius:10px;
    background:linear-gradient(135deg,#667eea,#764ba2);
    color:white;
    font-weight:bold;
    height:45px;
}

.stButton > button:hover {
    transform:translateY(-2px);
    transition:0.3s;
}

/* Metrics */
[data-testid="metric-container"] {
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.markdown("""
<div class="main-title">
📋 Column to Comma Separated
</div>

<div class="subtitle">
Convert Columns into SQL, Arrays & Lists Instantly
</div>
""", unsafe_allow_html=True)

# ==========================
# Input Card
# ==========================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📥 Input Settings")

col1, col2, col3 = st.columns(3)

with col1:
    prefix = st.text_input(
        "Prefix",
        placeholder="'"
    )
    
with col2:
    suffix = st.text_input(
        "Suffix",
        placeholder="'"
    )    

with col3:
    separator = st.selectbox(
        "Separator",
        [
            ", ",
            ",",
            "; ",
            " | ",
            "\n",
            " AND ",
            " OR ",
            " <br> ",
            " None "
        ]
    )



# Input and Output Side by Side
col_input, col_output = st.columns([1, 1])

with col_input:

    st.markdown("### ✍️ Paste Your Data")

    input_text = st.text_area(
        "",
        height=350,
        placeholder="""Paste your data here...

Apple
Banana
Orange
Mango"""
    )

st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# Conversion Logic
# ==========================

result_items = []

if input_text.strip():

    rows = [
        line.strip()
        for line in input_text.split("\n")
        if line.strip()
    ]

    for row in rows:

        if "\t" in row:
            values = [
                x.strip()
                for x in row.split("\t")
                if x.strip()
            ]
            result_items.extend(values)

        else:
            result_items.append(row)

    result_items = [
        f"{prefix}{item}{suffix}"
        for item in result_items
    ]

    output = separator.join(result_items)

else:
    output = ""

# ==========================
# Output Section
# ==========================

with col_output:

    st.markdown("### 📤 Output")

    output_box = st.empty()

    output_box.text_area(
        "",
        value=output,
        height=350
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================
# Footer
# ==========================

st.markdown("""
<div style="
text-align:center;
color:white;
margin-top:30px;
font-size:14px;
">
🚀 Built with Streamlit
</div>
""", unsafe_allow_html=True)
