import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import scipy

#f = int(input("Enter frequency(f є [1;20]): "))
f = 3
#a = int(input("Enter amplitude(a є [1;10]): "))
a = 7
#ph  = int(input("Enter initial phase(ph є [1;90]): "))
ph = 45

def sinusoid(f,a,phase):
    def yy (x):
        ans = a * np.sin(f * x + ph)
        return ans
    #fig, ax = plt.subplots()
    #ax.grid()
    x = np.linspace(-10, 10,1000)
    #plt.plot(x, yy(x))
    #plt.show()
    return x,yy(x)

def noiz_sinusoid():
    noiz = np.random.normal(0, 1, 1000)
    x,y = sinusoid(f,a,ph)
    y1 = y + noiz
    coef = pearsonr (y,y1)[0]
    plt.plot(x, y1)
    plt.show()
    print("coef = ",coef)
  
noiz_sinusoid()
x,y = sinusoid(f,a,ph)
print(scipy.fftpack.fft(y))