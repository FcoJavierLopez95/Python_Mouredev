a=5
b=7

### Operadores aritméticos
my_sum = (a + b) # También para concatenar
my_resta = (a - b)
my_mult = (a * b)
my_exponente = (a ** b)
my_div = (a / b)
my_aprox_div = (a // b) # división con resultado cortado a numero entero
my_resto = (a % b)

print(my_sum)
print(my_resta)
print(my_mult)
print(my_exponente)
print(my_div)
print(my_aprox_div)
print(my_resto)


### Operadores de comparación ==> True o False
my_mayor = (a > b)
mayor_o_igual  = (a >= b)
my_menor  = (a > b)
menor_o_igual  = (a >= b)
my_igual = (a == 5) # OJO con un solo símbolo = estaríamos asignando valor no comparando
my_diferent = (a != b) #  "!" significa not, se puede usar en cualquier otro comparador ej !< no menos, !true no verdadero...

### Operadores lógicos ==> and &&, or || y not !, in, not in:
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))