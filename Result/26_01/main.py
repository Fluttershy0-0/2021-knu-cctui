import pythoncom
import pyWinhook
from collections import defaultdict
import numpy as np

isShiftPressed = False
pressed = defaultdict(int)
data=[]

def end():
    srtd = np.array(sorted(data, key=lambda i:i[1]))
    time=np.array(srtd[:,1:],dtype='int64')
    dur=time[:,1]-time[:,0]
    interval = np.concatenate((np.zeros(1),time[:,0][1:]-time[:,0][:-1]))
    for i in range(len(data)):
        print("Key: {},\t duration: {},\t time interval from prev: {}".format(srtd[i][0],dur[i],interval[i]))
    exit(0)

def OnKeyboardEvent(event):
    if pressed[event.Key]:
        return True

    # print("pressed")
    # print('Key:',event.Key)
    # print('Time:',event.Time)
    if event.Key == "Escape":
        end()
        return False
    pressed[event.Key] = event.Time
    return True


def OffKeyboardEvent(event):
    # print("unpressed")
    # print('Key:', event.Key)
    # print('Time:',event.Time)
    if pressed[event.Key]:
        data.append([event.Key,pressed[event.Key],event.Time])
        pressed[event.Key]=0

    return True
print("enter escape to stop")
hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OffKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()