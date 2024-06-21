a , b = 2 , 4
if a > b :
     print (b)
elif a < b :
    print (a)
else :
    print ( ' a = b ')
    
  #Ejerecicio de una cadena revertirla y devolverla en orden alreves   
    
lista = input("Dame tres palabras separadas por espacios , porfa: ")
words = lista.split()
rev_sentence = ' y ' .join(reversed(words))
print (words[1])
words [2] = words [1]
print (words[2])
print(rev_sentence)
print(words)


tupla = (2, 3, 6, 8, 11)
#suma de una tupla
def suma_tupla(tupla):
    returm = sum(tupla)
resultado = sum(tupla)
print (resultado)




