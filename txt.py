import os

file_name = "/Users/josechuair/Desktop/DAM/Curso de Pyhton Dalto/I B M/EJERCICIO TXT/mouredev.txt"

#with open(file_name, "w") as file:
#    file.write("\n")
#    file.write("Brais Moure\n")
#    file.write("36\n")
#    file.write("Programador\n")
#    file.write("\n")

    
#with open(file_name, "r") as file:
#    print(file.read())


while True:
    print ("1 - Añadir producto")
    print ("2 - Consultar producto")
    print ("3 - Actualizar producto")
    print ("4 - Borrar producot")
    print ("5 - Mostrar productos")
    print ("6 - Calcular ventas total")
    print ("8 - Salir")
    
    option = input ("\n\n Selecciona una de las opciones: ")
    
    if option == "1":
        name = input ("Nombre del producto: ")
        quantity = input ("Cantidad del producto: ")
        prize = input ("Precio del producto: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {prize}\n")
            
    elif option == "2":
        name = input ("Dame un nombre y lo busco: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print (line)
                    break
                
    elif option == "3":
        name = input ("Nombre del producto: ")
        quantity = input ("Cantidad del producto: ")
        prize = input ("Precio del producto: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {prize}\n")
                else:
                    file.write(line)
                    
    elif option == "4":
        name = input ("Nombre del producto: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    
    elif option == "5":
        try:
            with open(file_name, "r") as file:
                print(file.read())
        except:
            print("\n Todavia no hay nada en la lista, añade algun producto. \n")
    
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                prize = float(components[2])
                total += quantity * prize
        print(f"\nEste es el total que nos has pedido: {total}n")
        
    elif option == "8":
        try:
            os.remove(file_name)
            break
        except:
            break
    


