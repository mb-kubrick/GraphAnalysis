"""Page for performing RAG using Neo4J."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import streamlit as st
from llm_rag_streamlit import run_llm_graph_rag

if 'messages' not in st.session_state:
    st.session_state.messages = []

# PAGE CONTENT ---------------------------------------------------------------------------------------------------------

st.title('Football Transfer Answerer')
st.markdown('Answer any question about transfers of football players and we will answer')

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Your message"):

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = run_llm_graph_rag(prompt)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": answer})
