'''我的主页'''
import streamlit as st
page = st.sidebar.radio("我的主页",["我的兴趣推荐","我的图片处理器","我的智慧词典","我的留言区"])

def page1():
    '''兴趣推荐'''
    st.image("ClassIn_20240219174943.jpg")
    st.write("我最喜欢的电影：流浪地球，长津湖")
    st.write("我最难忘的旅行：爬天柱山")
def page2():
    '''图片处理器'''
    pass
def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass

if page == "我的兴趣推荐":
    page1()
if page == "我的图片处理器":
    page2()
if page == "我的智慧词典":
    page3()
if page == "我的留言区":
    page4()