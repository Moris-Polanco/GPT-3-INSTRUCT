import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('GPT-3 Instruct')

st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Instruya a Davinci", value="Dígale qué necesita escribir")
response = openai.Completion(engine="davinci", prompt=prompt_text, max_tokens=3000)
st.text('Artículo:')
st.text((response["choices"][0]["text"]))
