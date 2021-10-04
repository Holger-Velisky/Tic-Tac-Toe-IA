import time
import secondary as m
import random as q
d=int(input("Enter number of games desired:\t"))
h=time.clock_gettime(time.CLOCK_REALTIME) 
f="dXO"
while not d==0:
  g=""
  b=True
  u=1
  t=0
  r=[0,0,0,0,0,0,0,0,0]
  while b:
    n=m.aV(r)
    if len(n)<2:
      b=False
    a=n[q.randint(0,len(n)-1)]
    g+=str(a+1)
    r=m.nP(a,u,r)
    if not m.rC(r,u):
      t=u
      b=False
    elif u==1:
      u=2
    else:
      u=1
  m.oP(g+"-"+f[t])
  d-=1
j=time.clock_gettime(time.CLOCK_REALTIME)-h
print(j)