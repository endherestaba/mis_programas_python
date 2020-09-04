# def multiplicar_por_dos(n):
#     return n * 2


# def sumar_dos(n):
#     return n + 2


# def aplicar_operacion(f, numeros): # f guarda el nombre de la funcion "multiplicar_por_dos" ó "sumar_dos"
#     resultados = []
#     for numero in numeros:     # recorre a la cadena "numeros" (que es igual a "nums") desde la posicion 1 hasta el final (3)
#         resultado = f(numero) # aqui llamo a la funcion "multiplicar_por_dos" ó "sumar_dos" con el parametro "numero"
#         resultados.append(resultado)
#     print(resultados)


# def main():
#     nums = [10, 20, 30]
#     aplicar_operacion(multiplicar_por_dos, nums)
#     aplicar_operacion(sumar_dos, nums) 


# def main():
#     sumar = lambda a, b, c: a + b + c # nombre_funcion = lambda <variables> : <expresion>
#     print(sumar(20,30,50))


# def aplicar_operaciones(num):
#     operaciones = [abs, float, str] # guardamos en la lista "operaciones" tres funciones "abs" valor absoluto "Float" convertir a como flotante y "str" convertir string

#     resultado = []
#     for operacion in operaciones:
#         resultado.append(operacion(num)) # agregamos a la lista "resultados" el resultado de la funciones contenidas en "operaciones" y a las cuales accedemos rrecorriendo con "operacion" y pasando el parametro "num"
    
#     return resultado

# def main():
#     print(aplicar_operaciones(-2))


# def aplicar_operaciones(num1, num2, S, R):
#     operaciones = [S, R, abs, float]
#     resultado = []

#     for operacion in operaciones:
#         if operacion == abs or operacion == float :
#             resultado.append(operacion(num1))
#         else: 
#             resultado.append(operacion(num1, num2))
#     return resultado


# def coordenadas():
#     return (5, 4)


# def main():
#     my_tuple = ()    # las tuplas se crean con parentesis
#     type(my_tuple)   # funcion para mostrar el tipo de dato
#     my_tuple = (1, 'dos', True)  # crea una tupla con distintos tipos de datos
    
#     my_tuple[1]  # accedemos al valor almacenado en la posicion 1 de la tupla (las posiciones comienzan en [0])
#     #my_tuple[0] = 2 # esto da error porque no se puede modificar los valores de la tupla 
    
#     my_tuple = (1,) # para crear una tupla de un solo valor hay que colocar coma ,
#     my_other_tuple = (2, 3, 4)
#     my_tuple += my_other_tuple  # asigna una tupla a la otra y se agregan los elementos

#     x, y, z = my_other_tuple  # desempaqueta la tupla y asigna cada dato de la tupla a las variables x, y, z correlativamente
    
#     coordenada = coordenadas() # podemos utilizar las tuplas para obtener varios valores a la vez de una funcion
#     print(coordenada)
#     print(my_tuple)
#     print(my_other_tuple)
#     print(str(x) + str(y) + str(z))


# def main():
#     sumar = lambda x, y: x + y 
#     restar = lambda x, y: x -y
#     print(aplicar_operaciones((int(input('Escoge un numero: '))), int(input('Escoge otro numero: ')), sumar, restar))


# def main(): # Range

#     impares_asc = range(1, 100, 2)
#     impares_des = range(99, 0, -2)
#     respuesta=int(input('Elija (1) Impares ascendentes ó (2) Impares descendentes: '))
#     if respuesta == 1:
#         for i in impares_asc:
#             print(i)
#     elif respuesta == 2:
#         for i in impares_des:
#             print(i)


# def es_primo(i):
#     contador = 1
#     divisible = 0
#     while contador <= i:
#         if i % contador == 0 and i != 1:
#             divisible += 1
#         contador += 1
#     if divisible ==2:
#         return True
#     else:
#         return False


# def main():
#     naturales_al_100 = list(range(1,101))
#     print(naturales_al_100)
#     primos = [i for i in naturales_al_100 if es_primo(i)]
#     print(primos)


# def main():
#     my_dict = {
#         'David':35,
#         'Erika':32,
#         'Jaime':50,
#     }
#     print(my_dict)
#     print(my_dict['David'])

#     print(my_dict.get('Lucas',17))
    
#     my_dict['Jaime'] = 20
#     print(my_dict)

#     my_dict['Pedro'] = 70
#     print(my_dict)

#     del my_dict['Jaime']
#     print(my_dict)

#     for llave in my_dict.keys():
#         print(llave)

#     for valores in my_dict.values():
#         print(valores)

#     for llave, valor in my_dict.items():
#         print(llave,valor)

#     print('David' in my_dict)
#     print('Tom' in my_dict)



# def suma(num_1, num_2):
#     return abs(num_1) + num_2

# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)

#     def test_suma_dos_negativos(self):
#         num_1 = -10
#         num_2 = -7

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, -17)

# def es_mayor_de_edad(edad):
#     if edad >= 18:
#         return True
#     else:
#         return False

# class PruebaDeCristalTest(unittest.TestCase):
    
#     def test_es_mayor_de_edad(self):
#         edad = 20
        
#         resultado = es_mayor_de_edad(edad)

#         self.assertEqual(resultado, True)
    
#     def test_es_menor_de_edad(self):
#         edad = 15

#         resultado = es_mayor_de_edad(edad)

#         self.assertEqual(resultado, False)

# def divide_elementos_de_lista(lista, divisor):
#     try:
#         return [i / divisor for i in lista]
#     except ZeroDivisionError as e:
#         print(f'e: {e}')
#         return lista

# def main():
#     lista = list(range(10))
#     divisor = 0

#     print(divide_elementos_de_lista(lista, divisor))

# if __name__ == '__main__':
#     main()

# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


def main():
    lista_de_palabras = ['perro','gato',8,'jirafa']
    print(f'Lista primera letra: {primera_letra(lista_de_palabras)}')


if __name__ == '__main__':
    main()