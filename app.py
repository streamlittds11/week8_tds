import streamlit as st
st.header("""
This app finds the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.subheader('User Input Parameters')

def user_input_features():
    Number_1 = st.number_input("Number_1,step_size=1")
    Number_2 = st.number_input("Number_2",min_value=-1000000000,max_value=1000000000)
    Number_3 = st.number_input("Number_3",min_value=-1000000000,max_value=1000000000)
    
    return max(Number_1,Number_2,Number_3)
answer=user_input_features()
st.subheader('Largest Number')
st.write(answer)
