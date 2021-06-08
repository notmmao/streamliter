#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Author: hufeng.mao@carota.ai
Date: 2021-06-08 13:53:49
LastEditTime: 2021-06-08 17:26:29
Description: 
'''

import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.write(
    """
    # My first app
    hello world!
    """
)

def add_input():
    st.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')

def add_progress():
    my_bar = st.progress(0)
    for p in range(100):
        time.sleep(0.1)
        my_bar.progress(p + 1)

def add_image():
    image = Image.open('C:\\Users\\Mao\\Pictures\\gwl.jpg')
    st.image(image, caption='切-格瓦拉')

def add_map():
    df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [31.15344, 121.430649],
    columns=['lat', 'lon'])
    st.map(df)

def add_audio():
    with open('D:\CloudMusic\Lopu$ - So Cute~.mp3', 'rb') as f:
        data = f.read()
        st.audio(data, format="audio/mp3")

def add_video():
    with open("C:\\Users\\Mao\\Videos\\Captures\\魔兽世界 2019-10-27 22-24-36.mp4", 'rb') as f:
        data = f.read()
        st.video(data)

def add_form():
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

def add_beta_container():
    with st.beta_container():
        st.write("This is inside the container")

        st.bar_chart(np.random.randn(50, 3))
    st.write("This is outside the container")

def add_beta_columns():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.write("col1")
        st.button("col1")
    with col2:
        st.write("col2")
        st.button("col2")
    with col3:
        st.write("col3")
        st.button("col3")

def add_beta_expender():
    with st.beta_expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")

def add_graphviz():
    st.graphviz_chart('''
        digraph {
            run -> intr
            intr -> runbl
            runbl -> run
            run -> kernel
            kernel -> zombie
            kernel -> sleep
            kernel -> runmem
            sleep -> swap
            swap -> runswap
            runswap -> new
            runswap -> runmem
            new -> runmem
            sleep -> runmem
        }
    ''')

def add_placeHolder():
    with st.empty():
        for seconds in range(60):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
    st.write("✔️ 1 minute over!")

with st.echo():
    st.header('This is a header')
    
    df = pd.read_csv("D:\\BaiduNetdiskDownload\\TQDat\\day\\stk\\600648.csv")
    
    # st.help(df)
    sidebar = st.sidebar
    add_selectbox = sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    df_date = df.pop("date")
    df_volume = df.pop("volume")

    column = sidebar.radio("Data column", ["open", "close", "high", "low"])
    df_column = df[column]
    start = sidebar.slider("Start", 0, len(df_column))
    end = sidebar.slider("End", 0, len(df_column), 50)
    
    data = df[start:start+end]
    st.line_chart(data)
    st.bar_chart(data)
    

    add_map()
    add_image()
    add_graphviz()
    add_audio()
    add_video()
    add_form()
    add_beta_container()
    add_beta_columns()
    add_beta_expender()
    # add_placeHolder()
    
    if start > 0:
        st.balloons()
        st.error('Error message')

    st.dataframe(df[start:start+end])
    # st.table(df[start:start+end])

