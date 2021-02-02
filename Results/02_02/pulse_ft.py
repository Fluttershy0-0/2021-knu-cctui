  
import numpy as np
import scipy.fft as fft
import pywt
import matplotlib.pyplot as plt


#start = float(input("Enter start time: "))
start = 0
#duration = float(input("Enter the duration: "))
duration = 1
#amplitude = float(input("Enter the amplitude: "))
amplitude = 7

def pulse(start,duration,amplitude):
    def rect_wave(x):
        r = 0
        if x == (duration  + start): 
              pass    
        elif x < start or x > duration + start:
              pass
        else:
              r = amplitude
        return r
    
    x=np.linspace(start - 3,duration + start + 3,100)
    y=np.array([rect_wave(t) for t in x])
    return x,y
def noiz_pulse():
    nois = np.random.normal(0, 1, 100)
    x,y = pulse(start,duration,amplitude)
    y1 = y + nois
    return x,y1

x,y = pulse(start,duration,amplitude)
#x,y = noiz_pulse()
plt.plot(x, y, 'r', label = "pulse")
freq = fft.fft(y, norm = "ortho")
w = np.hanning(100) * freq
plt.plot(w, 'b', label = "hann window")
plt.ylabel("Amplitude")
plt.xlabel("Time")
lf = abs(freq)
plt.plot(lf, 'g', label = "fourier")
plt.legend()
c = x,y
coef = pywt.dwt(c, 'db1')
print(coef)

plt.show()