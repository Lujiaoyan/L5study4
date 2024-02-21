"""我的主页"""
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    """兴趣推荐"""
    tab1, tab2, tab3, tab4 = st.tabs([':red[电影推荐]', ':red[小说推荐]', ':red[歌曲推荐]', ':red[工具推荐]'])
    with tab1:
        st.write('暂无推荐')
    with tab2:
        st.write('暂无推荐')
    with tab3:
        with open('好运来.mp3', 'rb')as f:
            haoyunlai = f.read()
        with open('只因你太美.mp3', 'rb')as f:
            zhiyinnitaimei = f.read()
        st.write('好运来')
        st.audio(haoyunlai, format='audio/mp3', start_time=0)
        st.write('只因你太美')
        st.audio(zhiyinnitaimei, format='audio/mp3', start_time=0)
    with tab4:
        st.write('暂无推荐')
def page2():
    """图片处理工具"""
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['原图', ':blue[红绿交换]', ':green[红蓝交换]', ':red[绿蓝交换]', '改色4', '改色5'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, rc=1, gc=0, bc=2))
        with tab3:
            st.image(img_change(img, rc=2, gc=1, bc=0))
        with tab4:
            st.image(img_change(img, rc=0, gc=2, bc=1))
        with tab5:
            st.image(img_change(img, rc=1, gc=2, bc=0))
        with tab6:
            st.image(img_change(img, rc=2, gc=0, bc=1))
def page3():
    """智慧词典"""
    st.write('暂无')
def page4():
    """留言区"""
    st.write('暂无')

def img_change(img, rc=2, gc=1, bc=0):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
