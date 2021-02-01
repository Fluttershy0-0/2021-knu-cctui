import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.signal import medfilt,savgol_filter


#Done: noise suppression with median and Savitzky-Golay filters for sin and puls signals.
F=1000
f=3
A=2
fi=pi/5
t1=0
t2=1
t_start=0.4
delta=0.5

def sinus(F,A,f,fi,t1,t2):
    x1 = np.linspace(t1,t2,F)
    y1 = A * np.sin(2 * pi * x1 * f + fi)
    #plt.plot(x1, y1)
    #plt.show()
    return x1,y1


idx_pulse_start = int(F * t_start)
pulse_duration_samples = int (F * delta)
idx_pulse_finish = idx_pulse_start + pulse_duration_samples
if idx_pulse_finish > F:
    idx_pulse_finish = F  # prevent taking sample out of interval





def rect(t_start,t_finish):
    time = np.linspace(t_start, t_finish, F)
    signal = np.zeros_like(time)
    signal[idx_pulse_start:idx_pulse_finish] = A
    #plt.plot(time, signal)
    #plt.show()
    return time,signal



s=sinus(F,A,f,fi,t1,t2)
r=rect(idx_pulse_start,idx_pulse_finish)


def add_nois_sinus(F,sin):
    nois = np.random.normal(0, 3, F)
    x,y=sin
    new_y=y+nois

    return new_y

def add_nois_rect(F,rect):
    nois = np.random.normal(0, 3, F)
    x,y=rect
    new_y=y+nois
    
    return new_y

nois_sin=np.array(add_nois_sinus(F,s))
nois_rect=np.array(add_nois_rect(F,r))

new_sin1=medfilt(nois_sin,101)
res_sin1=savgol_filter(new_sin1,9,1)

new_rec1=medfilt(nois_rect,71)
res_rec1=savgol_filter(new_rec1,53,1)



fig = plt.figure()
fig.add_subplot()
plt.plot(s[0], res_sin1,'m')
plt.plot(s[0],s[1],'g')

#plt.plot(r[0], res_rec1,'m')
#plt.plot(r[0],r[1],'g')
plt.show()
