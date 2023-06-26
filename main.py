import streamlit as st
from PIL import Image
st.write("1962 Telangana Services")
image = Image.open('cow.png')
st.image(image, caption='Sunrise by the mountains')
x="""
This is The 1962 Telangana give full details about 1962 regarding Call counts ,Trips ,UAC% ,Animal treated Etc. 
"""
st.write(x)
