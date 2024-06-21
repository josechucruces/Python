#Recursividad ... es un funcion que esta dentro de una funcion que sea la misma,
# hay que tener cuidado que tienes que ponerle un sistema para que pare el bucle



def countdown (number):
    if number >= 0 :
        print (number)
        countdown (number -1)

number = 20
countdown(number)


# ejercicio del factorial de 5 por ejemplo 

def factorial (number):
    if number < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif number ==0:
        return 1
    else:
        return number * factorial(number -1)
    
n = 5
print(factorial(n))
