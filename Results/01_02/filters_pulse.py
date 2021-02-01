import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

start = 0
duration = 1
amplitude = 2


def rect_wave(x):
    r = 0
    if x == (duration  + start):
         pass    
    elif x < start or x > duration + start:
         pass
    else:
         r = amplitude
    return r
    
x=np.arange(start - 1,duration + start + 1,0.1)
y=np.array([rect_wave(t) for t in x])
y1 = y + np.random.normal(0,0.8,np.size(x))
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x, y1)
plt.title('pulse')
y1=sig.medfilt(y1, kernel_size = 9)
y1=sig.savgol_filter(y1, window_length=5, polyorder=3,mode='mirror')
plt.subplot(2,1,2)
plt.plot(x,y1)
plt.title('after filters')
plt.show()


