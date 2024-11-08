import os
import streamlit as st 
from agent import agent_executor
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

st.markdown(
    """
    <style>
    .main {
        background-color: #1e1e1e;
        color: #f5f5f5;
        padding: 10px;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: #f5f5f5;
        border: 1px solid #555555;
        padding: 8px;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #ff5c5c;
        color: white;
        padding: 8px 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title and Description
st.title("🇯🇵 Michibiku: Your Japan Guide 🇯🇵")
st.subheader("Get answers to your questions about Japan and explore its wonders!")

with st.form("my_form"):
    question = st.text_input("Ask me anything about Japan")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = agent_executor.invoke({"input": question})
        st.write(response["output"])

# question = ""
# while question != "exit":
#     question = input("USER: ")
#     response = agent_executor.invoke({"input": question})
#     print(response)