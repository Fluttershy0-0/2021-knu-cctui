import pythoncom
import pyWinhook
from collections import defaultdict
import numpy as np
import pandas as pd

c=1
pressed = defaultdict(int)
data=[]
datau = []
datab = []
datat = []

# def end():
#     global c, data,datau,datab,datat,fu,fb,ft,session
#     strd = np.array(sorted(data, key=lambda i:i[1]))
#     comp=np.array(['Oem_Period', 'T', 'I', 'E', '5', 'Lshift', 'R', 'O', 'A', 'N', 'L', 'Return'])
#     comp2=np.array(['Oem_Period', 'T', 'I', 'E', '5', 'Rshift', 'R', 'O', 'A', 'N', 'L', 'Return'])
#     if comp.shape == strd[:,0].shape:
#
#         if np.all(comp == strd[:,0]) or np.all(comp2 == strd[:,0]):
#             time = np.array(strd[:, 1:], dtype='int64')
#             if time[5,1] > time[6,0] and time[5,1] < time[7,0]:
#
#                 dur = time[:, 1] - time[:, 0]
#                 UD = time[:, 0][1:] - time[:, 1][:-1]
#                 '''
#                                 unigram
#                 '''
#                 datau.append([session,c])
#                 for i in range(UD.shape[0]):
#                     datau[c-1].append(dur[i])
#                     datau[c - 1].append(UD[i])
#                 datau[c-1].append(dur[-1])
#                 '''
#                                 bigram
#                 '''
#                 datab.append([session,c])
#                 bdur=dur[:-1] + dur[1:]
#                 bUD=UD[:-1]+UD[1:]
#                 for i in range(bUD.shape[0]):
#                     datab[c - 1].append(bdur[i])
#                     datab[c - 1].append(bUD[i])
#                 datab[c-1].append(bdur[-1])
#                 '''
#                                 trigram
#                 '''
#                 datat.append([session,c])
#                 tdur = dur[:-2] + dur[1:-1] + dur[2:]
#                 tUD = UD[:-2] + UD[1:-1] + UD[2:]
#                 for i in range(tUD.shape[0]):
#                     datat[c - 1].append(tdur[i])
#                     datat[c - 1].append(tUD[i])
#                 datat[c - 1].append(tdur[-1])
#                 c+=1
#                 if c>15:
#                     '''
#                                     unigram
#                     '''
#                     btns= np.array(['period', 't', 'i', 'e', 'five', 'Shift', 'r', 'o', 'a', 'n', 'l', 'Return'], dtype="object")
#                     clmns = ["sessionIndex","rep"]
#                     t= btns[:-1]+"."+btns[1:]
#                     for i in range((UD.shape[0])):
#                         clmns.append("H."+btns[i])
#                         clmns.append("UD." + t[i])
#                     clmns.append("H."+btns[-1])
#                     clmns = np.array(clmns)
#                     datau = np.array(datau)
#                     df = pd.DataFrame(datau,columns=clmns)
#                     df.to_csv(fu,header=session==1, line_terminator='\n',index=False)
#                     '''
#                                     bigram
#                     '''
#                     clmns = ["sessionIndex","rep"]
#                     t = btns[:-2] + "." + btns[1:-1] + "+" + btns[1:-1] + "." + btns[2:]
#                     for i in range((UD.shape[0])-1):
#                         clmns.append("H." + btns[i]+"+"+btns[i+1])
#                         clmns.append("UD." + t[i])
#                     clmns.append("H." + btns[-1])
#                     clmns = np.array(clmns)
#                     datab = np.array(datab)
#                     df = pd.DataFrame(datab, columns=clmns)
#                     df.to_csv(fb, header=session==1, line_terminator='\n',index=False)
#                     '''
#                                     trigram
#                     '''
#                     clmns = ["sessionIndex","rep"]
#                     t = btns[:-3] + "." + btns[1:-2] + "+" + btns[1:-2] + "." + btns[2:-1] + "+" + btns[2:-1] + "." + btns[3:]
#                     for i in range((UD.shape[0])-2):
#                         clmns.append("H." + btns[i]+"+"+btns[i+1]+"+"+btns[i+2])
#                         clmns.append("UD." + t[i])
#                     clmns.append("H." + btns[-1])
#                     clmns = np.array(clmns)
#                     datat = np.array(datat)
#                     df = pd.DataFrame(datat, columns=clmns)
#                     df.to_csv(ft, header=session==1, line_terminator='\n',index=False)
#                     fu.close()
#                     fb.close()
#                     ft.close()
#                     exit()
#             else:
#                 print("input isn't correct(Shift)")
#         else:
#             print("input isn't correct")
#     else:
#         print("input isn't correct")
#     print(c)
#     data=[]
'''
Because in the dataset that we rely on Shift+k counts as 1 action, 
I will have to artificially reduce the number of features in the dataset I build
'''
def end():
    global c, data, datau, datab, datat, fu, fb, ft, session
    strd = np.array(sorted(data, key=lambda i: i[1]))
    comp = np.array(['Oem_Period', 'T', 'I', 'E', '5', 'Lshift', 'R', 'O', 'A', 'N', 'L', 'Return'])
    comp2 = np.array(['Oem_Period', 'T', 'I', 'E', '5', 'Rshift', 'R', 'O', 'A', 'N', 'L', 'Return'])
    if comp.shape == strd[:, 0].shape:

        if np.all(comp == strd[:, 0]) or np.all(comp2 == strd[:, 0]):
            time = np.array(strd[:, 1:], dtype='int64')
            if time[5, 1] > time[6, 0] and time[5, 1] < time[7, 0]:
                time=np.concatenate((time[:6],time[7:]))
                dur = time[:, 1] - time[:, 0]
                UD = time[:, 0][1:] - time[:, 1][:-1]
                '''
                                unigram
                '''
                datau.append([session, c])
                for i in range(UD.shape[0]):
                    datau[c - 1].append(dur[i])
                    datau[c - 1].append(UD[i])
                datau[c - 1].append(dur[-1])
                '''
                                bigram
                '''
                datab.append([session, c])
                bdur = dur[:-1] + dur[1:]
                bUD = UD[:-1] + UD[1:]
                for i in range(bUD.shape[0]):
                    datab[c - 1].append(bdur[i])
                    datab[c - 1].append(bUD[i])
                datab[c - 1].append(bdur[-1])
                '''
                                trigram
                '''
                datat.append([session, c])
                tdur = dur[:-2] + dur[1:-1] + dur[2:]
                tUD = UD[:-2] + UD[1:-1] + UD[2:]
                for i in range(tUD.shape[0]):
                    datat[c - 1].append(tdur[i])
                    datat[c - 1].append(tUD[i])
                datat[c - 1].append(tdur[-1])
                c += 1
                if c > 15:
                    '''
                                    unigram
                    '''
                    btns = np.array(['period', 't', 'i', 'e', 'five', 'Shift.r', 'o', 'a', 'n', 'l', 'Return'],
                                    dtype="object")
                    clmns = ["sessionIndex", "rep"]
                    t = btns[:-1] + "." + btns[1:]
                    for i in range((UD.shape[0])):
                        clmns.append("H." + btns[i])
                        clmns.append("UD." + t[i])
                    clmns.append("H." + btns[-1])
                    clmns = np.array(clmns)
                    datau = np.array(datau)
                    df = pd.DataFrame(datau, columns=clmns)
                    df.to_csv(fu, header=session == 1, line_terminator='\n', index=False)
                    '''
                                    bigram
                    '''
                    clmns = ["sessionIndex", "rep"]
                    t = btns[:-2] + "." + btns[1:-1] + "+" + btns[1:-1] + "." + btns[2:]
                    for i in range((UD.shape[0]) - 1):
                        clmns.append("H." + btns[i] + "+" + btns[i + 1])
                        clmns.append("UD." + t[i])
                    clmns.append("H."+ btns[-2] + "+" + btns[-1])
                    clmns = np.array(clmns)
                    datab = np.array(datab)
                    df = pd.DataFrame(datab, columns=clmns)
                    df.to_csv(fb, header=session == 1, line_terminator='\n', index=False)
                    '''
                                    trigram
                    '''
                    clmns = ["sessionIndex", "rep"]
                    t = btns[:-3] + "." + btns[1:-2] + "+" + btns[1:-2] + "." + btns[2:-1] + "+" + btns[2:-1] + "." + btns[3:]
                    for i in range((UD.shape[0]) - 2):
                        clmns.append("H." + btns[i] + "+" + btns[i + 1] + "+" + btns[i + 2])
                        clmns.append("UD." + t[i])
                    clmns.append("H." + btns[-3] + "+" + btns[-2] + "+" + btns[-1])
                    clmns = np.array(clmns)
                    datat = np.array(datat)
                    df = pd.DataFrame(datat, columns=clmns)
                    df.to_csv(ft, header=session == 1, line_terminator='\n', index=False)
                    fu.close()
                    fb.close()
                    ft.close()
                    exit()
            else:
                print("input isn't correct(Shift)")
        else:
            print("input isn't correct")
    else:
        print("input isn't correct")
    print(c)
    data = []


def OnKeyboardEvent(event):
    if pressed[event.Key]:
        return True
    pressed[event.Key] = event.Time
    return True



def OffKeyboardEvent(event):
    if pressed[event.Key]:
        data.append([event.Key,pressed[event.Key],event.Time])
        pressed[event.Key]=0
        if event.Key == "Return":
            end()
    return True

session = int(input("session: "))
with open("maliuk_data_uf.csv", "a") as fu:
    with open("maliuk_data_bf.csv", "a") as fb:
        with open("maliuk_data_tf.csv", "a") as ft:
            hm = pyWinhook.HookManager()
            hm.KeyDown = OnKeyboardEvent
            hm.KeyUp = OffKeyboardEvent
            hm.HookKeyboard()
            pythoncom.PumpMessages()
# .tie5Roanl
