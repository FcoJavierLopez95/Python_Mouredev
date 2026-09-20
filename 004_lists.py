### Listas

my_list = list()
my_other_list = []
print(my_list)
print(len(my_list))
print (type(my_list))

my_other_list= [20, 30, 14, 53, 42, 16, "Juan", "JuanValdes"]

print(my_other_list)
print(len(my_other_list))

print(type(my_list))
print(type(my_other_list))

## Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])    # Python permite numeros negativos para recorrer del ultimo al primero
print(my_other_list[-4])    
print(my_list.count(30))
# print(my_other_list[4]) IndexError desbordamiento
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Juan"))

## Concatenación
print(my_list + my_other_list)
#print(my_list - my_other_list)

## Creación, inserción, actualización y eliminación
my_other_list.append("JuanValdes")
print(my_other_list)

my_other_list.insert(1, "Rojo")         # Indicamos posición y inserta valor
print(my_other_list)

my_other_list[1] = "Azul"               # Indicamos posición y cambia el valor del elemento existente
print(my_other_list)

my_other_list.remove("Azul")            # Indicamos elemento a borrar
print(my_other_list)

print(my_other_list.pop())              # Indicamos posición y borra el elemento devolviendo el valor borrado

my_pop_element = my_other_list.pop(2)
print(my_pop_element)
print(my_other_list)

del my_other_list[2]
print(my_other_list)                     # Indicamos posición y borra el elemento sin devolver nada
# Operaciones con listas

my_new_list = my_other_list.copy()

my_other_list.clear()                   # Vacía la lista
print(my_new_list)

my_new_list.reverse()                   # invierte el orden de los elementos.
print(my_new_list)

