def decodificar(msg):
    # caso base
    if len(msg) == 1:
        print(msg)
        return
    
    # imprime a string atual
    print(msg)
    
    # chamada recursiva removendo o primeiro caractere
    decodificar(msg[1:])

decodificar("abc")