
class Hotel:
    def __init__(self, nombre_del_hotel, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0
        self.nombre_del_hotel = nombre_del_hotel

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    
    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    
    def ocupacion_total(self):
        return self.huespedes


def main():
    Hoteles = [] # Lista hoteles
    nombres = ['A','B','C','D','E','F','G','H','I','J']
    for i, v in enumerate(nombres):
        Hoteles.append(Hotel(v,50-i, 20-i))
        Hoteles[i].anadir_huespedes(30-i)

    for hotel in Hoteles:  
        print(f'Hotel: {hotel.nombre_del_hotel}     Ocup Tot: {hotel.ocupacion_total()}     Nume max de huesp: {hotel.numero_maximo_de_huespedes}     Lug de estac: {hotel.lugares_de_estacionamiento} ')


if __name__ == '__main__':
    main()