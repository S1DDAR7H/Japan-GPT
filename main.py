import os
import streamlit as st 
from agent import agent_executor
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

st.write("Michibiku: Your Japan Guide")

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