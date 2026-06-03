#.(4)ímpar ímpar
v=[9,2,7,7,2,2,1,7,7,9]
unico= 0
contador = 0
for numero in v:
  contador = 0
  for elemento in v:
    if numero == elemento:
       contador +=1
  if contador == 1:
       unico = numero
print("numero que aparece uma unica vez é",unico)