import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

#start = float(input("Enter start time: "))
start = 0
#duration = float(input("Enter the duration: "))
duration = 0.5
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
    
    x=np.linspace(start - 3,duration + start + 3,10000)
    y=np.array([rect_wave(t) for t in x])
    #plt.ylim(-1,amplitude+3)
    #plt.plot(x,y)
    #plt.show()
    return x,y
def noiz_pulse():
    nois = np.random.normal(0, 1, 10000)
    x,y = pulse(start,duration,amplitude)
    y1 = y + nois
    coef = pearsonr(y,y1)[0]
    plt.plot(x, y1, "k")
    plt.show()
    print("coef = ",coef)
noiz_pulse()
x,y = pulse(start,duration,amplitude)
print(scipy.fftpack.fft(y))
