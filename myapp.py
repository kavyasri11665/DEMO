import streamlit as st
st.set_page_config(page_title='cats')
st.header("types of cats")
col1,col2=st.columns(2)
with col:
  st.subheader("Persian Cat")
  st.image("./Persian.jpg",caption="Persian Cat",width=300,use_column_width=true)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./ragdoll.jpg",caption="Ragdoll Cat",width=300,use_column_width=true)
  st.write("Ragdoll cats are proud")
                     

                   
