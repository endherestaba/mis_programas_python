import random

def mostrar_resultado(bueno, abrir_puerta, cambiar_a_puerta, eleccion):
    global respuesta 
    respuesta = input(f'          Abri puerta {abrir_puerta} y no estaba el premio, quieres cambiar a puerta {cambiar_a_puerta} ? S/N : ')
    if bueno:
        if respuesta == 's':
            print('                           *****  G A N A S T E  *****') 
            return cambiar_a_puerta
        else:
            print('                           ***  Lo siento perdiste  ***')
            return eleccion
    else:
        if respuesta == 's':
            print('                           ***  Lo siento perdiste  ***')
            return cambiar_a_puerta
        else:
            print('                           *****  G A N A S T E  *****')
            return eleccion
    

def main():
    seguir = 's'
    premios = []
    elecciones = []
    nuevas_elecciones = []
    cambios = []
    jugadas = 0
    ganados = 0
    cambio = 0
    print('          ***  BIENVENIDO AL JUEGO TRES PUERTAS ***')
    while seguir == 's':
        abrir_puerta = 0
        puertas = ['vacio','vacio','vacio']
        puertas_vacias = []
        puertas[random.randint(0,2)] = 'premio'  # se genera el indice/numero de puerta y se asigna en ese indice la palabra premnio
        print(f'puertas:  {puertas}')
        print('*******************  JUEGO N° ' + str(jugadas + 1) + '  **********************')
        eleccion = int(input("""          Elija una puerta 
                1
                2
                3
          Puerta: """))
        for i, v in enumerate(puertas): # accede al indice y al valor de la lista con la funcion enumerate()
            if v == 'premio':
                puerta_premio = i + 1
            else:
                puertas_vacias.append(i+1)

        print(f'                                   puerta premio: {puerta_premio}      puertas vacias: {puertas_vacias}     eleccion: {eleccion}')
        if eleccion == puerta_premio:
            abrir_puerta = random.choice(puertas_vacias)
            print(f'abrir puerta: {abrir_puerta}')
            if abrir_puerta == puertas_vacias[0]:
                nueva_eleccion = mostrar_resultado(False, abrir_puerta, puertas_vacias[1], eleccion)
            else: 
                nueva_eleccion = mostrar_resultado(False, abrir_puerta, puertas_vacias[0], eleccion)
        else:
            if eleccion == puertas_vacias[0]:
                nueva_eleccion = mostrar_resultado(True, puertas_vacias[1], puerta_premio, eleccion)
            else:
                nueva_eleccion = mostrar_resultado(True, puertas_vacias[0], puerta_premio, eleccion)
        
        jugadas += 1
        premios.append(puerta_premio)
        elecciones.append(eleccion)
        nuevas_elecciones.append(nueva_eleccion)
        cambios.append(respuesta)
        seguir = input(f'                 Seguir jugando? S/N: ')
        print(' ')
    for i in range(jugadas):
        if cambios[i] == 's':
            cambio += 1
            if nuevas_elecciones[i] == premios[i]:
                print(f'Jugada {i+1}     Eleccion {elecciones[i]}     Nueva eleccion {nuevas_elecciones[i]}    Premio puerta {premios[i]}     Cambio {cambios[i]}     Ganó')
                ganados += 1
            else:
                print(f'Jugada {i+1}     Eleccion {elecciones[i]}     Nueva eleccion {nuevas_elecciones[i]}    Premio puerta {premios[i]}     Cambio {cambios[i]}     Perdió')
                
        else:
            if elecciones[i] == premios[i]:
                print(f'Jugada {i+1}     Eleccion {elecciones[i]}     Nueva eleccion {nuevas_elecciones[i]}    Premio puerta {premios[i]}     Cambio {cambios[i]}     Ganó')
                ganados += 1              
            else:
                print(f'Jugada {i+1}     Eleccion {elecciones[i]}     Nueva eleccion {nuevas_elecciones[i]}    Premio puerta {premios[i]}     Cambio {cambios[i]}     Perdió')
                
    print(' ')
    print(f'JUGADOS: {i+1}     GANADOS: {ganados} ({round(ganados/(i+1)*100, 2)}%)     CAMBIOS: {cambio} ({round(cambio/(i+1)*100, 2)}%)')
   
if __name__ == '__main__':
    main()