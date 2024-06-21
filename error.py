#Esto es una manera de gestionar los errores que pueden hacer que salte
# todo por los aires y pare el programa, esto lo salta y sigue


try:
    
    print(10/1) #Esto prueba a dividir 10/1 , lo puse en 10/0 en la primera prueba para ver el error que saca, con 10/1 no sale error y pasa al siguiente
    print([1,2,3,4][4]) #Esto prueba imprimir el parametro 4 de la lista que no hay y salta el error, por que el 4 es el 5 y no existe, entonces va al except
    
except Exception as e:
    print(f"Se ha producido un error: {e}")
    
print("Hola que tal ?")




#Aqui vamos a hacer un control de exceptiones mas potente 


def process_params(parameters: list):
    
    if len(parameters) <3:
        raise IndexError()
    elif parameters[1] ==0 :
        raise ZeroDivisionError()
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    
try:
    process_params([1, 0, 3, 4])
except IndexError as e:
    print("El numero de elementos de la llista debe ser mayor de 2")
except ZeroDivisionError as e:
    print ("No puede haber un elemento en la lista que sea 0 ")
except Exception as e:
    print(f"Se ha producido un error: {e}")
    
print("El programa finaliza")
    