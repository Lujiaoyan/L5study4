'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['原神目前版本新角色介绍','我的快速“更改神之眼大法”','我的留言区'])

def page1():
    '''我的兴趣'''
    st.write(':red[目前版本新角色介绍]')
    st.write('----------------------------')
    st.write('4.4版本')
    st.write('下一个远方 (《原神》2024新春会同人曲)- 喵酱油/爆裂菊是也/花玲/彭博/钱琛/苏逸_Suyi')
    with open('下一个远方.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3',start_time=0)
    st.image('4.4官方pv宣传图.png')    
    st.image('4.4新角色——嘉明.png')
    st.image('嘉明培养攻略.png')
    st.write('作者：小橙子猪弟,抖音号：1139838392')
    st.write(':red[补充：]'+'圣遗物还可以用魔女（伤害上限更高，但更难刷QAQ），前期可以用狂战（冒险等级45以前不对副词条有要求）；配队思路嘉明+挂水+生存+流动位（个人看法）')
    st.write(':red[配队推荐：（5组）]')
    st.write('No1.“小鸟芙特嘉”（嘉明+闲云+芙宁娜+班尼特）'+':orange[备注：小鸟芙特嘉，雷霆嘎巴！！除了难凑齐阵容其他全是优点！]')
    st.write('No2.“雷嘉夏香”（嘉明+雷电将军+夏沃蕾+香菱）'+':orange[备注：火雷超载，夏减抗回血，雷神挂雷充能，香菱副位输出，嘉明最后出场打C位，有对群能力，且枫丹后的怪基本炸不动，炸怪缺点较小——零充真君（抖音号：58438516480）]')
    st.write('No3.“砂罗班嘉”（嘉明+砂糖+罗莎莉亚+班尼特）'+':orange[备注：造价便宜弥补画地为牢的缺点]')
    st.write('No4.“芙嘉闲坎”（嘉明+芙宁娜+闲云+坎蒂丝）'+':orange[备注：‘小鸟芙特嘉’的变种版，坎不用练度，操作无脑]')
    st.write('No5.嘉明纯火队（嘉明+万叶+香菱+班尼特）'+':orange[备注：嘉明版的国家队]')
    st.image('4.4新角色——闲云.png')
    st.image('闲云培养攻略.png')
    st.write('作者：苏打ooo,抖音号：2226401033')
    st.write(':orange[那个女人没抽出来，没有研究...先看攻略吧（手动尴尬）]')
    
def page2():
    '''我的图片处理工具'''
    st.write(':sunglasses:最近网上总有人给角色换色就当换元素了，于是我直接提供一个快速方式:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))        
    
def page3():
    '''留言区'''
    pass

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '原神目前版本新角色介绍':
    page1()

elif page == '我的快速“更改神之眼大法”':
    page2()

elif page == '我的留言区':
    page3()
