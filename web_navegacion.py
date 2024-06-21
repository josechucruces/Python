def web_navegation():
    stack = []
    
    while True:
        
        action = input("Añade una url o interactua con palabras atras/salir:")
        
        if action == "salir":
            print("Saliendo del navegador web. ")
            break
        elif action == "atras":
            if len(stack) >0 :
                stack.pop()
        else:
            stack.append(action)
        
        if len(stack) >0 :
            
            print(f"Has navegado a la web : {stack[len(stack) -1]}")
        else:
            print("Estas en la pagina de inicio")
        
web_navegation()
