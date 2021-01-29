from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import time
import csv


start_time = time.time()
repetition_number = 1
buffer = []
password = ['.', 't', 'i', 'e', '5', 'R', 'o', 'a', 'n', 'l']
row = []
f = open("keystroke_dynamics_session_data.csv", "a")
writer = csv.writer(f)

def equal_lists(l1, l2):
    global buffer, repetition_number
    if (len(l1) != len(l2)):
        print("Length mismatch: ", len(l1), "!=", len(l2))
        print("WRONG PASSWORD. TRY AGAIN")
        buffer.clear()
        return False
    for i in range(0, len(l2)):
        if KeyCode.from_char(l1[i]) != l2[i]:
            print("Symbols mismatch: ", KeyCode.from_char(l1[i]), "!=", l2[i])
            print("WRONG PASSWORD. TRY AGAIN")
            buffer.clear()
            return False
    print("PASSWORD OK. ATTEMPT #" + str(repetition_number) + " SUCCESSFUL")
    buffer.clear()
    return True

def write_row():
    global row
    writer.writerow(row)
    row = []

def on_release(key):
    global start_time, repetition_number, buffer, password, row
    on_release.release_time = round(time.time() - start_time, 3)
    start_time = time.time()
    print("\non hold time: ", on_release.release_time)
    row.append(str(key))
    row.append(str(on_release.release_time))
    if key != Key.shift and key != Key.enter:
        buffer.append(key)
    if key == Key.enter:
        if equal_lists(password, buffer) == True:
            row.append("SUCCESS")
            repetition_number += 1
            write_row()
        else:
            row.append("FAIL")
            write_row()

def on_press(key):
    global start_time, repetition_number
    on_press.idle_time = round(time.time() - start_time, 3)
    start_time = time.time()
    print("idle time: ", on_press.idle_time)
    if len(row) == 0:
        row.append(repetition_number)
    row.append(str(on_press.idle_time))
    if key == Key.esc:
        row.append("END")
        write_row()
        f.close()
        return False

print("ENTER to confirm, ESC to end session")
with keyboard.Listener(on_release=on_release, on_press=on_press) as listener:
    listener.join()
