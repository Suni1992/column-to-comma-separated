import streamlit as st

st.set_page_config(
    page_title="Column to List Converter",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Column to List Converter")
st.write("Convert column data to comma-separated lists with optional prefix and suffix")

col1, col2 = st.columns(2)

with col1:
    prefix = st.text_input("Prefix", value="", placeholder="e.g., '")

with col2:
    suffix = st.text_input("Suffix", value="", placeholder="e.g., '")

separator = st.selectbox(
    "Separator",
    [", ", ",", "; ", " | ", "\n"],
    index=0
)

st.markdown("---")

input_text = st.text_area(
    "Input (paste your column data here)",
    placeholder="Paste your column data here...\nOne item per line\nor separated by tabs",
    height=200
)

# Process the input
if input_text.strip():
    result = input_text.split("\n" or "\t")
    result = [item.strip() for item in result if item.strip()]
    result = [f"{prefix}{item}{suffix}" for item in result]
    output = separator.join(result)
else:
    output = ""

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Output")
    if output:
        st.text_area("Result", value=output, height=200, disabled=True)
        if st.button("📋 Copy to Clipboard", use_container_width=True):
            st.write(output)
            st.success("Output ready to copy from above!")
    else:
        st.info("Paste your data above to see the result here")

with col2:
    st.subheader("Options")
    if st.button("🗑️ Clear All", use_container_width=True):
        st.rerun()

st.markdown("---")
st.markdown("""
### How to use:
1. Paste your column data (one item per line or tab-separated)
2. Add optional prefix and suffix (e.g., quotes)
3. Choose your separator (comma, semicolon, pipe, etc.)
4. Copy the result!
""")
