# (3) busca aproximada
v=[9,42,21,14,25,3,19,33,45,6]
k = 31
mais_proximo=v[0]
encontrou = False
for numero in v:
  if numero == k:
    encontrou = True
    mais_proximo = numero
  elif abs(numero-k) < abs(mais_proximo - k):
    mais_proximo = numero
if encontrou:
  print("o numero k está na lista")
else:
  print("não está lá  mais en contrei o mais proximo" ,mais_proximo)

