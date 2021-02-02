import numpy as np
import matplotlib.pyplot as plt
from math import pi
import scipy.fftpack
import pywt

#Done:Amplitude spectrum of Fast Fourier transform
#Approximation and detail coefficients for n-level Stationary Wavelet Transform

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



def add_nois_sinus(F, sin):
    nois = np.random.normal(0, 3, F)
    x, y = sin
    new_y = y + nois

    return new_y


def add_nois_rect(F, rect):
    nois = np.random.normal(0, 3, F)
    x, y = rect
    new_y = y + nois

    return new_y


nois_sin = np.array(add_nois_sinus(F, s))
nois_rect = np.array(add_nois_rect(F, r))


#print(scipy.fftpack.fft(r[1]))
arg_rect=np.abs(scipy.fftpack.fft(r[1]))
arg_sin=np.abs(scipy.fftpack.fft(s[1]))
#print(scipy.fftpack.fft(r[1]))
#print(arg_rect)

print(pywt.swt(s[1],'db6'))
print(pywt.swt(r[1],'db6'))
