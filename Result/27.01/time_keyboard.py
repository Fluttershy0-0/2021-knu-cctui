import time,keyboard
import csv,numpy,sys,os


def check(param):

    i = 0
    while i < len(param[0]):

        if param[0][i].isupper():
            if (param[0][i+1].islower() and param[0][i+1].upper()==param[0][i]) or param[0][i+1]=="shift":
                param[3][i+1] = round(param[2][i] + param[2][i + 1] + param[1][i + 1]+param[1][i],4)
                param[2][i+1] = round(param[2][i] + param[2][i + 1]+param[1][i+1],4)


                param[1][i] += round(param[1][i + 1],4)
                del param[1][i + 1]
                del param[2][i]
                del param[3][i]
                del param[0][i + 1]

        i += 1
    return (param)

def check_pas(password,param):
    p=param[0]
    s=""
    flag=True

    if len(password)!=(len(p)-1):
        flag=False
    else:
        for i in range(0,len(p)-1):
            s+=p[i]

            if s==password:
                flag=True
            else:
                flag=False
    return flag

def touch():
    a = keyboard.read_event()
    t_b=0
    t_e=0
    b=""
    time_p=[] # time of pressing the button
    time_b=[] # time between pressing the button
    time_n=[]
    t_old=[]
    password=[]
    n=0
    while a.name != "enter" and a.name != "esc":
        t_b = time.time()

        b = keyboard.read_event()
        t_e=time.time()
        password.append(b.name)
        time_p.append(round(t_e - t_b, 4))
        t_old.append(t_b)

        n=len(password)
        if len(password)>=2:
            time_b.append(round(t_old[n-1]-t_old[n-2]-time_p[n-2],4))
            time_n.append(round(t_old[n - 1] - t_old[n - 2],4))
        a = keyboard.read_event()
    else:
        t_b = time.time()
        b = keyboard.read_event()
        t_e = time.time()
        password.append(b.name)
        time_p.append(round(t_e - t_b, 4))
        t_old.append(t_b)
        n = len(t_old)
        if n >= 2:
            if len(t_old) >= 2:
                time_b.append(round(t_old[n - 1] - t_old[n - 2] - time_p[n - 2], 4))
                time_n.append(round(t_old[n - 1] - t_old[n - 2], 4))
        return (password,time_p,time_b,time_n)

def write_file(f,n_s,r,res):
    f.write("Anna-Maria"+","+n_s+","+r)
    n=len(res[2])
    m=len(res[1])
    for i in range(0,n):
        s=","+str(res[1][i])+","+str(res[2][i])+","+str(res[3][i])
        f.write(s)
    f.write(","+str(res[1][m-1]))
    f.write("\n")




col_name=["subject","sessionIndex",	"rep","H.period","DD.period.t","UD.period.t","H.t","DD.t.i","UD.t.i","H.i","DD.i.e","UD.i.e","H.e","DD.e.five","UD.e.five",
          "H.five","DD.five.Shift.r","UD.five.Shift.r",	"H.Shift.r","DD.Shift.r.o",	"UD.Shift.r.o",	"H.o","DD.o.a",	"UD.o.a","H.a","DD.a.n","UD.a.n","H.n","DD.n.l","UD.n.l","H.l",	"DD.l.Return",
          "UD.l.Return","H.Return"]
s=""
for i in range(0,len(col_name)-1):
    s+=col_name[i]+","
s+=col_name[len(col_name)-1]+"\n"


path=os.getcwd()

pas=".tie5Roanl"
print(pas+"\n")

f=open('Task2701_2.csv', 'w')
f.write(s)

res=[]


for i in range(0,15):
    a = touch()
    res = check(a)
    if check_pas(pas,res)==True:
        write_file(f,"2",str(i+1),res)