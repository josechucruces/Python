# Aqui veremos que en cuato moficiamos una lista los valores automaticamente
# a todas las listas que esten igualadas se le copian,
# es valor por referencia, no son independientes
# Hay una manera de coppiar las listas y que sean independientes, copy es una manera ,
# y es bueno buscar por internet maneras de hacerlo 


def my_list_func(my_list:list):
    my_list_e = my_list
    my_list.append(30)
    
    my_list_d = my_list
    my_list_d.append(40)
    

    print (my_list)
    print (my_list_d)
    
my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)