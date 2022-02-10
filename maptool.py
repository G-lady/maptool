import streamlit as st

from PIL import Image
img = Image.open("laboratory.png")
 
st.image(img, width=700)

st.title('Welcome to Laboratories in Nigeria')

st.markdown('### Use this App to Easily Access Laboratories!')

lab_name = st.text_input("Enter name of Laboratory:\n")

lab_location = st.selectbox("Select Location: ",['Abuja', 'Port-Harcourt', 'Lagos', 'Ibadan'])

lab_registration = st.number_input("MLSCN Registration Number")

inquiry_type = st.selectbox('Select your staff type: ',('Admin', 'Laboratory Professionals', 'Cleaners',))

number_of_staff = st.text_input("Number of Staff in lab")

accreditation_date = st.date_input('MLSCN Accreditation Date')

equipment_list = st.text("Enter your Equipments in lab:\n")

if(st.button('Submit')):
    result = equipment_list.title("labmap") 