import streamlit as st

st.title("Tensorflow Playgroud by Swetha")
st.page_link("app.py", label="Home")

st.subheader("Welcome to Tensorflow Playground")

st.markdown('''1. You can create a :red[Random Dataset] and train your :blue[Customized Neural Network] on the Randomly Generated Data.''')
st.page_link("pages/create_data.py", label=":green[click here]")

st.markdown('''2. This Feature provide :red[Nine] different Dataset You can use them and play with you :blue[customized Neural Network]''')
st.page_link("pages/select_Data.py", label=":green[click here]")
st.sidebar.header("")