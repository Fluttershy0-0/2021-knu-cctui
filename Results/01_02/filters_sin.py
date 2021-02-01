import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

f = 3
a = 6

x = np.arange(0,1,0.001)
b = a * np.sin(2*np.pi*f*x)
y = b + np.random.normal(0,0.8,np.size(b)) 
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x, y)
plt.title('sinusoid')

y=sig.medfilt(y, kernel_size=9)
y=sig.savgol_filter(y, window_length=5, polyorder=3,mode='mirror')
plt.subplot(2,1,2)
plt.plot(x,y)
plt.tight_layout()
plt.title('after filters')
plt.show()




