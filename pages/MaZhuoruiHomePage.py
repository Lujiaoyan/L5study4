# coding:utf-8

'''我的主页'''

import streamlit as st
from PIL import Image

page = st.sidebar.radio('首页', ['兴趣推荐', '图片处理工具', '智慧词典', '留言区'])


def img_change(img, rc, bc, gc):
    width, height = img.size
    img_array = img.load()

    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]

            img_array[x, y] = (r, g, b)

    return img


def page1():
    '''我的兴趣推荐'''
    st.image('logo.png')
    st.write('动漫推荐')
    st.write('------------------------')
    st.write('你的名字。（君の名は。）')
    st.image('YourName.png')
    st.write('故事梗概:')
    text = '故事背景发生在适逢千年一遇彗星到访的日本，生活在日本小镇的女高中生宫水三叶对于担任镇长的父亲所举行的选举运动，还有家传神社的古老习俗感到无聊乏味，对大城市充满憧憬的她，甚至幻想着来世请做东京的帅哥！忽然有一天三叶做了个自己变成男孩子的梦，在陌生的房间，面对陌生的朋友，以及东京的街道。虽然感到困惑，但少女对于能来到朝思暮想的东京还是充满喜悦。与此同时，生活在东京的男高中生立花泷也做了个奇怪的梦，他在一个从未去过的深山小镇中，变成了女高中生。少男少女就这样在梦中邂逅了彼此，并带着“不论你在世界何方我一定会去见你”的信念去寻找彼此.'
    st.write(text)


def page2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size

        img = Image.open(uploaded_file)

        tb1, tb2, tb3, tb4 = st.tabs(['原图', '改色1', '改色2', '改色3'])

        with tb1:
            st.image(img)

        with tb2:
            st.image(img_change(img, 0, 2, 1))

        with tb3:
            st.image(img_change(img, 1, 2, 0))

        with tb4:
            st.image(img_change(img, 1, 0, 2))
def page3():
    '''我的智慧词典'''
    pass


def page4():
    '''我的留言区'''
    pass


if page == '兴趣推荐':
    page1()
elif page == '图片处理工具':
    page2()
elif page == '智慧词典':
    page3()
elif page == '留言区':
    page4()
