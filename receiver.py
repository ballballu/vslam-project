import os
import thulac
import time
thu = thulac.thulac()

distance=[]
direction=[]
destination = []
key_words=['教室','实验室','走廊','客厅','厨房']

''' 
    读取 received.txt的原始内容
    输出为 command.txt 
    地点模式 A address_code1 address_code2...
    方向前进模式 D direction_code1 distance1 direction_code2 distance2....
    direction_code: 1-forward  3-backward 4-left 2-right
    address_code: 教室-1, 实验室-2,  走廊-3, 客厅-4, 厨房-5

'''



def getcommand():
    if os.access("received.txt",os.F_OK):
        f = open("received.txt")
        r_data = f.read()
        f.close()
        os.remove("received.txt")
        if '语音' in r_data:
            Mode = 'SPEECH'
            data = r_data[5:]
        elif '按键' in r_data:
            Mode= 'BUTTON'
            data = r_data[5:]
        elif '摇杆' in r_data:
            Mode = 'JOYSTICK'
            data = r_data[5:]
        elif '重力' in r_data:
            Mode = 'GRAVITY'
            data = r_data[5:]
        elif '路径' in r_data:
            Mode = 'GESTURE'
            data = r_data[5:]
    else:
        Mode = 'NONE'
        data = []

    return Mode, data

def speech_control(data):
        
        words = thu.cut(data)
        print(data)
        print(words)
        dir_command = ""
        dis_command = ""
        des_command = ""
        command = ""
        for i in range(len(words)):
            #提取出要走的方向和距离
            if words[i][0] in key_words:
                destination.append([words[i][0],i])
            elif (words[i][1]=='f' and i!=0 and words[i-1][1]=='p') or (words[i][1]=='v' and len(words[i][0])>1):
                direction.append([words[i][0],i])
            elif words[i][1]=='m':
                distance.append([words[i][0],i])

        if len(destination)!=0:
            des_command = "A"
            for i in range(len(destination)):
                #des_command.append( int(key_words.index(destination[i][0])+1) )
                des_command = des_command + ' ' + str(key_words.index(destination[i][0])+1)
            print(des_command)
            command = des_command
        elif len(direction)!=0:
            dir_command = "DIR"   
            for i in range(len(direction)):
                if '前' in direction[i][0]:
                    #dir_command.append( int(1) )
                    dir_command = dir_command + " " + str(1)
                elif ('后' or '退') in direction[i][0]:
                    #dir_command.append( int(3) )
                    dir_command = dir_command + " " + str(3)
                elif '左' in direction[i][0]:
                    #dir_command.append( int(4) )
                    dir_command = dir_command + " " + str(4)
                elif '右' in direction[i][0]:
                    #dir_command.append( int(2) )
                    dir_command = dir_command + " " + str(2)
                if i < len(distance):
                    #dis_command.append( int(distance[i][0]) )
                    dir_command = dir_command + " " + str( int( distance[i][0] ) )
                else:
                    #dis_command.append( int(1) )
                    dir_command = dir_command + " " + str( 1 )

            print(dir_command)
            #print(dis_command)
            command =  dir_command
        else:
            print('无法执行的指令')
            command = '无法执行的指令'

        with open('command.txt','w') as f:
            f.write(command)


# def joystick_control(data)

# def button_control(data):

# def gravity_control(data):

# def gesture_control(data):

def Controller():
    
    mode,data = getcommand()
    if mode == 'NONE':
        #print("wait for command")
        time.sleep(0.2)
    else:
        if mode == 'SPEECH':
            speech_control(data)
        '''elif mode == 'BUTTON':
            button_control(data)
        elif mode == 'GRAVITY':
            gravity_control(data)
        elif mode == 'GESTURE':
            gesture_control(data)'''


if __name__ == '__main__':
    while(1):
        Controller()
        time.sleep(0.2)

        
