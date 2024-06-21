numero_nuevo= input('Dame un numero : ')
numero_dado= int (numero_nuevo)

def fibonaccimia(numero_dado):
    a , b = 0 , 1
    fibonaccimia_lista = [0]
    for i in range(numero_dado):
        if b > numero_dado : return fibonaccimia_lista
        else:
            fibonaccimia_lista.append(b)    
            a , b = b , a+b
            
print (fibonaccimia(numero_dado))