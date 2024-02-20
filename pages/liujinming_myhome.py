# 我的主页
import streamlit as st
page = st.sidebar.radio("主页", ["一些音乐","情报","答疑","成绩展示","资源分享"])
def page1():# 一些音乐
    st.write(":red[速核警告!!!]")
    with open("国士無双.ogg", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format="audio/ogg", start_time=0)
def page2():# 情报
    pass
def page3():# 答疑
    pass
def page4():# 成绩展示
    st.write("ADOFAI最难官谱'It go' 准度99.22% 严判击破!!!")
    st.image("it go.jpg")
def page5():# 资源分享
    pass
if page == "一些音乐":
    page1()
elif page == "情报":
    page2()
elif page == "答疑":
    page3()
elif page == "成绩展示":
    page4()
elif page == "资源分享":
    page5()