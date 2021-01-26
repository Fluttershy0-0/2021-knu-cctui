import time,keyboard
import csv


def check(param):

    i = 0
    while i < len(param[0]):

        if param[0][i].isupper() == True:
            if i + 1 < len(param[0]):
                del param[0][i + 1]
                del param[1][i+1]
                del param[2][i]
                del param[3][i]


        i += 1
    return (param)


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

res=touch()
for i in range (0,len(res[0])):
    print(" ")
    print(res[0][i]+"-"+str(res[1][i]))
for i in range (2,4):
    print(" ")
    print(res[i])

res=check(res)
for i in range (0,len(res[0])):
    print(" ")
    print(res[0][i]+"-"+str(res[1][i]))
for i in range (2,4):
    print(" ")
    print(res[i])

#pas=res[0]
#time_pres=res[1]
#time_betw=res[2]
#time_betwn=res[3]

#col_name=["subject","sessionIndex",	"repH.period","DD.period.t","UD.period.t","H.t","DD.t.i","UD.t.i","H.i","DD.i.e","UD.i.e","H.e","DD.e.five","UD.e.five",
          #"H.five","DD.five.Shift.r","UD.five.Shift.r",	"H.Shift.r","DD.Shift.r.o",	"UD.Shift.r.o",	"H.o","DD.o.a",	"UD.o.a","H.a","DD.a.n","UD.a.n","H.n","DD.n.l","UD.n.l","H.l",	"DD.l.Return","UD.l.Return",
          #"H.Return"]



#s,f=check(["b","a","c","D"])
#print(s,f)
