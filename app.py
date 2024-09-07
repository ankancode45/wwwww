import streamlit as st
st.markdown("*STREAMLIT IS AMAZING!!!*")
st.markdown("##streamlit is amazing!!!")
st.markdown('''
-pen
-paper 
-pencil
-copy
-marker 
        ''')


st.title('streamlit rocks:100 :white_check_mark: ')

st.subheader(':green[welcome] :red[to the world of] :violet[streamlit]')

st.caption(':crown: This is a caption :crown:')


st.code("""
///Hello in java 
      class A{
      voidmain()
      {
      system.out.println("HI")
      }
     }
""",language='java')


st.text("Hello Streamlit!!!!",help='I am the helper!!!!!')



st.subheader('Todays temperature')
st.metric("Temperature","30","1.2C")

st.subheader('Current wind speed')
st.metric("wind speed","6 kwph","-8%",help='Display the current temperature!!!')

 
