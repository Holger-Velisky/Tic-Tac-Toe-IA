import time
import random as q
def rC(r, u):
  w=(u, u, u)
  if (r[0],r[1],r[2]) == w or (r[3],r[4],r[5]) == w or (r[6],r[7],r[8]) == w or (r[0],r[3],r[6]) == w or (r[1],r[4],r[7]) == w or (r[2],r[5],r[8]) == w or (r[0],r[4],r[8]) == w or (r[2],r[4],r[6]) == w:
    return False
  else:
    return True
def nP(a,u,r):
  k=[]
  o=0
  for i in r:
    if o==a:
      k.append(u)
    else:
      k.append(i)
    o+=1
  return k
def oP(x):
  m=open("0.txt", "a")
  m.write(x+"\n")
  m.close()
def aV(r):
  c,l=0,[]
  for i in r:
    if i==0:
      l.append(c)
    c+=1
  return l
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
    n=aV(r)
    if len(n)<2:
      b=False
    a=n[q.randint(0,len(n)-1)]
    g+=str(a+1)
    r=nP(a,u,r)
    if not rC(r,u):
      t=u
      b=False
    elif u==1:
      u=2
    else:
      u=1
  oP(g+"-"+f[t])
  d-=1
j=time.clock_gettime(time.CLOCK_REALTIME)-h
print(j)