from scipy import signal
import matplotlib.pyplot as plot
import numpy as np
import random as random


a = random.randint(1, 10)
t = np.linspace(0, 1, 100, endpoint=False)
d = random.randint(0, 5) / 10
n = 100*d
signal_sq = a*signal.square(2 * np.pi * 10 * t)
plot.plot(t, signal_sq)
plot.ylim(-11, 11)
plot.show()


def generate_sin():
    f = random.randint(1, 20)
    T = random.randint(1, 10) / 10
    A = random.randint(1, 10)
    fs = 100
    Ts = T/fs
    N = int(T/Ts)
    t = np.linspace(0, T, N)
    signal = A * np.sin(2 * np.pi * f * t)
    return (t, signal)

def plot_sin(t, signal):
    plot.plot(t, signal, 'y')
    plot.show()

x, y = generate_sin()
plot_sin(x, y)

noise = np.random.normal(0, 1, 100)
signal_sq_noisy = signal_sq + noise
signal_sin_noisy = y + noise
signal_sq_median = signal.medfilt(signal_sq_noisy)
signal_sin_median = signal.medfilt(signal_sin_noisy)

signal_sq_savgol3 = signal.savgol_filter(signal_sq_median, 3, 2, mode='mirror')
signal_sin_savgol3 = signal.savgol_filter(signal_sin_median, 3, 2, mode='mirror')
signal_sq_savgol5 = signal.savgol_filter(signal_sq_median, 5, 2, mode='mirror')
signal_sin_savgol5 = signal.savgol_filter(signal_sin_median, 5, 2, mode='mirror')
signal_sq_savgol7 = signal.savgol_filter(signal_sq_median, 7, 2, mode='mirror' )
signal_sin_savgol7 = signal.savgol_filter(signal_sin_median, 7, 2, mode='mirror')
signal_sq_savgol9 = signal.savgol_filter(signal_sq_median, 9, 2, mode='mirror')
signal_sin_savgol9 = signal.savgol_filter(signal_sin_median, 9, 2, mode='mirror')

plot.plot(t, signal_sq_median, 'g')
plot.plot(t, signal_sq_noisy, 'r')
plot.plot(t, signal_sq_savgol3, 'k')
plot.plot(t, signal_sq_savgol5, 'y')
plot.plot(t, signal_sq_savgol7, 'c')
plot.plot(t, signal_sq_savgol9, 'm')
plot.ylim(-11, 11)
plot.show()
plot.plot(t, signal_sin_median, 'g')
plot.plot(t, signal_sin_noisy, 'r')
plot.plot(t, signal_sin_savgol3, 'k')
plot.plot(t, signal_sin_savgol5, 'y')
plot.plot(t, signal_sin_savgol7, 'c')
plot.plot(t, signal_sin_savgol9, 'm')
plot.show()
