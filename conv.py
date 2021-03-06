
DEF_Y_MAX= 9000
DEF_Y_MOD=-1


#S 0 0 100 -100 0 1 0 N
#S LTX LTY RBX RBY 0 1 0 N
#Line X1 Y1 X2 Y2 8 0 0 0
def changeStoLine(istr):
    #print("changeStoLine")    
    if not istr.startswith('S ') :
        #print("no s")
        return ""
    sa = istr.split()
    rets = ""
    ltx = sa[1]
    lty = sa[2]
    rbx = sa[3]
    rby = sa[4]
    rets += "Line "+ ltx + " "+ lty + " "+ ltx + " "+ rby + " 8 1 0 0 \n"
    rets += "Line "+ ltx + " "+ rby + " "+ rbx + " "+ rby + " 8 1 0 0 \n"
    rets += "Line "+ rbx + " "+ rby + " "+ rbx + " "+ lty + " 8 1 0 0 \n"
    rets += "Line "+ rbx + " "+ lty + " "+ ltx + " "+ lty + " 8 1 0 0 \n"
    return rets
    
#P 5 0 1 0 0 0 0 -200 200 -200 200 0 0 0 N
def changePtoLine(istr):
    #print("changePtoLine")    
    if not istr.startswith('P ') :
        #print("no P")
        return ""
    sa = istr.split()
    rets = ""
    lineCnt = int(sa[1])
    for i in range(lineCnt-1):
        idx = i * 2 + 5
        #print(idx)
        ltx = sa[idx + 0]
        lty = sa[idx + 1]
        rbx = sa[idx + 2]
        rby = sa[idx + 3]
        rets += "Line "+ ltx + " "+ lty + " "+ rbx + " "+ rby + " 8 1 0 0 \n"

    return rets

#DRAW
# pin
# X ~ 1 200 -50 100 L 50 50 1 1 I
# X ~ ~ 50 -200 99 U 50 50 1 1 I
# X RST_N 10 900 -1150 200 U 50 50 0 0 U
# X Text PinNumber X Y Length UpDownLeftRight 50 50 1 1 I
def changeXtoPin(istr):
    #print("changeXtoPin")    
    if not istr.startswith('X ') :
        #print("no X")
        return ""
    sa = istr.split()
    rets = ""
    name = sa[1]
    pinnumber = sa[2]
    x = int(sa[3])
    y = int(sa[4])
    leng = int(sa[5])
    dir = sa[6]
    if dir == "D":
        #上方向
        #Pin X Y X Y+Len 0
        #Name "FAT" X Y-12 70 282
        #No "1" X Y+50 70 264
        rets += "Pin "+ str(x) + " "+ str(y-leng) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x-12) + " "+ str(y-leng) + " 70 282\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x) + " "+ str(y+50-leng) + " 70 264\n"
    elif dir == "U":
        #Pin X Y X Y-Len 0
        #Name "FAT" X Y+12 70 280
        #No "1" X Y-50 70 266
        rets += "Pin "+ str(x) + " "+ str(y+leng) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x) + " "+ str(y+12+leng) + " 70 280\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x) + " "+ str(y-50+leng) + " 70 266\n"
    elif dir == "L":
        #右方向
        #Pin X Y X+Len Y 0
        #Name "FAT" X-18 Y 70 26
        #No "1" X+50 Y 70 264
        rets += "Pin "+ str(x-leng) + " "+ str(y) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x-18-leng) + " "+ str(y) + " 70 26\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x+100-leng) + " "+ str(y) + " 70 10\n"
    elif dir == "R":
        #Pin X Y X-Len Y 0
        #Name "FAT" X+12 Y 70 24
        #No "1" X-50 Y 70 10
        rets += "Pin "+ str(x+leng) + " "+ str(y) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x+12+leng) + " "+ str(y) + " 70 24\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x-50+leng) + " "+ str(y) + " 70 10\n"
    return rets

# T 0 50 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -300 50 0 0 0 FFF Normal 0 C C
#T 900 350 -400 50 0 0 0 DA Normal 0 C C
# Text "test" 2100 7700 70 8
#Text "DA" x y 70 264
#Text "DA" x y 70 520
#Text "DA" x y 70 776
def changeTtoText(istr):
    #print("changeXtoPin")    
    rets = ""
    if not istr.startswith('T ') :
        #print("no T")
        return ""
    
    sa = istr.split()
    if sa[1] == "900":
        dir = "R"
    else:
        dir = "D"
    x = int(sa[2])
    y = int(sa[3])
    leng = int(sa[4])
    txt = sa[8]
    if dir == "D":
        rets += 'Text "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 8\n"
    elif dir == "R":
        rets += 'Text "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 264\n"
    return rets



