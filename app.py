import streamlit as st
import time

st.set_page_config(
    page_title="Column to List Converter",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #666;
        margin-bottom: 30px;
    }
    .input-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .output-card {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #84fab0;
    }
    .stats-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">📋 Column to List Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transform your data instantly</div>', unsafe_allow_html=True)

# Input section
st.markdown("### 📥 Input Settings")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Prefix**")
    prefix = st.text_input(
        "Add prefix to each item",
        value="",
        placeholder="e.g., ' or \"",
        key="prefix"
    )

with col2:
    st.markdown("**Separator**")
    separator = st.selectbox(
        "Choose separator",
        [", ", ",", "; ", " | ", " ~ ", "\n", " AND "],
        index=0,
        key="sep"
    )

with col3:
    st.markdown("**Suffix**")
    suffix = st.text_input(
        "Add suffix to each item",
        value="",
        placeholder="e.g., ' or \"",
        key="suffix"
    )

st.markdown("---")

# Input area
st.markdown("### ✍️ Paste Your Data")
input_text = st.text_area(
    "Enter your column data here",
    placeholder="Paste column data here...\n• One item per line\n• Tab-separated values\n• Any delimited format",
    height=250,
    key="input_area"
)

# Process the input
if input_text.strip():
    # Split by newline or tab
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]
    result_items = []
    for line in lines:
        if '\t' in line:
            result_items.extend([item.strip() for item in line.split('\t') if item.strip()])
        else:
            result_items.append(line)

    result_items = [f"{prefix}{item}{suffix}" for item in result_items]
    output = separator.join(result_items)
else:
    output = ""
    result_items = []

st.markdown("---")

# Output section with stats
col_output, col_stats = st.columns([3, 1])

with col_output:
    st.markdown("### 📤 Your Result")
    if output:
        # Display in text area for easy selection and copying
        st.text_area(
            "Select and copy your result:",
            value=output,
            height=120,
            disabled=True,
            key="output_area"
        )

        # Also show as code for better formatting
        st.markdown("**Formatted view:**")
        st.code(output, language="text")

        col_copy, col_clear = st.columns(2)
        with col_copy:
            st.info("✅ Select the text above and press Ctrl+C to copy", icon="📋")

        with col_clear:
            if st.button("🗑️ Clear All", use_container_width=True, key="clear_btn"):
                st.rerun()
    else:
        st.info("👈 Paste your data to see the magic happen!", icon="👈")

with col_stats:
    st.markdown("### 📊 Stats")
    if result_items:
        st.metric("Items", len(result_items))
        st.metric("Output Length", len(output))
    else:
        st.metric("Items", 0)
        st.metric("Output Length", 0)

st.markdown("---")

# Templates section
st.markdown("### 📚 Quick Templates")

template_col1, template_col2 = st.columns(2)

with template_col1:
    st.markdown("**SQL IN Clause**")
    template1 = "apple\nbanana\ncherry\ndate"
    if st.button("Load Template 1", use_container_width=True):
        st.session_state.input_area = template1
        st.session_state.prefix = "'"
        st.session_state.suffix = "'"
        st.session_state.sep = ", "
        st.rerun()
    st.code(template1)

with template_col2:
    st.markdown("**Array Format**")
    template2 = "red\ngreen\nblue\nyellow"
    if st.button("Load Template 2", use_container_width=True):
        st.session_state.input_area = template2
        st.session_state.prefix = '"'
        st.session_state.suffix = '"'
        st.session_state.sep = ", "
        st.rerun()
    st.code(template2)

st.markdown("---")
template_col3, template_col4 = st.columns(2)

with template_col3:
    st.markdown("**Newline Separated**")
    template3 = "item1\nitem2\nitem3"
    if st.button("Load Template 3", use_container_width=True):
        st.session_state.input_area = template3
        st.session_state.prefix = ""
        st.session_state.suffix = ""
        st.session_state.sep = "\n"
        st.rerun()
    st.code(template3)

with template_col4:
    st.markdown("**Pipe Separated**")
    template4 = "north\nsouth\neast\nwest"
    if st.button("Load Template 4", use_container_width=True):
        st.session_state.input_area = template4
        st.session_state.prefix = ""
        st.session_state.suffix = ""
        st.session_state.sep = " | "
        st.rerun()
    st.code(template4)

st.markdown("---")

# Guide section
st.markdown("""
### 🎯 How to Use

**Step 1: Paste Your Data**
- Paste column data from Excel, CSV, or any source
- One item per line or tab-separated

**Step 2: Configure Options**
- **Prefix**: Add text at the beginning of each item (e.g., single quote for SQL)
- **Separator**: Choose how items are joined (comma, semicolon, pipe, newline, etc.)
- **Suffix**: Add text at the end of each item (e.g., closing quote)

**Step 3: Get Your Result**
- Result appears instantly in the output box
- Click "Copy to Clipboard" to copy the result
- Use the preview to verify your data

### 💡 Common Use Cases

**SQL WHERE IN clause:**
- Prefix: `'` | Separator: `, ` | Suffix: `'`
- Result: `'apple', 'banana', 'cherry'`

**JavaScript Array:**
- Prefix: `"` | Separator: `, ` | Suffix: `"`
- Result: `"item1", "item2", "item3"`

**Markdown List:**
- Prefix: `- ` | Separator: `\\n` | Suffix: ``
- Result: `- item1\\n- item2\\n- item3`

### ⚡ Tips
- Copy directly from Excel or Google Sheets
- Works with tab-separated or line-separated data
- Supports special characters in prefix/suffix
- Instant preview of your output
""
)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 0.9em;'>"
    "🚀 Built with Streamlit | Made with ❤️"
    "</div>",
    unsafe_allow_html=True
)
