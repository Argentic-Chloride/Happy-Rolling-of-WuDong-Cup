import tkinter 
import xlrd
import tkinter.ttk
import random

class EntryWithPlaceholder(tkinter.Entry):#Placeholder功能模块
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',):
        super().__init__(master)#Placeholder默认值"PLACEHOLDER"，默认颜色灰色

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in) #绑定鼠标点入操作
        self.bind("<FocusOut>", self.foc_out)#绑定鼠标点出操作

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get(): #如果Entry没有得到值
            self.put_placeholder()#那么将默认值放上去

root = tkinter.Tk()
root.wm_attributes('-topmost',1)#窗口默认置顶
root.title('Happy Rolling of 舞动杯') #标题
root['height'] = 200 #窗口高度
root['width'] = 375 #窗口宽度

data = xlrd.open_workbook('Songs_list.xls')#歌曲列表读入

shenxian = data.sheet_by_name('shenxian') #神仙组歌曲roll列表读入，下同
julao = data.sheet_by_name('julao')
yeye = data.sheet_by_name('yeye')

global sx_artist,sx_songname,sx_package,sx_difficulty,sx_Diffnum
sx_package = shenxian.col_values(0)#歌曲对应曲包
sx_songname = shenxian.col_values(1)#歌曲名称
sx_artist = shenxian.col_values(2)#歌曲艺术家
sx_difficulty = shenxian.col_values(3)#歌曲难度等级
sx_Diffnum = shenxian.col_values(4)#歌曲定数，下同

global jl_artist,jl_songname,jl_package,jl_difficulty,jl_Diffnum
jl_package = julao.col_values(0)
jl_songname = julao.col_values(1)
jl_artist = julao.col_values(2)
jl_difficulty = julao.col_values(3)
jl_Diffnum = julao.col_values(4)

global yy_artist,yy_songname,yy_package,yy_difficulty,yy_Diffnum
yy_package = yeye.col_values(0)
yy_songname = yeye.col_values(1)
yy_artist = yeye.col_values(2)
yy_difficulty = yeye.col_values(3)
yy_Diffnum = yeye.col_values(4)

global sx_song_totalnum,jl_song_totalnum,yy_song_totalnum
sx_song_totalnum = len(sx_package)#神仙组曲库歌曲总数量，用于roll number
jl_song_totalnum = len(jl_package)
yy_song_totalnum = len(yy_package)

def sx_rolling():
    global sx_song_totalnum
    rand = random.randint(1,sx_song_totalnum)
    #print(sx_artist[rand-1])
    entry_package = EntryWithPlaceholder(root,sx_package[rand-1])
    entry_package.place(x=85,y=60,width=280,height=20)
    entry_package['state']='disabled'

    entry_artist = EntryWithPlaceholder(root, sx_artist[rand-1])
    entry_artist.place(x=85,y=85,width=280,height=20)
    entry_artist['state']='disabled'

    entry_difficulty = EntryWithPlaceholder(root, sx_difficulty[rand-1])
    entry_difficulty.place(x=85,y=110,width=280,height=20)
    entry_difficulty['state']='disabled'

    entry_Diffnum = EntryWithPlaceholder(root, sx_Diffnum[rand-1])
    entry_Diffnum.place(x=85,y=135,width=280,height=20)
    entry_Diffnum['state']='disabled'

    entry_songname = EntryWithPlaceholder(root, sx_songname[rand-1])
    entry_songname.place(x=85,y=160,width=280,height=20)
    entry_songname['state']='disabled'

def jl_rolling():
    global jl_song_totalnum
    rand = random.randint(1,jl_song_totalnum)
    #print(jl_artist[rand-1])
    entry_package = EntryWithPlaceholder(root,jl_package[rand-1])
    entry_package.place(x=85,y=60,width=280,height=20)
    entry_package['state']='disabled'

    entry_artist = EntryWithPlaceholder(root, jl_artist[rand-1])
    entry_artist.place(x=85,y=85,width=280,height=20)
    entry_artist['state']='disabled'

    entry_difficulty = EntryWithPlaceholder(root, jl_difficulty[rand-1])
    entry_difficulty.place(x=85,y=110,width=280,height=20)
    entry_difficulty['state']='disabled'

    entry_Diffnum = EntryWithPlaceholder(root, jl_Diffnum[rand-1])
    entry_Diffnum.place(x=85,y=135,width=280,height=20)
    entry_Diffnum['state']='disabled'

    entry_songname = EntryWithPlaceholder(root, jl_songname[rand-1])
    entry_songname.place(x=85,y=160,width=280,height=20)
    entry_songname['state']='disabled'

def yy_rolling():
    global yy_song_totalnum
    rand = random.randint(1,yy_song_totalnum)
    #print(jl_artist[rand-1])
    entry_package = EntryWithPlaceholder(root,yy_package[rand-1])
    entry_package.place(x=85,y=60,width=280,height=20)
    entry_package['state']='disabled'

    entry_artist = EntryWithPlaceholder(root, yy_artist[rand-1])
    entry_artist.place(x=85,y=85,width=280,height=20)
    entry_artist['state']='disabled'

    entry_difficulty = EntryWithPlaceholder(root, yy_difficulty[rand-1])
    entry_difficulty.place(x=85,y=110,width=280,height=20)
    entry_difficulty['state']='disabled'

    entry_Diffnum = EntryWithPlaceholder(root, yy_Diffnum[rand-1])
    entry_Diffnum.place(x=85,y=135,width=280,height=20)
    entry_Diffnum['state']='disabled'

    entry_songname = EntryWithPlaceholder(root, yy_songname[rand-1])
    entry_songname.place(x=85,y=160,width=280,height=20)
    entry_songname['state']='disabled'
    
