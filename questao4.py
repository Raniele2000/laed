# (4)Elemento isolado
v=[17,2,8,1,7,13,9,12,4,16]
achou = False
for i in v:
    if(i-1 not in v) and (i+1 not in v):
       print("elemento isolado é  o ",i)
       achou = True
if achou == False:
  print("não existe")
