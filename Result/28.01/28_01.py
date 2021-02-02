import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy import signal as sg
from scipy import stats as st
from scipy import fftpack
import random


def sin_wave():#function for sinusoidal wave generation
    A = random.randint(1,10) #Amplitude A є [1;10]
    f = random.randint(1,20) #frequency f є [1;20]
#further part will be calculation of initial phase
    fs = 100
    T = random.randint(1, 10) / 10
    Ts = T / fs
    i_f = int(T / Ts)
    t = np.linspace(0, T, i_f)
    signal = A * np.sin(2 * pi * t * f)
    return (t, signal)

x,y = sin_wave()
plt.plot(x, y)
plt.title('sinusoidal wave')
plt.show() #plotting sinusoidal wave


def rect_pulse():
    A = random.randint(1, 10)  # Amplitude A є [1;10]
    t = np.linspace(0, 1, num = 100) #generation of signals with fixed sample rate (num = 100)
    signal = sg.square(2 * pi * t *10)*A
    return (t, signal)

w,v = rect_pulse()
plt.plot(w,v)
plt.title('rectangular pulse')
plt.show() #plotting rectangular pulse

Amp_sp_S1 = np.fft.fft(y) # amplitude spectra for generated S1(t) signal
Amp_sp_S2 = np.fft.fft(v) # amplitude spectra for generated S2(t) signal
Phase_sp_S1 = np.angle(Amp_sp_S1) # Phase spectra for generated S1(t) signal
Phase_sp_S2 = np.angle(Amp_sp_S2) # Phase spectra for generated S2(t) signal

#adding to generated signals white Gaussian noise with random mean and variance
noise = np.random.normal(0, 1, 100)
sin_with_noise = y + noise
pulse_with_noise = v +noise

Pearson_corr_sin = st.pearsonr(y, sin_with_noise)
Pearson_corr_pulse = st.pearsonr(v, pulse_with_noise)
print(Pearson_corr_sin, "\n", Pearson_corr_pulse)

a =fftpack.fft(Pearson_corr_sin)
b =fftpack.fft(Pearson_corr_pulse)
print(a,"\n",b)

np.