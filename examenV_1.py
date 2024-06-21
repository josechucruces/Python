
""" Programa en Python utilizando POO para el examen practico final

(Esto lo muestro para demostrar otro tipo de comentarios que se pueden utilizar) """

#Creo la lista principal en la que voy a incluir todas las tareas ordenadas para poder localizarlas siempre por su posicion

lista_tareas = []

#creo una clase con una expcepción personalizada que muestra un mensaje con el error cuando en el codigo llamemos a la clase
class MiExcepcionPersonalizada(Exception):
        def __str__(self):
            return "\n\n Error: La tarea no existe en la lista. \n"
        
#creo la clase GestorTareas         
class GestorTareas:
    def mostrar_tareas(self, lista_tareas):
        #Escribo un titulo de lo que voy a mostrar
        print("\nListado de todas las tareas :\n")
        #recorro toda la lista 
        for i in range(0, len(lista_tareas), 2):
            #guardo en una variable el valor que hay en cada hueco de la lista de dos en dos para mostrar la tarea y su estado
            tarea = lista_tareas[i]
            estado = lista_tareas[i + 1]
            #muestro los valores fila por fila de cada tarea
            print(f"\nTarea: {tarea} - Estado: {estado}\n")
            
#defino la clase MenuPrincipal          
class MenuPrincipal:
    def mostrar_menu(self, lista_tareas):
        #Mustro todas las opciones que tienen en el menu para escoger
        print ("\nBienvenidos a tu agenda de tareas\n")
        print ("\n1. Añadir una tarea a la agenda")
        print ("\n2. Ver el listado de todas las tareas")
        print ("\n3. Borrar un registro de la agenda")
        print ("\n4. Completar una tarea pendiente ")
        print ("\n5. Mostrar listado de tareas pendientes")
        print ("\n6. Salir de la agenda\n")

#definiento la clae BorrarTarea 
class BorrarTarea:
    def borrando_tareas(self, lista_tareas):
        #Pido el input para saber que tarea se quiere borrar
        tarea_para_borrar = input("\nNombre de la tarea que quieres borrar: ")
            #Busco la tares que se quiere borrar en la lista de tareas
        if tarea_para_borrar in lista_tareas:
                #localizo su posicion para poder borrar la tarea y tambien su estado gracias a su siguiente posicion en la lista
            index_tarea = lista_tareas.index(tarea_para_borrar)
            if index_tarea < len(lista_tareas) - 1:
                    
                del lista_tareas[index_tarea : index_tarea + 2]
            else:
                    
                del lista_tareas[index_tarea]
        else:
                #Aqui llamo a una clase que es una excepcion personalizada que indica que la tarea que queremos borrar no existe
            raise MiExcepcionPersonalizada(tarea_para_borrar)
        
class CompletarTarea():
    def completar_tareas(self, lista_tareas):
        #Pedimos que tarea queremos marcar como completada
        completar_tarea = input("Por favor, dame la tarea que quieres marcar como completada: ")
        # aqui comprobamos si la tarea que en la variable completar_tarea esta en la lista ...
        if completar_tarea in lista_tareas:
            #localizamos la posición y le añadimos el texto completada en la posición justo siguiente , machacando el valor que habia , que si era pendiente ahora sera completada
            index_tarea = lista_tareas.index(completar_tarea)
            lista_tareas[index_tarea + 1] = "completada"
            #Aqui indicamos que hemos modificado el estado de la tarea para que lo sepa
            print("Estado de la tarea actualizado correctamente.\n")
            gestor = GestorTareas()
            gestor.mostrar_tareas(lista_tareas)
        else:
            #Esta es otra manera de lanzar una excepcion personalizada por mi y que no para el programa de ejecutarse para demostrar que se de ambas maneras
            print("La tarea no existe en la lista.")
            
