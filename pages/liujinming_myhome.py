# 我的主页
import streamlit as st
from PIL import Image
page = st.sidebar.radio("主页", ["Home","情报","答疑","成绩展示","资源分享"])
def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page0():# Home
    st.write("音游，启动！")
def page1():# 情报
    pass
def page2():# 答疑
    st.write("针对因快捷手势导致的音游游玩问题的解决方案:")
    st.write("小米MIUI:更多设置 -> 快捷手势")
    st.image("小米手势.jpg")
def page3():# 成绩展示
    st.write("ADOFAI最难官谱《It go》准度99.22% 严判击破!!!")
    st.image("it go.jpg")
def page4():# 资源分享
    r, g, b = 0, 1, 2
    st.write("音频")# 音乐
    st.write("Laur--国士無双:red[【速核警告！！！】]")
    with open("国士無双.ogg", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format="audio/ogg", start_time=0)
    st.write(":dog:图片处理工具(RGB转换):dog:")# 图片处理
    uploaded_file = st.file_uploader("上传图片", type=["jpg","jpeg","png","bmp"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["空白对照", "BGR", "RBG", "BRG", "GRB", "GBR"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, b, g, r))
        with tab3:
            st.image(img_change(img, r, b, g))
        with tab4:
            st.image(img_change(img, b, r, g))
        with tab5:
            st.image(img_change(img, g, r, b))
        with tab6:
            st.image(img_change(img, g, b, r))
if page == "Home":
    page0()
elif page == "情报":
    page1()
elif page == "答疑":
    page2()
elif page == "成绩展示":
    page3()
elif page == "资源分享":
    page4()
