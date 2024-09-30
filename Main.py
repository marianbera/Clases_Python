from Automovil import Automovil

class Main:
    auto = Automovil("rojo", "ferrari", 10, 5)
    print(f"Numero de ruedas: {auto.ruedas}")
    print(f"Aceleración: {auto.aceleracion}")

    auto.aceleracion = 20
    print(f"Aceleración: {auto.aceleracion}")


    auto2 = Automovil("azul", "fiat", 20, 10)
    
    # print(f"El auto acelera a {auto2.acelera()} km")
    print(f"El auto frena a {auto2.frena()} km")