class NuevaTarea():
    def nueva_tarea(self, lista_tareas):
    #Pedimos que tarea quieren incluir en la lista y la guardamos en una variable
        registro_nuevo = input("\n¿Qué tarea nueva quieres incluir en la lista?\n")
        #Si esa tarea esta en la lista le decimos que ya esta en la lista y no se puede incluir dos veces
        if registro_nuevo in lista_tareas:
            
            print("Esa tarea ya está en la lista")
        #si no esta en la lista entonces arranca el else  
        elif registro_nuevo == "" or registro_nuevo == " ":
            #Si se escribe como tarea vacio o un espacio en blanco te lo aviso con un error personalizado pero que no para el programa
            print("Esa tarea es erronea has puesto un espacio o vacio")

        else:
            #Aqui el append añade a la lista lo que hay en la variable registro_nuevo
            lista_tareas.append(registro_nuevo)
            #Pedimos Que nos indique escribiendo pendiente o completada en que estado esta la tarea
            print("\nPor favor , escribe pendiente o completada para saber el estado de la tares:")
            print("\npendiente")
            print("\ncompletada\n")
            #Gauardamos el estado en la variable registro_tarea
            registro_tarea = input("Escribe pendiente o completada : \n\n")
            #si registro tara es igual a pendiente o completada que quiere decir que esta bien escrita como queremos la guardamos en la lista
            if registro_tarea == "pendiente" or registro_tarea == "completada" : 
                lista_tareas.append(registro_tarea)
            #Si no la han escrito bien lo que hacemos es escribir estado incierto para que quede regsitrada aunque no se sepa su estado, luego en otro menu pueden modificar el estado
            else:
                
                print("\nMe has dado un estatus erroneo, voy a marcarlo como erroneo, la proxima vez escribe pendiente o completada\n")
                lista_tareas.append("estado_erroneo")    

class ListarPendientes():
    def listar_pendientes (self, lista_tareas):
    #Si escogen 5 es para que el programa cree una lista de tareas pendientes y las muestre
        #creamos una lista vacia para rellenarla despues 
        lista_pendientes = []
        # recorremos la lista de principio a fin
        for i in range(1, len(lista_tareas)):
            #si la palabra pendiente aparace en la lista se recoge el punto donde esta y luego guardamos en una variable el texto que hay en la posción justo anterior en la lista
            if lista_tareas[i] == "pendiente":
                
                tarea_pendiente = lista_tareas[i - 1]
                lista_pendientes.append(tarea_pendiente)
        # imprimimos la lista de tareas pendientes guardadas pero la divido en lineas y numero cada una de ellas para mostrar la lista mas clara y mas visual
        for i in range(0, len(lista_pendientes), 1):
            tarea = lista_pendientes[i]
            print(f"\nTarea {i+1} : {tarea}\n")

#definimos la funcion tareas()
def tareas():
    
# Aqui mostramos un menu en el cual van a poder seleccionar la opcion que quieren hacer y que estara en bucle hasta que le digamos salir o salte una excepcion
    while True:
        # LLamamamos a la clase MenuPrincipal para mostrar el menu principal.
        menu = MenuPrincipal()
        menu.mostrar_menu(lista_tareas)
        
        #Guardamos en una variable la opcion que quieren 
        opcion = input("Escoge una opcion : ")
        
        # Si esccriben 1 al escoger las opciones llama a la clse NuevaTarea() para que haga todo lo que tiene que hacer para inscribir una tarea en la lista
        if opcion == "1":
            
            nuevo = NuevaTarea()
            nuevo.nueva_tarea(lista_tareas)
            
# Programa muestra todas tareas , mostrando si estan completadas o pendientes

        if opcion == "2":
            #si marcan la opcion 2 en el menu sigue con este menu que llama a la clase GestorTareas y utiliza mostrar_tareas para sacarme el listado de tareas 
            gestor = GestorTareas()
            gestor.mostrar_tareas(lista_tareas)
            
#Borrar una tarea en la lista 

        if opcion == "3":
            #Llamando a la clase BorrarTarea para borrar una de las tareas que nos indiquen .
            borrar = BorrarTarea()
            borrar.borrando_tareas(lista_tareas)
                
# Marcar una tarea como completada, dada su posicion en la lista , localizarla y cambiar su estado
        
        if opcion == "4":
            #Llamamos a la clase CompletarTarea()
            completar = CompletarTarea()
            completar.completar_tareas(lista_tareas)
            
        if opcion == "5":
            #llamamos a la clase ListarPendientes() 
            pendientes = ListarPendientes()
            pendientes.listar_pendientes(lista_tareas)
            
        # si presionan 6 sales de la agenda
        if opcion == "6":
            
            print("\nGracias por usar nuestra agenda de tareas ...")
            print("\nVuelve pronto !!!\n")
            #para de ejecutarse el programa
            break

if __name__ == "__main__":
    # LLamamos a la funcion tareas que esta definida arriba y se pone a hacer todo
    tareas()
