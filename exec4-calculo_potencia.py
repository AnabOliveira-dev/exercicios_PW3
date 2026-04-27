def calculo_potencia (base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * calculo_potencia(base, expoente - 1)

print(calculo_potencia(2,4))