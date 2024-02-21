import streamlit as st
from PIL import Image
#python -m  streamlit run C:\Users\shugu\Desktop\陈冠霖的网络根据地\chenguanlin_home.py


page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])


def page1():
    '''兴趣推荐'''
    pass
def page2():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file: 
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))  
        
def page3():
    '''智能词典'''
    pass
def page4():
    '''留言区'''
    pass
if page=='我的兴趣推荐':
    page1()
    st.image("bc0594dc-ca0f-4c44-ac2d-df93d9eab3e6.jpg")
    st.write("九品芝麻官")
elif page=='我的图片处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
    st.write()
elif page=='我的留言区':
    page4()
    st.write()
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
