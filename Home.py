from time import sleep

import streamlit as st

from clear import clear

st.set_page_config(
	page_title="Solo web",
	page_icon=":computer:",
	layout="wide",
	initial_sidebar_state="auto",
)

clear()

def write_documentation():
	sleep(0.5)
	
	with open("home.md", 'r') as f:
		for line in f.read():
			yield line
			sleep(0.02)
	

text_without_solo = """Eu eu mollit sit esse nostrud cillum et pariatur 
in consectetur. Cillum commodo veniam irure duis 
dolor consequat officia."""
text_with_solo = """
540811552 924811552 0368106581022410224980011400 11250980011400 
924811250112509248 051210658112501140011100115529112 
8978980010224102241155210368 24811400 
1080487121110098008712114001155211100 980010512 
97810658105121125092488978114009248114001155211100. 
202980010224102241155210368 897810658103681036810658911210658 
117049248105129800871210368 98001110011552111009248 
911211552980011250 911210658102241065811100 
97810658105121125092481095211552871211400 
10658938493849800897898008712.
"""

st.write_stream(write_documentation)

file_columns = st.columns(2)
without_layout = file_columns[0].container(height=150, border=False)
with_layout = file_columns[1].container(height=300, border=False)

without_layout.write("Файл без solo")
without_layout.code(text_without_solo, language="text", line_numbers=True)

with_layout.write("Файл с solo")
with_layout.code(text_with_solo, language="text", line_numbers=True)