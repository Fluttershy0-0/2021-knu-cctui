import keyboard
from pynput.keyboard import Key, Listener
import time

p = ".tie5Roanl"
clockArr = []
q = 0


def on_press(key):
    clockArr.append(time.time())
    # print('{0} pressed'.format(
    # key))


def on_release(key):
    clockArr.append(time.time())
    # print('{0} unpressed'.format(
    # key))
    if key == Key.enter:
        print("Stop")
        return False


# A = [0.1491,0.3979,0.2488,0.1069,0.1674,0.0605,0.1169,0.2212,0.1043,0.1417,1.1885,1.0468,0.1146,1.6055,1.4909,0.1067,0.7590,0.6523,0.1016,0.2136,0.1120,0.1349,0.1484,0.0135,0.0932,0.3515,0.2583,0.1338,0.3509,0.2171,0.0742]
# print(len(A))
# print(keyboard.read_key())
# A.append(input("Please input username"))
# A.append(input("Please input number of session"))
# for i in range(int(input("Please input number of session"))):
#    print("plaese input ", p, "  session", i)
#    A.append(i)
A = []

A.append(1)
A.append(1)
A.append(1)
for i in range(int(A[2])):
    print("please input ", p, "  session", A[1], "try", i)
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
for i in range(1, 10, 2):
    A.append(clockArr[i] - clockArr[i - 1])
    A.append(clockArr[i + 1] - clockArr[i - 1])
    A.append(clockArr[i + 1] - clockArr[i])

A.append(clockArr[13] - clockArr[10])
A.append(clockArr[14] - clockArr[10])
A.append(clockArr[14] - clockArr[13])

for i in range(15, 22, 2):
    A.append(clockArr[i] - clockArr[i - 1])
    A.append(clockArr[i + 1] - clockArr[i - 1])
    A.append(clockArr[i + 1] - clockArr[i])

A.append(clockArr[23] - clockArr[22])

print(A)
print(len(A))
f = open("data.csv", 'a')
for i in A:
    f.write(str(i))
    f.write(",")
f.write('\n')