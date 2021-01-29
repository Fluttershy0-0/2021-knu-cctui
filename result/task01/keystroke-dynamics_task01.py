from pynput import keyboard
from pynput.keyboard import Key
import time

start_time = time.time()

def on_release(key):
    global start_time
    on_release.release_time = round(time.time() - start_time, 3)
    start_time = time.time()
    f = open("keystroke_dynamics.txt", "a")
    print("\non hold time: ", on_release.release_time)
    f.write("pressed " + str(key) + ": " + str(on_release.release_time) + "\n")
    if key == Key.enter:
        f.close()
        return False

def on_press(key):
    global start_time
    on_press.idle_time = round(time.time() - start_time, 3)
    start_time = time.time()
    print("idle time: ", on_press.idle_time)
    f = open("keystroke_dynamics.txt", "a")
    f.write("idle time: " + str(on_press.idle_time) + "\n")
    if key == Key.enter:
        f.close()
        return False

print("to stop the input please press ENTER")
with keyboard.Listener(on_release=on_release, on_press=on_press) as listener:
    listener.join()
