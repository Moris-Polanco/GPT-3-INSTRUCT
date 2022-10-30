import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('GPT-3 Instruct')

st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Add here phrase, which you want to be completed", value="Add here few words")
response = openai.Completion.create(engine="davinci", prompt=Escriba un artículo para blog sobre el tema indicado, max_tokens=3000)
st.text('Artículo:')
st.text(response["choices"][0]["text"])
