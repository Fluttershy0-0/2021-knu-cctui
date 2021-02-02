import matplotlib.pyplot as plot
import numpy as np
import random as random
import pywt as wavelet
from numpy.fft import fft, fftshift

def generate_sin():
    f = random.randint(1, 25)
    T = 100 # random.randint(1, 1000) / 10
    A = random.randint(1, 10)
    fs = 100
    Ts = T/fs
    N = int(T/Ts)
    t = np.linspace(0, T, N)
    signal = A * np.sin(2 * np.pi * f * t)
    return (t, signal)

sin = generate_sin()
x, y = sin
plot.plot(x, y, 'y', label="sin signal")

# noise = np.random.normal(0, 1, 100)
# noisy = y + noise
# plot.plot(noisy, label="noisy signal")

freq = np.fft.fft(y, norm="ortho")
window = np.hanning(100) * freq
plot.plot(window, label="Hann window")
plot.title("Hann window")
plot.ylabel("Amplitude")
plot.xlabel("Sample")
lf = abs(freq)
plot.plot(lf, label="Fourier transform")
plot.legend()

coefficients = wavelet.dwt(sin, 'db1')
print("Wavelet coefficients:", coefficients)

plot.show()