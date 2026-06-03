# (5) repetições
v=[7,1,9,1,7,3,9,2,1,6,8,3]
k=3
for i in v:
   cont = 0
   for j in v:
       if i==j:
          cont+=1
       if cont >=k:
        print("elemento",i)
        break
