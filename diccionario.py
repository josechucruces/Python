miDiccionario4={"nombre":"Jordan", "Equipo":"Bulls", "Anillos": {"Temporadas":[1991,1992,1993,1996]}}

print(miDiccionario4)
print(miDiccionario4.keys())
print(miDiccionario4.values())
print(miDiccionario4["nombre"])

#Hacer una copia del diccionario
miDiccionario3=miDiccionario4.copy()


# otro diccionario

lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario=dict(zip(lista_claves, lista_valores))
print (diccionario)
print (diccionario["nombre"])
if "nombre" in diccionario: 
    print ("True")
    
    

#metodo pop para eliminar un elemento del diccionario

miDiccionario4.pop("Equipo")
print(miDiccionario4)

print (miDiccionario3)


#diccionarios anidados  ojo a la coma detras del parentesis de cada bloque

myFamily = { 
    "child1" :
        { "name" : "Emily", "year" : "2004" },
    "child2" :
        { "name" : "Donald", "year" : "2006" },
    "child3" :
        {"name" : "Greg","year" : "2002"}
}
print (myFamily)



