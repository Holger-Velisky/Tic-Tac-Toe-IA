import secondary as m
piece,turn,r=[" ","X","O"],1,[0,0,0,0,0,0,0,0,0]
m.tablePrint(r,piece)
b=m.rowsCalc(r,turn)
while b:
  a=int(input("Enter objective square:\n"))-1
  while not r[a]==0:
    a=int(input("The square you have selected is already occupied, please enter a valid objective coordinate:\n"))-1
  r=m.newPiece(a,turn,r)
  m.tablePrint(r,piece)
  if not m.rowsCalc(r,turn):
    print("Player "+str(turn)+" (using "+str(piece[turn])+" pieces) won!")
  b=m.rowsCalc(r,turn)
  turn=2 if turn==1 else 1

  