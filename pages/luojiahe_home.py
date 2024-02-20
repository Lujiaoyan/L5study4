"""我的主页"""
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page1():
    """兴趣推荐"""
    st.write(':red[技能展示]')
    # st.image()
    st.write('暂无展示')
    st.write('-----------------------------------------------')
    
    st.write(':red[荣誉分享]')
    # st.image()    
    st.write('暂无分享')
    st.write('-----------------------------------------------')
    
    st.write(':red[电影推荐]')
    # st.image()
    st.write('暂无推荐')
    st.write('-----------------------------------------------')
    
    st.write(':red[小说推荐]')
    # st.image()
    st.write('暂无推荐')
    st.write('-----------------------------------------------')
    
    st.write(':red[歌曲推荐]')
    with open('音乐/好运来.mp3', 'rb')as f:
        haoyunlai = f.read()
    with open('音乐/只因你太美.mp3', 'rb')as f:
        zhiyinnitaimei = f.read()
    st.write('好运来')
    st.audio(haoyunlai, format='audio/mp3', start_time=0)
    st.write('只因你太美')
    st.audio(zhiyinnitaimei, format='audio/mp3', start_time=0)
    st.write('-----------------------------------------------')
    
    st.write(':red[工具推荐]')
    # st.image()
    st.write('暂无推荐')
    st.write('-----------------------------------------------')
    
    st.write(':red[景色分享]')
    # st.image()
    st.write('暂无分享')
def page2():
    """图片处理工具"""
    pass
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
# python -m streamlit run C:\Users\yphy1\Desktop\冬令营\我的网络根据地\my_home.py