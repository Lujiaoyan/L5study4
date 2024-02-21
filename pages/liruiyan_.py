'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def img_change(img,rc,gc,bc):
    """图片处理"""
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img


def page1():
    """兴趣推荐"""
    st.image("liruiyan_LOGO.png")
    st.write("V.box个人工作室")
    st.write("---------------------------------------------")
    st.write("个人爱好:")
    st.write("乐高，computer，以及")
    st.write("热爱生活")
def page2():
    """图片处理工具"""
    st.write(":sunglasses:图片处理の小工具:sunglasses:")
    st.write("a tool to dispose the pictures")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["原图","color1","color2","color3","color4","灰の色(grey)"])
        with tab1:
            st.image(img)
        with tab2:    
            st.image(img_change(img,0,2,1))
        with tab3:    
            st.image(img_change(img,1,2,0))
        with tab4:    
            st.image(img_change(img,1,0,2))
        with tab5:    
            st.image(img_change(img,1,2,1))
        with tab6:    
            st.image(img_change(img,1,1,1))
def page3():
    """智慧词典"""
    pass

def page4():
    """留言区"""
    pass

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
