'''
a = -1
b = -4

def resultado(a, b):

    if a <= b: 
        return a 

    else :
        return b

print(resultado(a, b))

a = -1
b = -4
'''

textoa = 'geeks quiz practive code'
print (textoa)

def resultado_sentence(frase):
    words = frase.split(' ')
    
    resultado_frase_alreves = ' y '.join(reversed(words))
    return resultado_frase_alreves

if __name__ == "__main__":
    textoquepongo = 'perrito comer tenera coger'
    #print (texto)
    print (resultado_sentence(textoquepongo))
    
print ('\n')

test_tupla = (1 , 20, 33, 44, 50)

print('The original tupla is : ' + str (test_tupla))
 
resultado = sum(list(test_tupla))
print ('La suma de la tupla es :' + str (resultado))


frase_recibida= input ('Dame una cadena de texto: ')
lista_dividida = frase_recibida.split(' ')
lista_ordenada_alreves = ' y '.join(reversed(lista_dividida))

print ('La frase ordenadas sus palabras alreves son asi : ' + lista_ordenada_alreves)

def texto_alreves(frase_recibida):
    frase_recibida= input ('Dame una cadena de texto: ')
    lista_dividida = frase_recibida.split(' ')
    lista_ordenada_alreves = ' y '.join(reversed(lista_dividida))
    broma = ('Lo que me da la gana')
    return broma
    #return lista_ordenada_alreves

print ('La frase ordenadas sus palabras alreves son asi : ' + texto_alreves(frase_recibida))

