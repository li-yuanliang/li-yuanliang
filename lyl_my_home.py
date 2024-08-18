"""我的主页"""

import streamlit as st
from PIL import Image,ImageOps,ImageFilter
import requests
import random
import matplotlib.pyplot as plt
import time
import os
myDir = 'musics'
files = sorted(os.listdir(myDir))
musics = []
for file in files:
    musics.append(file)
musics_names=sorted(['周深 - Wala li longla.wav', '周深 - 嗨.wav', 
              '周深 - 少管我.wav', '周深 - 空壳.wav', 
              '周深 - 缝合.wav', '周深 - 蜃楼.wav', 
              '周深 - 警报.wav', '周深 - 记忆商店.wav', 
              '周深 - 重启.wav'])
page = st.sidebar.radio("我的首页",["我的主页","我的兴趣推荐","我的图片工具箱","我的计算器","我的智慧词典","我的留言区","我的朋友圈","我的python旅程","生米的基本素养"])
def img_change1(img,rc,gc,bc):
    new_img=img
    w,h=new_img.size
    img_array=new_img.load()
    for x in range(w):
        for y in range(h):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return new_img
def img_change2(img):
    #转灰度图
    img_gray=img.convert("L")
    plt.rcParams["image.cmap"]="gray"
    return img_gray
def img_change3(img):
    #反色
    img_invert=ImageOps.invert(img_change2(img))
    return img_invert
def img_change4(img,num):
    #高斯模糊
    new_img=img_change3(img)
    img_gaussian=new_img.filter(ImageFilter.GaussianBlur(num))
    return img_gaussian
def img_change5(img,num):
    #颜色减淡
    new_img=img
    w,h=img.size
    img_gray=img_change2(img)
    img_gaussian=img_change4(img,num)
    for x in range(w):
        for y in range(h):
            pos=(x,y)
            A=img_gray.getpixel(pos)
            B=img_gaussian.getpixel(pos)
            img_gray.putpixel(pos,min(int(A+A*B/(256.0-B*1.0)),255))
    return img_gray
def page_1():
    """我的主页"""
    st.write("作者的简介")
    st.write("姓名:李……")
    text = """大家好！我叫李……,在2011年7月22日出生于安徽合肥，今年我是13岁。做这个网站也是为了简单的展示一些日常生活之类的一些事情,也发一些自己喜欢听的歌。
             希望我做的网站可以给大家带来快乐♪٩(´ω`)و♪！"""
    st.write("个性签名:"+text)
    st.write("感谢参观,wala li longla!（｡･ω･｡)つ━☆・*。")
def page_2():
    """我的兴趣推荐"""
    #学生使用write()、image()、audio()等自行发挥
    st.write('我的音乐分享')
    st.write('----------------------------------------------------------------反深代词----------------------------------------------------------------')
    st.image("images/反深代词.png")
    for music in musics:
        st.write(musics_names[musics.index(music)]+"(音量有些大,可以先调`小`一点哦)")
        with open("musics/"+music,"rb") as f:
            mymp3=f.read()
        st.audio(mymp3,format='audio/wav',start_time=0)
    st.write('------')
    st.write('我的网站分享')
    with open("webs.txt","r",encoding="utf-8") as f:
        webs_list=f.read().split('\n')
    for i in range(len(webs_list)):
        webs_list[i]=webs_list[i].split('#')
    webs={}
    for i in webs_list:
        webs[i[0]]=i[1]
    webs_names=[]
    for i in webs:
        webs_names.append(i)
    webs["其他的网站"]=""
    webs_names.append("其他的网站")
    go = st.selectbox('网页跳转:',webs_names)
    if go !="其他的网站":
        try:
            st.link_button(go, webs[go])
        except:
            webs.pop(go)
            with open("webs.txt","w",encoding="utf-8") as f:
                message=''
                for k,v in webs.items():
                    message+=str(k)+'#'+str(v)+'\n'
                message=message[:-1]
                f.write(message)
            st.write("抱歉!之前的路径有些问题(是别人的局域网),已为您删除!")
    else:
        name=st.text_input("请输入要跳转的网站名称",
                            help="名称")
        web=st.text_input("请输入要跳转的网站网址(请不要输入局域网,谢谢🙏)",
                            help="网址")
        try:
            if st.button("确认"):
                response = requests.get(web)
                if web in webs.values():
                    st.write("当前列表已包含"+web+" !请勿重复输入!")                 
                elif response.status_code==200:
                    with open("webs.txt","a",encoding="utf-8") as f:
                        m="\n"+name+"#"+web
                        f.write(m)
                    st.link_button(name,web)
                else:
                    st.write("输入有误,请重新输入!")
        except:
            st.write("输入有误,请重新输入!")
            
