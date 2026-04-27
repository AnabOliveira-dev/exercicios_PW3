mapa = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def explorar_salas(mapa, sala, visitadas=None):
    if visitadas is None:
        visitadas = set()
    
    # evita visitar a mesma sala duas vezes
    if sala in visitadas:
        return
    
    print(sala, end=", ")
    visitadas.add(sala)
    
    # visita salas conectadas
    for proxima in mapa[sala]:
        explorar_salas(mapa, proxima, visitadas)

explorar_salas(mapa, "A")