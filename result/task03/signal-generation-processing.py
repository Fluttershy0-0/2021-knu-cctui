from scipy import signal, stats
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
    plot.plot(t, signal, 'r')
    plot.show()

x, y = generate_sin()
plot_sin(x, y)

fourier1 = np.fft.fft(signal_sq)
phase1 = np.angle(fourier1)
fourier2 = np.fft.fft(y)
phase2 = np.angle(fourier2)

print(phase1,"\n", phase2)
noise = np.random.normal(0, 1, 100)
signal_sq_noisy = signal_sq + noise
signal_sin_noisy = y + noise
cor = stats.pearsonr(signal_sq_noisy, signal_sin_noisy)
print("C(signal1, signal2) = ", cor)
