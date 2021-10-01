import os
def tablePrint(r,piece):
  os.system("cls" if os.name=="nt" else "clear")
  r2=[]
  for i in r:
    r2.append(piece[i])
  print(" ╔════╦════╦════╗\n ║₁ "+r2[0]+ " ║₂ "+r2[1]+ " ║₃ "+r2[2]+ " ║\n ╠════╬════╬════╣\n ║₄ "+r2[3]+ " ║₅ "+r2[4]+ " ║₆ "+r2[5]+ " ║\n ╠════╬════╬════╣\n ║₇ "+r2[6]+ " ║₈ "+r2[7]+ " ║₉ "+r2[8]+ " ║\n ╚════╩════╩════╝\n ") 
def rowsCalc(r, x_or_o):
  w=(x_or_o, x_or_o, x_or_o)
  if (r[0],r[1],r[2]) == w or (r[3],r[4],r[5]) == w or (r[6],r[7],r[8]) == w or (r[0],r[3],r[6]) == w or (r[1],r[4],r[7]) == w or (r[2],r[5],r[8]) == w or (r[0],r[4],r[8]) == w or (r[2],r[4],r[6]) == w:
    return False
  else:
    return True
def newPiece(coordinate,turn,r):
  r2=[]
  n=0
  for i in r:
    if n==coordinate:
      r2.append(turn)
    else:
      r2.append(i)
    n+=1
  return r2