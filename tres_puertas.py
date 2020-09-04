import random

def mostrar_resultado(bueno, puerta_abierta, puerta_cambiar, eleccion):
    global respuesta 
    respuesta = input(f'          Abri puerta {puerta_abierta} y no estaba el premio, quieres cambiar a puerta {puerta_cambiar} ? S/N : ')
    if bueno:
        if respuesta == 's':
            print(' ')
            print('                           *****  G A N A S T E  *****') 
            print(' ')  
            return puerta_cambiar
        else:
            print(' ')
            print('                           ***  Lo siento perdiste  ***')
            print(' ')
            return eleccion
    else:
        if respuesta == 's':
            print(' ')
            print('                           ***  Lo siento perdiste  ***')
            print(' ')
            return puerta_cambiar
        else:
            print(' ')
            print('                           *****  G A N A S T E  *****')
            print(' ')
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
    print('          ***  BIENVENIDO A TRES PUERTAS ***')
    while seguir == 's':
        puerta_premio = random.randint(1,3)
        print('*******************  JUEGO N° ' + str(jugadas + 1) + '  **********************')
        eleccion = int(input("""          Elija una puerta 
                1
                2
                3
          Puerta: """))
        #print('Puerta premio: ' + str(puerta_premio))
        if eleccion == puerta_premio:
            if eleccion == 1:
                puerta_abrir = random.randint(1,2) # 1 = 2 y 2 = 3
                if puerta_abrir == 1:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir + 1, puerta_abrir + 2, eleccion)
                else:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir + 1, puerta_abrir, eleccion) 
            elif eleccion == 2:
                puerta_abrir = random.randint(1,2) # 1 = 1 y 2 = 3
                if puerta_abrir == 1:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir, puerta_abrir + 2, eleccion)
                else:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir + 1, puerta_abrir - 1, eleccion)
            elif eleccion == 3:
                puerta_abrir = random.randint(1,2) # 1 = 1 y 2 = 2
                if puerta_abrir == 1:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir, puerta_abrir + 1, eleccion)
                else:
                    nueva_eleccion = mostrar_resultado(False, puerta_abrir, puerta_abrir - 1, eleccion)
        else:
            if puerta_premio == 1:
                if eleccion == 2:
                    nueva_eleccion = mostrar_resultado(True, 3, 1, eleccion)
                elif eleccion == 3:
                    nueva_eleccion = mostrar_resultado(True, 2, 1, eleccion)
            elif puerta_premio == 2:
                if eleccion == 1:
                    nueva_eleccion = mostrar_resultado(True, 3, 2, eleccion)
                elif eleccion == 3:
                    nueva_eleccion = mostrar_resultado(True, 1, 2, eleccion)
            elif puerta_premio == 3:
                if eleccion == 1:
                    nueva_eleccion = mostrar_resultado(True, 2, 3, eleccion)
                elif eleccion == 2:
                    nueva_eleccion = mostrar_resultado(True, 1, 3, eleccion)

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