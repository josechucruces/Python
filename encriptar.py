def obtener_pass_cifrado():
    pass_sin_encriptar = input ("\nDame una contraseña de 6 caracteres:\n")
    if len(pass_sin_encriptar) > 5 and len(pass_sin_encriptar) < 7 :
        zone_pass1 = pass_sin_encriptar[1:3]
        zone_pass2 = pass_sin_encriptar[3:5]
        zone_pass3 = pass_sin_encriptar[3:6]
        contraseña_encriptada = zone_pass3 + zone_pass1 + zone_pass2 + zone_pass1 + zone_pass2 + zone_pass3
        return (contraseña_encriptada)
    else:
        print ("Dame una contraseña de 6 caracteres porfa")

pass_nuevo = obtener_pass_cifrado()
print (pass_nuevo)

#imaginate que quiero cambiar un caracter que aparezca por otro ... se hace asi :
nuevo_pass5 = pass_nuevo.replace("o", "e")

# O divir un str texto en partes en una lista ... 
x = "Pedro Juan Tamara"
nuevo_valor = x.split(" ")
print (nuevo_valor)
print (nuevo_valor[1])

# conversion a mayuscular upper y a minusculas lower
x = "Pedro Juan Tamara"
nuevo_valor = x.lower()
print (nuevo_valor)





