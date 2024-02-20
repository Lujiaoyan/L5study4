


import streamlit as st

page = st.sidebar.radio('我的首页', ['音乐','音乐播放器'])

def page1():
    st.image("1.png")
    st.write("歌曲:  浮光")
    st.write("艺术家:  周深")
    st.write("专辑:  浮光")

def page2():
    st.image("1.png")
    st.write("歌曲:  浮光")
    st.write("艺术家:  周深")
    with open('2.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
#python -m streamlit run G:\DLC\xuyixiang\xuyixiang_home.py

if page == '音乐':
    page1()
elif page == '音乐播放器':
    page2()