labelFormat = tkinter.Label(root,text='请选择Happy Rolling组别：'
                            ,justify=tkinter.RIGHT,width=50)
labelFormat.place(x=10,y=5,width=150,height=20)
comboFormat = tkinter.ttk.Combobox(root,width=300)

def resetentry():
    entry_difficulty = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
    entry_difficulty.place(x=85,y=110,width=280,height=20)
    entry_difficulty['state']='disabled'
    
    entry_package = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
    entry_package.place(x=85,y=60,width=280,height=20)
    entry_package['state']='disabled'

    entry_artist = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
    entry_artist.place(x=85,y=85,width=280,height=20)
    entry_artist['state']='disabled'

    entry_songname = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
    entry_songname.place(x=85,y=160,width=280,height=20)
    entry_songname['state']='disabled'

    entry_Diffnum = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
    entry_Diffnum.place(x=85,y=135,width=280,height=20)
    entry_Diffnum['state']='disabled'
    
def shenxian_label():#神仙组
    global label_sx
    label_sx = tkinter.Label(root,text='当前Happy Rolling组别：神仙组'
                                  ,justify=tkinter.RIGHT,width=150)
    label_sx.place(x=15,y=35,width=180,height=15)

    global button_sx_rolling 
    button_sx_rolling = tkinter.Button(root,text='Rolling!',command=sx_rolling)
    button_sx_rolling.place(x=300,y=10)
    resetentry()

def julao_label():
    global label_jl
    label_jl = tkinter.Label(root,text='当前Happy Rolling组别：巨佬组'
                                  ,justify=tkinter.RIGHT,width=150)
    label_jl.place(x=15,y=35,width=180,height=15)

    global button_jl_rolling 
    button_jl_rolling = tkinter.Button(root,text='Rolling!',command=jl_rolling)
    button_jl_rolling.place(x=300,y=10)
    resetentry()

def yeye_label():
    global label_yy
    label_yy = tkinter.Label(root,text='当前Happy Rolling组别：椰叶组'
                                  ,justify=tkinter.RIGHT,width=155)
    label_yy.place(x=15,y=35,width=185,height=15)

    global button_yy_rolling 
    button_yy_rolling = tkinter.Button(root,text='Rolling!',command=yy_rolling)
    button_yy_rolling.place(x=300,y=10)
    resetentry()

def no_label():
    global label_no
    label_no = tkinter.Label(root,text='当前Happy Rolling组别：上面选一个'
                                  ,justify=tkinter.RIGHT,width=200)
    label_no.place(x=15,y=35,width=200,height=15)
    resetentry()

def doalllabel():#全做一遍，目的是创建变量
    shenxian_label()
    julao_label()
    yeye_label()
    no_label()
    
def forgetalllabel():#清屏，防止Entry占屏幕引起程序错误
    global label_sx,label_yy,label_jl,label_no
    label_sx.place_forget();
    label_yy.place_forget();
    label_jl.place_forget();
    label_no.place_forget();
    global button_sx_rolling,button_jl_rolling,button_yy_rolling
    button_sx_rolling.place_forget()
    button_jl_rolling.place_forget()
    button_yy_rolling.place_forget()

comboFormat['value']=('','神仙组','巨佬组','椰叶组') #参考文献类型combobox候选项
comboFormat.current(0);
doalllabel();forgetalllabel();
no_label();
comboFormat.place(x=160,y=5,width=75,height=20)

def comboChange(event):#如果combobox选项改变，那么将表单转成改变后对应的参考文献表单
    global ref_format
    ref_format=comboFormat.get()
    forgetalllabel();
    if ref_format=='神仙组':
        shenxian_label();
    elif ref_format=='巨佬组':
        julao_label();
    elif ref_format=='椰叶组':
        yeye_label();
    elif ref_format=='':
        no_label();

label_package = tkinter.Label(root,text='所在曲包：',justify=tkinter.RIGHT,width=50,fg='blue')
label_package.place(x=9,y=60,width=75,height=15)
entry_package = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
entry_package.place(x=85,y=60,width=280,height=20)
entry_package['state']='disabled'

label_artist = tkinter.Label(root,text='艺 术 家：',justify=tkinter.RIGHT,width=50,fg='blue')
label_artist.place(x=9,y=85,width=75,height=15)
entry_artist = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
entry_artist.place(x=85,y=85,width=280,height=20)
entry_artist['state']='disabled'

label_difficulty = tkinter.Label(root,text='难度等级：',justify=tkinter.RIGHT,width=50,fg='blue')
label_difficulty.place(x=9,y=110,width=75,height=15)
entry_difficulty = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
entry_difficulty.place(x=85,y=110,width=280,height=20)
entry_difficulty['state']='disabled'

label_Diffnum = tkinter.Label(root,text='歌曲定数：',justify=tkinter.RIGHT,width=50,fg='blue')
label_Diffnum.place(x=9,y=135,width=75,height=15)
entry_Diffnum = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
entry_Diffnum.place(x=85,y=135,width=280,height=20)
entry_Diffnum['state']='disabled'

label_songname = tkinter.Label(root,text='歌曲名称：',justify=tkinter.RIGHT,width=50,fg='blue')
label_songname.place(x=9,y=160,width=75,height=15)
entry_songname = EntryWithPlaceholder(root, "不告诉你，roll了才知道")
entry_songname.place(x=85,y=160,width=280,height=20)
entry_songname['state']='disabled'

comboFormat.bind('<<ComboboxSelected>>',comboChange)#绑定combobox选择改变操作

if __name__=="__main__":
    root.mainloop()
