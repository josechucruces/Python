
            
def myagenda():
    agenda = {}
        
    while True: 
        print ("\n")
        print (" BIENVENIDO A TU AGENDA ")
        print ("\n Elige un aopcion :\n")
        print (" 1 - Buscar cliente \n ")
        print (" 2 - Nuevo cliente \n ")
        print (" 3 - Modificar datos de cliente \n ")
        print (" 4 - Borrar cliente \n ")
        print (" 5 - Imprimir toda la agenda :")
        print (" 6 - Salir de Agenda ")
        
        option = input("\n Escoge tu opcion : ")
        
        def insertar_numero():
            phone = input("Dame el nuevo numero de telfono: ")
            if phone.isdigit() and len(phone) > 0 and len(phone) < 10:
                agenda[name] = phone
            else:
                print("Introduce un numero con menos de 10 digitos")
    
        match option:
            case "1":
                name = input("¿Que nombre quieres buscar ? ")
                if name in agenda:
                    print("")
                    print(f"\n El numero de telefono de {name} es {agenda[name]}" )
                    print("")
                else:
                    print("El nombre no existe en la agenda")
            case "2":
                name = input("Dame un nombre: ")
                insertar_numero()
            case "3":
                name = input("¿Que nombre quieres modificar ? ")
                if name in agenda:
                    insertar_numero()
                else: 
                    print("El nombre no existe en la agenda")
            case "4":
                name = input("¿Que nombre quieres eliminar ? ")
                if name in agenda:
                    del agenda[name]
                else:
                    print("El nombre no existe en la agenda")
            case "5":
                print (agenda)
            case "6":
                print (" \n Gracias por haber usado la agenda. \n ")
                break
            case _:
                print("Por favor escoge una opcion valida del 1 al 6")

myagenda() 


