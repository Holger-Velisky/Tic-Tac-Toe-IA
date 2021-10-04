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