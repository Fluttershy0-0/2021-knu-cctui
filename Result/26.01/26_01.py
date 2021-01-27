from pynput import keyboard
import time

but_press =[]
dur_press = []
interval = []
press_f = 0
press_s = 0

def on_press(key):
    try:
        but_press.append(key)
        press_s = time.time()

        if press_f == 0:
            pass
        else:
            interval.append(press_s-press_f)

    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    global press_f
    press_f = time.time()
    dur_press.append(press_f-press_s)
    print(dur_press)
    print(interval)
    if key == keyboard.Key.esc and key == keyboard.Key.enter:
        # Stop listener
        return False


with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()