# 円弧
#A X Y  Y 634 -634 0 1 0 N 150 0 150 -200
#A 200 0 50 -1799 -1 0 1 0 N 150 0 250 0
#A X Y  50 -1799 -1 0 1 0 N 150 0 250 0
#Arc X Y 100 270 97 8 1 0 0
#Arc X Y 100 180 0 8 1 0 0 
def changeAToArc(istr):
    rets = ""
    if not istr.startswith('A ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[1])
    y = int(sa[2])
    fx = int(sa[10])
    fy = int(sa[11])
    lx = int(sa[12])
    ly = int(sa[13])

    # left
    # up
    # down 
    # right
    rets += "Arc "+ str(x) + " "+ str(y) + " 100 "
    arckakudo = " 0 180 "
    if fx == lx:
        if ly > fy:
            arckakudo = " 270 90 "
        elif ly < fy:
            arckakudo = " 90 270 "
        
    if ly == fy:
        if lx > fx:
            arckakudo = " 180 0 "
        elif lx < fx:
            arckakudo = " 0 180 "

    rets += arckakudo + " 8 1 0 0 \n"
    return rets

#円
#C -80 0 20 0 0 0 N
#Arc X Y 20 0 344 8 1 0 0
def changeCToArc(istr):
    rets = ""
    if not istr.startswith('C ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[1])
    y = int(sa[2])
    rets += "Arc "+ str(x) + " "+ str(y) + "  20 0 344 8 1 0 0 \n"
    return rets



# --------------------------------------------------------

# text 
#Text Notes 2850 7250 0    50   ~ 0
#BT_RX_IND
def changeSchTextNoteTtoText(istr, txt):
    #print("changeXtoPin")    
    rets = ""
    if not istr.startswith('Text Notes ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[2])
    y = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    txt = txt.strip()
    rets += 'Text "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 8\n"
    return rets

# text 
#Text GLabel 7050 6300 0    50   Output ~ 0
#BT_RX_IND
def changeSchTextGLabeltoName(istr, txt):
    #print("changeXtoPin")    
    rets = ""
    if not istr.startswith('Text GLabel ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[2])
    y = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    dir = sa[6]
    txt = txt.strip()
    lasttype = 8
    if dir == "Output":
        lasttype = 851976
    elif dir == "Input":
        lasttype = 917512
    rets += 'Name "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 "+ str(lasttype) +" \n"
    return rets

# text 
#Text Label 6850 5700 0    50   ~ 0
#GPIO0
def changeSchTextLabeltoName(istr, txt):
    #print("changeXtoPin")    
    rets = ""
    if not istr.startswith('Text Label ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[2])
    y = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    txt = txt.strip()
    rets += 'Name "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 8\n"
    return rets


# wire 赤い線
def changeWWLtoLine(istr):
    rets = ""
    sa = istr.split()
    x1 = int(sa[0])
    y1 = int(sa[1])*DEF_Y_MOD + DEF_Y_MAX
    x2 = int(sa[2])
    y2 = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    rets += "Line "+ str(x1) + " "+ str(y1) + " "+ str(x2) + " "+ str(y2) + " 8 0 0 0 \n"
    return rets

# wirebus 青い太い線
def changeWBusLtoLine(istr):
    rets = ""
    sa = istr.split()
    x1 = int(sa[0])
    y1 = int(sa[1])*DEF_Y_MOD + DEF_Y_MAX
    x2 = int(sa[2])
    y2 = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    rets += "Line "+ str(x1) + " "+ str(y1) + " "+ str(x2) + " "+ str(y2) + " 242 2 0 0 \n"
    return rets


# 接点
#Connection ~ X Y
#Junc X Y
def changeConnectToJunc(istr):
    rets = ""
    if not istr.startswith('Connection ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[2])
    y = int(sa[3])*DEF_Y_MOD + DEF_Y_MAX
    rets += "Junc "+ str(x) + " "+ str(y) + " \n"
    return rets

