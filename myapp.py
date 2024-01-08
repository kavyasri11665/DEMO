import streamlit as st
st.set_page_config(page_title='cats')
st.header("types of cats")
col1,col2=st.columns(2)
with col:
  st.subheader("cat1 Cat")
  st.image("./cat1.jpeg",caption=" Cat1",width=300,use_column_width=true)
  st.write(" cat1 are cute")
with col2:
  st.subheader("cat2 Cat")
  st.image("./cat2.jpg",caption=" Cat2",width=300,use_column_width=true)
  st.write(" cat2 are proud")
                     

                   
