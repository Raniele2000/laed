#(3) O mais próximo da média
v=[5,3,1,10,2,13,9,12,4,7]
soma=0
for i in v:
  soma+=i
  media=soma/len(v)
  menor_dif = abs(v[0]- media)
for i in v:
  dif = abs(i-media)
  if dif < menor_dif:
     menor_dif = dif
     mais_proximo = i
print("media é igual ",media)
print("mais proximo é igual", mais_proximo)
