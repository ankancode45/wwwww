import streamlit as st
import pandas as pd  
import seaborn as sns

def call():
      df=sns.load_dataset('mpg')
      st.dataframe(df)

def call2():
      df=sns.load_dataset('mpg')
      st.dataframe(df.style.highlight_max(axis=0,color='red'))

def call3():
      df=sns.load_dataset('mpg')
      st.table(df.head())


def call4():
      st.subheader('......JSON String........')
      df=sns.load_dataset('mpg')
      st.json(
        {'first_five_mpg':list(df['horsepower'][:5])}
      )


def call5():
     df=sns.load_dataset('mpg')
     #st.line_chart(df,x='weight',y='horsepower')
     st.area_chart(df,x='weight',y='horsepower')

def call6():
    st.text("---------------")
    df=sns.load_dataset('mpg')
    #st.line_chart(df,x='weight',y='horsepower')
    st.bar_chart(df,x='origin',y='cylinders')

def call7():
    st.text("---------------")
    df=sns.load_dataset('mpg')
    fig,ax=plt.subplots()
    ax.scatter(x=df['mpg'],y=df['weight'],c='red')
    ax.set_xlabel('MPG')
    ax.set_ylabel('weight')
    st.pyplot(fig)

if __name__== '__main__':
   call5()
   call6()
   call7()