'''我的主页'''
import streamlit as st
from PIL import Image,ImageFilter
page = st.sidebar.radio("我的主页",["我的兴趣推荐","我的图片处理器","我的智慧词典","我的留言区"])

def page1():
    '''兴趣推荐'''
    st.image("ClassIn_20240219174943.jpg")
    st.write("我最喜欢的电影：流浪地球，长津湖")
    st.write("我最难忘的旅行：爬天柱山")
def page2():
    '''图片处理器'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图","改色1","改色2","改色3","滤镜"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            im = img.filter(ImageFilter.GaussianBlur)
            st.image(im)

def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass


def img_change(img,rc,gc,bc):
    '''图片处理器'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc] 
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
    
if page == "我的兴趣推荐":
    page1()
if page == "我的图片处理器":
    page2()
if page == "我的智慧词典":
    page3()
if page == "我的留言区":
    page4()
