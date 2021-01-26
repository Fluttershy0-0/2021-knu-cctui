from pynput.keyboard import Key, Listener
import time as t
import csv


times = []
#rep = int(input('Enter amount of rep you watn to do: '))
rep = 1

def on_press(k):
    times.append(t.time())
    
def on_release(k):
    times.append(t.time())
    if k == Key.enter:
        return False
    
ans = []
ans.append(1)
ans.append(1)   
for i in range(rep):
    ans.append(rep)
    print("Enter .tie5Roanl   ")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
#print(times)
#print(len(times))   

for i in range(1,10,2):
    ans.append(times[i] - times[i - 1])
    ans.append(times[i + 1] - times[i - 1])
    ans.append(times[i + 1] - times[i])
ans.append(times[13] - times[10])
ans.append(times[14] - times[10])
ans.append(times[14] - times[13])

for i in range(15, 22, 2):
    ans.append(times[i] - times[i - 1])
    ans.append(times[i + 1] - times[i - 1])
    ans.append(times[i + 1] - times[i])

ans.append(times[23] - times[22])


#print(ans)    

first_column = "subject, sessionIndex, rep, H.period, DD.period.t, UD.period.t, H.t, DD.t.i, UD.t.i, H.i, DD.i.e, UD.i.e, H.e, DD.e.five, UD.e.five,  H.five, DD.five.Shift.r, UD.five.Shift.r,	 H.Shift.r, DD.Shift.r.o, UD.Shift.r.o,	H.o, DD.o.a, UD.o.a, H.a, DD.a.n, UD.a.n, H.n, DD.n.l, UD.n.l, H.l,	DD.l.Return, UD.l.Return, H.Return"


with open('my_data.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(first_column.split())
    wr.writerow(ans)
print(len(ans))
