#(7)Repetidos próximos
v=[2,1,9,7,6,3,9,4,2,6,1,3]
k=4
for i in range(len(v)):
  for j in range(i+1,len(v)):
    if v[i]==v[j]:
      distancia=i-1
      if distancia==k:
        print("elemento:",v[i])
        achou=True
        break
if achou==False:
  print("não existe")