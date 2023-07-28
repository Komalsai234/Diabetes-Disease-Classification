import streamlit as st
from streamlit_extras.switch_page_button import switch_page

image_url = "https://assets.newatlas.com/dims4/default/3461759/2147483647/strip/true/crop/7360x4907+0+3/resize/840x560!/quality/90/?url=http%3A%2F%2Fnewatlas-brightspot.s3.amazonaws.com%2F10%2F7f%2F5e48f79245c0b831a58d7cf8fb1d%2Fdepositphotos-228244172-xl.jpg"

st.title("Diabetes Prediction Web App")
st.title(" ")
st.sidebar.title("Created By:")
st.sidebar.subheader("P.S.S.Sai.Keerthana")
st.sidebar.subheader("P.Komal Sai Anurag")
st.sidebar.subheader("Varun Udayagiri")
st.sidebar.subheader("Sejal Singh")

#st.image(image_url,width=500)

st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="{image_url}" alt="Image" width="550" align="left">'
    '</div>',
    unsafe_allow_html=True
)

st.title(" ")
data_entry = st.button("Click Here to enter the details of the patients", key="red")
if data_entry:
    switch_page("Patient Data")
