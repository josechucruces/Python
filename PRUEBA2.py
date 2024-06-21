#lista random de elementos y el shuffle arrasa, machaca todas las variables que se llamen igual que fruta y hace un aleaotio ya machacando a tope

import random
frutas = ['peras', 'manzanas', 'plátanos', 'ciruelas']
frutas2 = frutas
frutas3 = frutas2
print (frutas3)
random.shuffle(frutas)
print (frutas)


var1 = "casa"
var2 = "casa"
print ("Es igual la variable1 que la dos ?")
if (var1 == var2):
    print ("Si")
else :
    print ("No son iguales")

for x in range (10, 56):
    if x % 2 == 0 and x != 16 and x % 3 != 0 :
        print(x)
    x += 1
