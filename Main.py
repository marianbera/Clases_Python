from Automovil import Automovil
from AutomovilVolador import AutomovilVolador

class Main:
    # auto = Automovil("rojo", "ferrari", 10, 5)
    # print(f"Numero de ruedas: {auto.ruedas}")
    # print(f"Aceleración: {auto.aceleracion}")

    # auto.aceleracion = 20
    # print(f"Aceleración: {auto.aceleracion}")

    # auto2 = Automovil("azul", "fiat", 20, 10)
    
    # # print(f"El auto acelera a {auto2.acelera()} km")
    # print(f"El auto frena a {auto2.frena()} km")

    autoVolador = AutomovilVolador("negro", "ford", 15, 10,True)

    print(autoVolador.color)
    print(autoVolador.marca)
    print(autoVolador.velocidad)
    print(autoVolador.aceleracion)
    print(autoVolador.esta_volando)

    autoVolador.aterriza()
    autoVolador.vuela()

    # print("El auto " + auto.conducir())
    print("El auto " + autoVolador.conducir())