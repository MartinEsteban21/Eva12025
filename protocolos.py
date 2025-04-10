protocolo = input("Ingrese un protocolo (OSPF, RIP, EIGRP, BGP): ").upper()

# Verificar y mostrar la distancia administrativa correspondiente
if protocolo == "OSPF":
    print("El protocolo OSPF tiene una distancia administrativa de 110.")
elif protocolo == "RIP":
    print("El protocolo RIP tiene una distancia administrativa de 120.")
elif protocolo == "EIGRP":
    print("El protocolo EIGRP tiene una distancia administrativa de 90.")
elif protocolo == "BGP":
    print("El protocolo BGP tiene una distancia administrativa de 20.")
else:
    print("Protocolo no reconocido. Intente con OSPF, RIP, EIGRP o BGP.")