def page_3():
    """我的图片工具箱"""
    #换色
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        # s2=st.toggle('改色1')
        # s3=st.toggle('改色2')
        # s4=st.toggle('改色3')
        # s5=st.toggle('转灰度图')
        # s6=st.toggle('反色')
        # s7=st.toggle('高斯模糊')
        # s8=st.toggle('素描画(建议使用此时取消前三个)')
        # if s2:
        #     img=img_change1(img,0,2,1)
        # if s3:
        #     img=img_change1(img,1,2,0)
        # if s4:
        #     img=img_change1(img,1,0,2)
        # if s5:
        #     img=img_change2(img)
        # if s6:
        #     img=img_change3(img)
        # if s7:
        #     img=img_change4(img,5)
        # if s8:
        #     img=img_change5(img,5)
        # st.image(img)
        # img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5=st.tabs(["原图","改色1","改色2","改色3","素描画"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change1(img,0,2,1))
        with tab3:
            st.image(img_change1(img,1,2,0))
        with tab4:
            st.image(img_change1(img,1,0,2))
        with tab5:
            st.image(img_change5(img,5))
def page_4():
    """我的计算器"""
    op = st.selectbox(
        label = '请输入您的需求',
        options = ('加法', '减法', '乘法','除法','乘方'),
        index = 2,
        format_func = str,
        help = '敬请期待更多计算方法！'
    )
    if op == '加法':
        num1 = st.number_input(label = '请输入第一个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='第一个加数'
        )
        num2 = st.number_input(label = '请输入第二个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='第二个加数'
        )
        st.write(num1+num2)
    elif op == '减法':
        num1 = st.number_input(label = '请输入第一个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='被减数'
        )
        num2 = st.number_input(label = '请输入第二个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='减数'
        )
        st.write(num1-num2)
    elif op == '乘法':
        num1 = st.number_input(label = '请输入第一个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='第一个因数'
        )
        num2 = st.number_input(label = '请输入第二个数字', 
            min_value=0, 
            max_value=10000000000, 
            value=5000000000, 
            step=1, 
            help='第二个因数'
        )
        st.write(num1*num2)
    elif op == '除法':
        num1 = st.number_input(label = '请输入第一个数字', 
            min_value=0, 
            max_value=1000000000, 
            value=500000000, 
            step=1, 
            help='被除数'
        )
        num2 = st.number_input(label = '请输入第二个数字', 
            min_value=0, 
            max_value=1000000000, 
            value=500000000, 
            step=1, 
            help='除数'
        )
        st.write(num1*1.0/num2)
    elif op == '乘方':
        num1 = st.number_input(label = '请输入第一个数字', 
            min_value=-100, 
            max_value=100, 
            value=50, 
            step=1, 
            help='底数'
        )
        num2 = st.number_input(label = '请输入第二个数字', 
            min_value=0, 
            max_value=200, 
            value=100, 
            step=1, 
            help='指数'
        )
        st.write(num1**num2)
