import streamlit as st

st.title("Hello World!")
st.header("What's up?")
st.subheader("Fine...")
st.text("This is a boy")

# Button
if st.button('Click Me'):
    st.success('sucess')
if st.button('Click Me1'):
    st.info('infromation')
if st.button('Click Me2'):
    st.warning('warning')
if st.button('Click Me3'):
    st.error('error')

# INPUT
name=st.text_input('Enter your full Name: ')
if name:
    st.write(f'Hello, {name}')

age=st.number_input('Enter your age: ', max_value=100, min_value=1)
if age:
    st.write(f'your age is {age}')

# check box
if st.checkbox('I agree to terms and conditions'):
    st.success("Logged in")

# Radio
gender = st.radio('select gender',('Male', 'Female'))

#select box or drop down box
country = st.selectbox('choose your country', ['Nepal','Bhutan', 'India', 'China'])

#slider 
level=st.slider('volume', 1,15)

cb=st.checkbox('I agree to terms and conditons')
bn=st.button('Sign-Up')
if cb and bn:
    st.success("Signed Up sucessfully")
elif bn:
    st.warning('agree all the terms and condition')