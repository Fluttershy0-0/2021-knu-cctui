  
import numpy as np
import scipy.fft as fft
import pywt
import matplotlib.pyplot as plt


#f = int(input("Enter frequency(f є [1;20]): "))
f = 3
#a = int(input("Enter amplitude(a є [1;10]): "))
a = 7
#ph  = int(input("Enter initial phase(ph є [1;90]): "))
ph = 45
d = 100
start = 0
finish = 100
def sinusoid(f,a,phase):
    def yy (x):
        ans = a * np.sin(2 * np.pi * f * x + ph)
        return ans
    #fig, ax = plt.subplots()
    #ax.grid()
    x = np.linspace(start,finish,d)
    #plt.plot(x, yy(x))
    #plt.show()
    return x,yy(x)

def noiz_sinusoid():
    noiz = np.random.normal(0, 1, d)
    x,y = sinusoid(f,a,ph)
    y1 = y + noiz
    return x,y1

x,y = sinusoid(f, a, ph)
#x,y = noiz_sinusoid()
plt.plot(x, y, 'r', label = "sinusoid")
freq = fft.fft(y, norm = "ortho")
w = np.hanning(100) * freq
plt.plot(w, 'b', label = "hann window")
plt.ylabel("Amplitude")
plt.xlabel("Time")
l = abs(freq)
plt.plot(l, 'g', label = "fourier")
plt.legend()
c = x,y
coef = pywt.dwt(c, 'db1')
print(coef)

plt.show()