def page_5():
    """我的智慧词典"""
    st.write('智慧词典')
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split('\n')
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times={}
    words={}
    for i in words_list:
        words[i[1]]=[int(i[0]),i[2]]
    for i in times_list:
        times[int(i[0])]=int(i[1])
    word=st.text_input("请输入要查询的单词",
                       help="难道单词就只能输入英文吗?")  
    if word=="":
        word=" "   
    if ord(word[:1])>128:
        st.write("恭喜你发现隐藏功能!")
        j=1
        for i in words_list:
            if word in i[2]:
                st.markdown("**"+str(j)+"、**")
                j+=1
                st.write(i[2])
                st.write(i[1])
                st.write("这是词典的第"+str(i[0])+"个单词")
    elif word in words:
        st.write(words[word][1])
        n=words[word][0]
        if n in times:
            times[n]+=1
        else:
            times[n]=1
        st.write("这是词典的第"+str(words[word][0])+"个单词")
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message=''
            for k,v in times.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write("这个单词的查询次数是:"+str(times[n]))
    elif word!=" ":
        op = st.selectbox(label = '你需要将此单词添加到单词表吗?(不要乱写,谢谢配合!)',
                          options = ('需要', '不需要'),
                          index=1,
                          format_func = str,
                          help = '谢谢配合！'
        )
        if op == "需要":
            dc=st.text_input("请输入单词的词性+意思(按下Enter↩︎就行啦,谢谢!)",
                            help="例如n.苹果(词性.意思)")
            if dc !="":
                with open("words_space.txt","a",encoding="utf-8") as f:
                    m="\n"+str(int(words_list[-1][0])+1)+"#"+word+"#"+dc+"#"
                    f.write(m)
    if word=='python':
        st.code('''
            # 恭喜你触发彩蛋，这是一行python代码
            print("hello world")''')
    elif word=='c++'or word=='C++':
        st.code('''
                //恭喜你触发彩蛋，这是几行C++框架
                #include <iostream>
                using namespace std;
                int main(){
                
                    return 0;
                }
            ''',language='C++')
    elif word=="birthday":
        st.balloons()
    elif word=="snow"or word=="winter":
        st.snow()
    elif word=="李元梁" or word == "lyl":
        st.write("HaHa,你怎么知道我的名字的！！！😄")
        st.write("加我QQ:3627921142")
        st.balloons()
    elif word=="unordered_map":
        st.code('''
                //恭喜你触发彩蛋，这是几行C++框架
                #include <iostream>
                unordered_map<键的类型,值的类型>mp(预留空间);//哈希表
                using namespace std;
                int main(){
                
                    return 0;
                }
            ''',language='c++')
def page_6():
    """我的留言区"""
    st.write("我的留言区")
    #从文件中加载内容，并处理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list =f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]= messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message(i[3]):
            st.write(i[1],':',i[2])
    name = st.text_input("请输入您的名字:")
    new_massage = st.text_input("请输入您的留言:")
    tx = st.text_input("请输入您的头像(一个emoji表情):")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_massage,tx])
        messages = ''
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            for i in messages_list:
                messages+=i[0]+'#'+i[1]+"#"+i[2]+"#"+i[3]+"\n"
            messages=messages[:-1]
            f.write(messages)
def page_7():
    """我的朋友圈"""
    #北京
    st.write("北京之旅2023.8.7-2023.8.14")
    st.image("images/头像.png")
    #天坛
    st.write("天坛")
    st.write("这是在天坛公园的皇穹宇,那天人好多，只能在旁边拍照了……")
    st.image("images/北京1.png")
    #长城
    st.image("images/头像.png")
    st.write("长城")
    st.write('这是在八达岭长城,导游说前半段又陡又长,可以坐滑车,不要坐缆车(缆车太贵了,还是单程票),虽然加在一起才爬一次长城,但已经把我累"死"了')
    st.image("images/北京2.png")
    #游乐园
    st.image("images/头像.png")
    st.write("地点未知")
    st.write('这是在地点未知,我们在"冰雪乐园"玩')
    st.image("images/北京3.png")
    #鸟巢
    st.image("images/头像.png")
    st.write("鸟巢(旁边)")
    st.write('这是在鸟巢和水立方(旁边),一直在晒太阳,拍完照之后不知道咋了,我走丢了……只能在大巴车那等😣')
    st.image("images/北京4.png")
    #水立方
    st.image("images/头像.png")
    st.image("images/北京5.png")
    #环球影城
    st.image("images/头像.png")
    st.write("环球影城")
    st.write('''这是在环球影城(就是一个一根雪糕60RMB的游乐园,一个项目排队两个小时的游乐园……)的门口,然后入园排队了2个小时……里面项目玩起来都可以,只是物价有点高。我妈妈说
             过山车好玩,玩了3,4次,我挺后悔的,但让我再去一次我还是不敢玩……''')
    st.image("images/北京6.png")
    #"赶海"
    st.write('"赶海"之旅2024.3.23-2023.3.24')
    st.image("images/头像.png")
    st.write("淮河入海口")
    st.write('这是在淮河入海口,我爸打着赶海的名号带我们去"喂"蚊子……但是我家的金毛玩的挺wala li longla(开心)的,玩的一身上都是"烂泥"……')
    st.image("images/赶海.png")
    #皖南
    st.write("皖南之旅2024.5.4-2024.5.5")
    st.image("images/头像.png")
    st.write("这次是我爸和他的朋友带我们(我,我姐,我妈,和他朋友的家人)一起去了皖南(是在五一的时候)那天是五一的最后两天,最后上学还迟到了😜……")
    st.write("这几张照片是他们几个在抓鱼,与其说是抓鱼,不如说是无聊,几个人拿了一堆石头想拦住路过的鱼,不出所料,一直没抓到……")
    st.image("images/皖南1.png")
    st.image("images/头像.png")
    st.write("这张是我,我当时下午要上学,鞋子不能湿,但是穿的运动鞋😭……")
    st.write("简直是世界上最近却又最远的距离!")
    st.image("images/皖南2.png")
