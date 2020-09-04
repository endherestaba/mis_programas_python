import random

def mostrar_resultado(cambio_positivo, abrir_puerta, cambiar_a_puerta, eleccion, puerta_premio):
    global respuesta
    respuesta = ''
    while respuesta.lower() != 's' and respuesta.lower() != 'n':
        respuesta = input(f'          Abri la puerta {abrir_puerta} y no estaba el premio, quieres cambiar a la puerta {cambiar_a_puerta} ? S/N : ')
    
        if respuesta.lower() == 's':
            if cambio_positivo:
                print('                                                   *  ! F E L I C I D A D E S !    G A N A S T E  *') 
            else:
                print(f'                                                   * UFF!!! PERDISTE, el premio estaba en la puerta {puerta_premio} *')

            return cambiar_a_puerta
        
        elif respuesta.lower() == 'n':
            if cambio_positivo:
                print(f'                                                   * UFF!!! PERDISTE, el premio estaba en la puerta {puerta_premio} *')
            else:
                print('                                                   *  ! F E L I C I D A D E S !    G A N A S T E  *')

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
    print('')
    print('            * BIENVENIDO AL JUEGO DE LAS TRES PUERTAS *')
    print('         ( Una de las 3 puertas contiene un premio, elige bien! )')
    while seguir.lower() != 'n':
        abrir_puerta = 0
        puertas = ['vacio','vacio','vacio']
        puertas_vacias = []
        puertas[random.randint(0,2)] = 'premio'  # se genera el indice/numero de puerta y se asigna en ese indice la palabra premnio
        print('')
        print('*******************  ROUND ' + str(jugadas + 1) + '  **********************')
        eleccion = int(input("""          Elije una puerta 
                1                2                3
          Puerta: """))
        for i, v in enumerate(puertas): # accede al indice y al valor de la lista con la funcion enumerate()
            if v == 'premio':
                puerta_premio = i + 1
            else:
                puertas_vacias.append(i+1)

        #print(f'                                   puerta premio: {puerta_premio}      puertas vacias: {puertas_vacias}     eleccion: {eleccion}')
        if eleccion == puerta_premio:
            abrir_puerta = random.choice(puertas_vacias)
            #print(f'abrir puerta: {abrir_puerta}')
            if abrir_puerta == puertas_vacias[0]:
                nueva_eleccion = mostrar_resultado(False, abrir_puerta, puertas_vacias[1], eleccion, puerta_premio)
            else: 
                nueva_eleccion = mostrar_resultado(False, abrir_puerta, puertas_vacias[0], eleccion, puerta_premio)
        else:
            if eleccion == puertas_vacias[0]:
                nueva_eleccion = mostrar_resultado(True, puertas_vacias[1], puerta_premio, eleccion, puerta_premio)
            else:
                nueva_eleccion = mostrar_resultado(True, puertas_vacias[0], puerta_premio, eleccion, puerta_premio)
        
        jugadas += 1
        premios.append(puerta_premio)
        elecciones.append(eleccion)
        nuevas_elecciones.append(nueva_eleccion)
        cambios.append(respuesta)
        seguir = input(f'                 Seguir jugando? S/N: ')
    print(' ')
    print('RESULTADOS:')
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