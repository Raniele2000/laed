# (2) O segundo maior ímpar
v=[9,42,21,14,28,3,19,32,46,6]
maior_impar = -1
segundoMaior = -1
for numero in v:
  if numero%2!=0:
    if numero >maior_impar:
      segundoMaior = maior_impar
      maior_impar = numero
    elif numero > segundoMaior and numero != maior_impar:
      segundoMaior = numero
if segundoMaior != -1:
  print("segundo maior é ",segundoMaior)
else:
  print("não existe numero")