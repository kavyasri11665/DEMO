import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of dogs")
col1,col2=st.columns(2)
with col1:
  st.subheader("paresian")
  st.image("./cat1.jpeg",caption="French Bulldogs",width=300,use_column_width=True)
  st.write("French Bulldogs are cute")
with col2:
  st.subheader("ragdoll")
  st.image("./cat2.jpg",caption="Golden Retriver",width=300,use_column_width=True)
  st.write("Golden Retriver cat are cute")
                     

                   
