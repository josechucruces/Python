#creando una funcion para saber si un numero es primo


def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

#   Este seria para obtener el resultado de esa funcion,
#   llamamos a la funcion con un valor a ver que pasa y que nos devulve, con el 5 por ejemplo:       
#   resultado = es_primo(5)


#creando funcion que retorne una lista con todos los primos

def funcion_cuales_son_primos_hasta(num):
    #creamos una lista
    lista_de_los_que_son_primos = []
    for i in range(2,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que el valor sea primo, lo agregamos a la lista
        if resultado == True: lista_de_los_que_son_primos.append(i)
    return lista_de_los_que_son_primos


resultado = funcion_cuales_son_primos_hasta(100)

print(resultado)

