import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]

import streamlit as st
from streamlitextras.authenticator import get_auth

auth = None
def main():
    global auth
    auth = get_auth("my_cookie_name")
    auth.delayed_init() # This is required to make sure current Authenticator stays in session state

    auth_status = auth.auth_status
    user = auth.current_user

    if auth_status and user:
        st.write(f"Welcome {user.displayName}!")
    else:
        auth_page()

def auth_page():
    if auth.current_form == "login" or not auth.current_form:
        user, res, error = auth.login("Login")
    if auth.current_form == "register":
        res, error = auth.register_user("Register")
    elif auth.current_form == "reset_password":
        res, error = auth.reset_password("Request password change email")

    if error:
        st.error(error.message)

if __name__ == "__main__":
    main()
    
st.title('GPT-3 Instruct')

st.text('This GPT-3 model is the Davinci-engine')
prompt_text = st.text_input(label="Add here phrase, which you want to be completed", value="Escriba un caso de ética, con las siguientes palabras clave:")
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt_text, max_tokens=3000)
st.text('Remaining phrase:')
st.markdown(response["choices"][0]["text"])
