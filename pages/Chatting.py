import streamlit as st

from clear import clear
from streams import Streams

st.set_page_config(
	page_title="Chat with solo",
	page_icon=":computer:",
	layout="centered",
	initial_sidebar_state="auto",
)

clear()

st.title("💬 Solo chat")

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.write(message["content"])

if len(st.session_state.messages) == 0:
	with st.chat_message("assistant"):
		response = st.write_stream(Streams.usage)
		st.session_state.messages.append({"role": "assistant", "content": response})
	
if prompt := st.chat_input("What is up?"):

	with st.chat_message("user"):
		st.write(prompt)

	with st.chat_message("assistant"):
		if "e#d" in prompt:
			response = st.write_stream(Streams.encoding(prompt))
		elif "d#e" in prompt:
			response = st.write_stream(Streams.decoding(prompt))
		else:
			response = st.write_stream(Streams.notFound)

	st.session_state.messages.append({"role": "user", "content": prompt})
	st.session_state.messages.append({"role": "assistant", "content": response})
