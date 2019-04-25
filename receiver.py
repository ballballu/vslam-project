import os
import thulac
thu = thulac.thulac()

distance=[]
direction=[]
destination = []
key_words=['教室','实验室','走廊','客厅','厨房']
def getcommand():
    if os.access("received.txt",os.F_OK):
        f = open("received.txt")
        r_data = f.read()
        f.close()
        #os.remove("received.txt")
        if '语音' in r_data:
            Mode = 'SPEECH'
        data = r_data[5:]
    else:
        Mode= 'NONE'
        data=[]
    return Mode, data

def speech_control(data):
        
        words = thu.cut(data)
        print(data)
        print(words)
        dir_command = []
        dis_command = []
        des_command = []
        
        for i in range(len(words)):
            #提取出要走的方向和距离
            if words[i][0] in key_words:
                destination.append([words[i][0],i])
            elif (words[i][1]=='f' and i!=0 and words[i-1][1]=='p') or (words[i][1]=='v' and len(words[i][0])>1):
                direction.append([words[i][0],i])
            elif words[i][1]=='m':
                distance.append([words[i][0],i])

        if len(destination)!=0:
            for i in range(len(destination)):
                des_command.append( [destination[i][0], key_words.index(destination[i][0])] )
            print(des_command)
        elif len(direction)!=0:   
            for i in range(len(direction)):
                if '前' in direction[i][0]:
                    dir_command.append( 'FORWARD' )
                elif ('后' or '退') in direction[i][0]:
                    dir_command.append( 'BACKWARD' )
                elif '左' in direction[i][0]:
                    dir_command.append( 'LEFT' )
                elif '右' in direction[i][0]:
                    dir_command.append( 'RIGHT' )
                if i < len(distance):
                    dis_command.append( int(distance[i][0]) )
                else:
                    dis_command.append( int(1) )
            print(dir_command)
            print(dis_command)
        else:
            print('无法执行的指令')
    




# def button_control(data):

# def gravity_control(data):

#def gesture_control(data):

def Controller():
    
    mode,data = getcommand()
    if mode == 'NONE':
        print("wait for command")
    else:
        if mode == 'SPEECH':
            speech_control(data)
        '''elif mode == 'BUTTON':
            button_control(data)
        elif mode == 'GRAVITY':
            gravity_control(data)
        elif mode == 'GESTURE':
            gesture_control(data)'''

Controller()
