'''def multiplicar_por_dos(n):
    return n * 2


def sumar_dos(n):
    return n + 2


def aplicar_operacion(f, numeros): # f guarda el nombre de la funcion "multiplicar_por_dos" ó "sumar_dos"
    resultados = []
    for numero in numeros:     # recorre a la cadena "numeros" (que es igual a "nums") desde la posicion 1 hasta el final (3)
        resultado = f(numero) # aqui llamo a la funcion "multiplicar_por_dos" ó "sumar_dos" con el parametro "numero"
        resultados.append(resultado)
    print(resultados)


def main():
    nums = [10, 20, 30]
    aplicar_operacion(multiplicar_por_dos, nums)
    aplicar_operacion(sumar_dos, nums) 


def main():
    sumar = lambda a, b, c: a + b + c # nombre_funcion = lambda <variables> : <expresion>
    print(sumar(20,30,50))


def aplicar_operaciones(num):
    operaciones = [abs, float, str] # guardamos en la lista "operaciones" tres funciones "abs" valor absoluto "Float" convertir a como flotante y "str" convertir string

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num)) # agregamos a la lista "resultados" el resultado de la funciones contenidas en "operaciones" y a las cuales accedemos rrecorriendo con "operacion" y pasando el parametro "num"
    
    return resultado

def main():
    print(aplicar_operaciones(-2))


def aplicar_operaciones(num1, num2, S, R):
    operaciones = [S, R, abs, float]
    resultado = []

    for operacion in operaciones:
        if operacion == abs or operacion == float :
            resultado.append(operacion(num1))
        else: 
            resultado.append(operacion(num1, num2))
    return resultado

def main():
    sumar = lambda x, y: x + y 
    restar = lambda x, y: x -y
    print(aplicar_operaciones((int(input('Escoge un numero: '))), int(input('Escoge otro numero: ')), sumar, restar))
'''

def main():

    impares_asc = range(1, 100, 2)
    impares_des = range(99, 0, -2)
    respuesta=int(input('Elija (1) Impares ascentes ó (2) Impares descendentes: '))
    if respuesta == 1:
        for i in impares_asc:
            print(i)
    elif respuesta == 2:
        for i in impares_des:
            print(i)



if __name__ == '__main__':
    main()