#(5)Alguem e o dobro,a)lista não ordenada
v=[9,42,21,14,25,3,19,33,45,6]
encontrou=False
for i in range(len(v)):
  for j in range(len(v)):
    if i != j:
      if v[i] == 2* v[j]:
        print("encontrados",v[j], "e",v[i])
        encontrou=True
        break

  if encontrou:
    break
if not encontrou:
  print("não existem elementos ")

