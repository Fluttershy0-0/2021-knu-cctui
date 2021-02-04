import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgn
from random import randrange, randint

#sinus wave case

def sin_create(f, f1, t_start, t_finish, A, F):
    x = np.linspace(t_start, t_finish, F)
    y = A * np.sin(2 * np.pi * x * f + f1)
    return x, y


f, f1, t_start, t_finish, A, F = randint(2, 5), np.pi/5, 0, 1, randint(2, 4), 1500
sin = sin_create(f, f1, t_start, t_finish, A, F)

def noise_sin_data(F, sinus):
    noise = np.random.normal(0, randint(3,5), F)
    x, y = sinus
    noised_y = y + noise
    return noised_y

noised_sin = np.array(noise_sin_data(F, sin))
new_sin = sgn.medfilt(noised_sin, 151)
sin_filtered = sgn.savgol_filter(new_sin,  window_length=5, polyorder=3, mode='mirror')

fig = plt.figure()
fig.add_subplot()
plt.plot(sin[0], sin_filtered, 'm')
plt.plot(sin[0], sin[1], 'g')
plt.show()

# rectaingle wave case

def rect_create(t_start, t_finish, F):
    amplitude = 3
    pulse_start = int(F * t_start)
    pulse_duration = int(F * amplitude)
    pulse_finish = pulse_start + pulse_duration
    if pulse_finish > F:
        pulse_finish = F
    x = np.linspace(t_start, t_finish, F)
    y = np.zeros_like(x)
    y[pulse_start:pulse_finish] = A
    return x, y

rect = rect_create(t_start, t_finish, F)

def noise_rect_data(rect, F):
    noise = np.random.normal(0, randint(3,5), F)
    x, y = rect
    noised_rect = y + noise
    return noised_rect

noised_rect = np.array(noise_rect_data(rect, F))
new_rect = sgn.medfilt(noised_rect, 111)
rect_filtered = sgn.savgol_filter(new_rect, window_length = 1001, polyorder = 1, mode = 'mirror')

fig = plt.figure()
fig.add_subplot()
plt.plot(rect[0], rect_filtered, 'm')
plt.plot(rect[0], rect[1], 'g')
plt.show()