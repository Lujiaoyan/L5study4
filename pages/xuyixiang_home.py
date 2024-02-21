


import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['音乐','音乐播放器','图片修改到指定大小'])

def page1():
    st.image("周深 - 浮光.png")
    st.write("歌曲:  浮光")
    st.write("艺术家:  周深")
    st.write("专辑:  浮光")

def page2():
    st.image("周深 - 浮光.png")
    st.write("歌曲:  浮光")
    st.write("艺术家:  周深")
    with open('周深 - 浮光.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
#python -m streamlit run G:\DLC\xuyixiang\xuyixiang_home.py
def page3():
    st.write("图片上传，目前只支持正方形和圆形图片。")
    uploacded_file = st.file_uploader("点击此处上传图片。", type=['png','jpeg','jpg'])
    if uploacded_file:
        tab1,tab2,tab3,tab4 = st.tabs(['原图','400X400','800X800','1200X1200'])
        with tab1:
            img_1 = Image.open(uploacded_file)
            st.image(img_1)
        with tab2:
            img_2 = Image.open(img_change(uploacded_file, (400,400)))
            st.image(img_2)
        with tab3:
            img_3 = Image.open(img_change(uploacded_file, (800,800)))
            st.image(img_3)
        with tab4:
            img_4 = Image.open(img_change(uploacded_file, (1200,1200)))
            st.image(img_4)
            
        
def img_change(img, size=(800,800)):
    img.size = size
    return img
    
if page == '音乐':
    page1()
elif page == '音乐播放器':
    page2()
elif page == '图片修改到指定大小':
    page3()
