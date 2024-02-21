#一个仅自己可见的，记录生活，记录想法，同时也可以作为学习的工具，比如词典，计算器（？），成绩记录和分析（比如折线图啊啥的）
'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
with open('yrx-十七岁请回答.mp3','rb')as f:
    mymp3 = f.read()
st.audio(mymp3,format = 'audio/kgm',start_time = 1)
def page1():
    '''我的兴趣推荐'''
    st.write('欢迎来到我的兴趣分享，希望大家能在这里重拾力量。')
    st.write('-------------------------------------------------------------------')
    st.write('近期在看的电视剧')
    st.write('《烟火人家》')
    st.image('yrx-烟火人家.jpg')
    st.write('-------------------------------------------------------------------')
    st.write('近期在看的综艺')
    st.write('《令人心动的offer5》')
    st.image('yrx-令人心动的offer5.jpg')
    st.write('-------------------------------------------------------------------')
    st.write('最爱的电影')
    st.write('《魔法满屋》')
    st.image('yrx-魔法满屋.png')
    st.write('-------------------------------------------------------------------')
    st.write('最爱的小说')
    st.write('《拉普拉斯的魔女》')
    st.write('-------------------------------------------------------------------')
    st.write('喜欢的科目')
    st.write('语文、生物')
    st.write('-------------------------------------------------------------------')
    st.write('我的爱好')
    st.write('看书、追剧、学各种各样的技能')
    st.write('-------------------------------------------------------------------')
    st.write('看看我喜欢的一些小说语录，治愈一下自己吧！')
    st.image('yrx-语录1.jpg')
    st.write(':blue[「我们太急切想要一个答案了。想要风光的学位，瞬间的博学，想要意气风发，想闪着金光走向喜欢的人。但现实告诉我，操之过急便会败北，他要我等，要我耐得住不断延长的时间线，要我交付出足够的努力堆砌在沉闷、晦涩的时光里，才肯将一切“我想要”一点一点递送至我手里。」]')
    st.image('yrx-语录2.jpg')
    st.write(':coral[「最勇敢的方式就是销声匿迹，自我沉淀，在繁华中自律，在落魄中自愈。那些难以言表、不作声响、暗自努力的日子，通往你想要的生活，所以开始了就不要停下。心若有所向往，何惧道阻且长。」]')
    st.image('yrx-鼓励1.jpg')
    st.image('yrx-鼓励2.jpg')
    st.image('yrx-鼓励3.jpg')
    st.image('yrx-鼓励4.jpg')
    st.write('-------------------------------------------------------------------')
    st.write('向未来张望的时光，或许孤独而漫长，希望努力过后，都是晴朗。')
    st.image('yrx-pic2.png')
    st.write('注明：以上图片来源于网络。')
def page2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        
    
def page3():
    '''我的智慧词典'''
    pass
def page4():
    '''我的留言区'''
    pass
def img_change(img,rc,gc,bc):
    '''图片处理'''
    new_img = img
    width,height = new_img.size
    new_img_array = new_img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r = new_img_array[x,y][rc]
            g = new_img_array[x,y][gc]
            b = new_img_array[x,y][bc]
            new_img_array[x,y] = (r,g,b)
    return new_img
    
    
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
    