def page_8():
    st.image("images/头像.png")
    st.write("这是我的第一个python老师:夏温老师")
    st.image("images/python1.png")
    st.image("images/头像.png")
    st.write("这是我的第二个python老师:夸夸老师(最开始的聊天找不到了……这是最早的一个消息……)")
    st.image("images/python2.png")
    st.image("images/头像.png")
    st.write("这是我的第一个创赛营的python老师:江江老师")
    st.image("images/python3.png")
    st.image("images/头像.png")
    st.write("这是我的现在(也是第二个创赛营)的python老师:小彭老师")
    st.image("images/python4.png")
    st.image("images/头像.png")
    st.write("这是我的现在(第三个)创赛营的python老师:小乐老师")
    st.image("images/python5.png")
def page_9():
    '''我的基本素养'''
    score = 0
    st.write('先来做几个测试题吧，看看你对周深了解多少')
    st.write('')
    st.write('')
    col1_1, col1_2, col1_3, col1_4 = st.columns([1, 1, 1, 1])
    choice1 = st.radio(
        '周深的生日是?(送分题)',
        random.choice(['1992年9月29日','1993年9月29日','1992年9月26日','1993年9月26日'])
    )
    if choice1=='1992年9月29日':
        score+=5
    else:
        score-=25
    st.write('')
    st.write('')
    choice2 = st.radio(
        '深的深的发行日期是?',
        random.choice(['2017年10月26日','2017年11月6日','2017年11月16日','2017年11月26日'])
    )
    if choice2=='2017年10月26日':
        score+=15
    else:
        score-=10
    choice3 = st.radio(
        '周深的第二个专辑的第3首歌是?',
        random.choice(['少管我','警报','大鱼','重启'])
    )
    if choice3=='重启':
        score+=15
    elif choice3=="大鱼":
        score-=20
    else:
        score-=10
    choice5 = st.radio(
        '周深的第二个专辑的价格是?',
        random.choice(['30$','30RMB','50$','50RMB'])
    )
    if choice5=='30RMB':
        score+=15
    else:
        score-=25
    #50
    choice6 = st.radio(
        '周深的第二个专辑的名称是(送分题)?',
        random.choice(['反深代词','深的深','玫瑰与小鹿','小美满'])
    )
    if choice3=='反深代词':
        score+=15
    else:
        score-=20
    st.write('下面那些歌是周深的?')
    c1=st.checkbox("消夏图")
    c2=st.checkbox("Hi")
    c3=st.checkbox("Intro")
    c4=st.checkbox("花开忘忧")
    if c1 and c4 and ~c2 and ~c3:
        score+=35
    else:
        score-=5
    if st.button("交卷"):
        if score>0:
            st.write("恭喜🎉,本次问卷你get到了`"+str(score)+"`分!")
        else:
            st.write("很遗憾,本次问卷你get到了`0`分……")
if page == "我的主页":
    page_1()
if page == "我的兴趣推荐":
    page_2()
elif page == "我的图片工具箱":
    page_3()
elif page == "我的计算器":
    page_4()
elif page == "我的智慧词典":
    # st.write("智慧词典加载中……")
    # # 初始化进度条为0
    # progress = st.sidebar.progress(0)
    # # 模拟耗时操作（这里只是一个循环）
    # for i in range(100):
    #     # 更新进度条
    #     progress.progress(i + 1)
    #     time.sleep(0.03)  # 短暂休眠模拟实际运算时间
    # # 当所有任务完成后，设置进度为1
    # progress.progress(0)
    # st.write("智慧词典加载成功!")
    page_5()
elif page == "我的留言区":
    page_6()
elif page == "我的朋友圈":
    page_7()
elif page == "我的python旅程":
    page_8()
elif page=="生米的基本素养":
    page_9()
