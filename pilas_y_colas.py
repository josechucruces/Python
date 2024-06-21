# Actuar como una pila, meter elementos y borrar el ultimo de la lista
print ("\n\nEjercicio de funcionamiento de pilas \n")


stack = []

#esto es hacer push ... meter elementos en la lista
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")

print (stack)

#esto es hacer pop, borrar elementos en la lista 

stack_item = stack[len(stack)-1]
del stack[len(stack)-1]

#esto es hacer pop de otra manera y hace lo mismo borrar el ultimo en la lista 
print(stack.pop())

print(stack)

print("")
print("")
      
#  Aeui hablamos de colas Queue

print ("Ejercicio de funcionamiento de colas \n")
stack = []

stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")

print (stack)

stack_item = stack[0]
del stack[0]
print (stack)

stack_item = (stack.pop(0))
print (stack)

