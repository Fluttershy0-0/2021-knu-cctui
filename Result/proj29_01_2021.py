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
X_f=abs(sf.fft(x))
s=np.size(x)
fr=(Fs/2)*np.linspace(0,1,s)
xr_m=(2/s)*abs(X_f[0:np.size(fr)])
plt.subplot(2,1,2)
plt.plot(fr,xr_m)
plt.title('spectrum of noisy signal')
plt.tight_layout()
o=5
fc=np.array([8,12])
wc=2*fc/Fs
[b,a]=sig.butter(o,wc, btype='bandpass')
[W,h]=sig.freqz(b,a,worN=1024)
W=Fs*W/(2*pi)
plt.figure(2)
plt.subplot(2,1,2)
plt.plot(W, 20*np.log10(h))
plt.title('filter')
x_filt=sig.lfilter(b,a,x)
plt.subplot(3,1,1)
plt.plot(n,x_filt)
plt.title('Filtered signal')
plt.tight_layout()

#t =np.linspace(0, 1, 100, endpoint=False)
#noise = np.random.normal(0, 1, 100)
#s=signal.square(2 * np.pi * 5 *t)+noise
#plt.plot(t, s)
#plt.ylim(-3, 3)

plt.show()
