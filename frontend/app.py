import streamlit as st
import requests

# 🔗 BACKEND URL
BASE_URL = "https://ai-code-debugger-gen-ai.onrender.com"

st.set_page_config(page_title="AI Code Debugger", layout="wide")

# 🎨 DARK UI + BIG FONT
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://images.unsplash.com/photo-1510915228340-29c85a43dcfe") no-repeat center center fixed;
    background-size: cover;
}

.main {
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(12px);
    border-radius: 12px;
    padding: 20px;
}

html, body, [class*="css"] {
    font-size: 18px;
    color: white;
}

h1 {
    text-align: center;
    font-size: 50px;
    color: #00f5ff;
    text-shadow: 0px 0px 20px #00f5ff;
}

.stButton>button {
    font-size: 18px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    border-radius: 12px;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.07);
    box-shadow: 0px 0px 20px #06b6d4;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

.stMarkdown, .stTextArea, .stCodeBlock {
    animation: fadeIn 0.5s ease-in;
}

[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.85);
}
</style>
""", unsafe_allow_html=True)

# 🧠 Title
st.markdown("""
<h1>🧠 AI Code Debugger</h1>
<p style='text-align:center; font-size:20px;'>
Fix bugs • Optimize code • Analyze repositories 🚀
</p>
""", unsafe_allow_html=True)

# 🧠 SESSION STATE
if "history" not in st.session_state:
    st.session_state.history = []

if "current_result" not in st.session_state:
    st.session_state.current_result = ""

# 🎛 Sidebar
with st.sidebar:
    st.title("⚙ Controls")

    language = st.selectbox(
        "Select Language",
        ["Python", "C++", "Java", "JavaScript"]
    )

    if st.button("🧹 Clear Output"):
        st.session_state.current_result = ""

# 🧱 Layout
col1, col2 = st.columns(2)

# 📥 INPUT
with col1:
    st.markdown("### 💻 Enter Code")
    code_input = st.text_area("", height=300)

    if st.button("🚀 Analyze Code"):
        if code_input.strip():
            with st.spinner("🤖 AI thinking..."):
                try:
                    res = requests.post(
                        f"{BASE_URL}/analyze",
                        json={"code": code_input, "language": language}
                    )
                    result = res.json().get("result", "No response")

                    st.session_state.current_result = result

                    st.session_state.history.append({
                        "code": code_input,
                        "result": result
                    })
                except:
                    st.error("⚠️ Backend connection error")

    if st.button("▶ Run Code"):
        try:
            res = requests.post(
                f"{BASE_URL}/run",
                json={"code": code_input, "language": language}
            )
            out = res.json()

            st.markdown("### 🖥 Output")
            if out.get("output"):
                st.code(out["output"])
            if out.get("error"):
                st.error(out["error"])
        except:
            st.error("⚠️ Backend connection error")

# 📊 OUTPUT
with col2:
    st.markdown("### 📊 Analysis Output")

    if st.session_state.current_result:
        latest = st.session_state.current_result

        parts = latest.split("Fix:")

        st.markdown("### 🐛 Bugs")
        st.write(parts[0])

        if len(parts) > 1:
            fix = parts[1].split("Explanation:")

            st.markdown("### 🔧 Fix")
            st.code(fix[0])

            if len(fix) > 1:
                exp = fix[1].split("Optimized Code:")

                st.markdown("### 📖 Explanation")
                st.write(exp[0])

                if len(exp) > 1:
                    st.markdown("### ⚡ Optimized Code")
                    st.code(exp[1])
    else:
        st.info("💡 Enter code and click Analyze")

# 🔗 GITHUB ANALYZER
st.markdown("## 🔗 GitHub Repo Analyzer")

repo = st.text_input("Enter Repo URL")

if st.button("Analyze Repo"):
    if repo:
        with st.spinner("Analyzing repo..."):
            try:
                res = requests.post(
                    f"{BASE_URL}/analyze-repo",
                    json={"repo_url": repo}
                )
                st.code(res.json().get("result", "No response"))
            except:
                st.error("⚠️ Backend connection error")

# 📜 HISTORY
st.markdown("## 📜 History")

for item in reversed(st.session_state.history):
    with st.expander("View Previous Analysis"):
        st.code(item["code"])
        st.write(item["result"])