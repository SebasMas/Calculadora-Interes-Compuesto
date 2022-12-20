A = float(input("Ingrese el capital inicial: "))
B = float(input("Ingrese la tasa de interés: "))
C = int(input("Ingrese el tiempo de ahorro en años: "))

print("Capital final: " + str(round(A * (B / 100 + 1) ** C, 2)))

