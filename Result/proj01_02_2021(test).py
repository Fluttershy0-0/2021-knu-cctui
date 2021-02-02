import matplotlib.pyplot as plt
import numpy as np
from math import pi
import scipy.fftpack as sf
import scipy.signal as sig
plt.close('all')
t=np.linspace(0,1,100)
Fs=100
t=1
n=np.arange(0,t,1/Fs)
f=10
x=np.sin(2*pi*f*n)
y=np.random.normal(0,0.8,np.size(x))
x=x+y
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(n,x)
plt.title('sin wave')
plt.xlabel('Time(s)')
plt.ylabel('amplitude')
x=sig.medfilt(x, kernel_size=3)
x=sig.savgol_filter(x, window_length=3, polyorder=2,mode='mirror')
plt.subplot(2,1,2)
plt.plot(n,x)
plt.tight_layout()
plt.title('filt')
plt.show()
