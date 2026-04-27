rede = {
    "Renato": ["Ana", "Bruno"],
    "Ana": ["Carla"],
    "Bruno": ["Diego"],
    "Carla": [],
    "Diego": []
}

def explorar_rede(rede, usuario, visitados=None):
    if visitados is None:
        visitados = set()
    
    # evita repetição
    if usuario in visitados:
        return
    
    print(usuario, end=", ")
    visitados.add(usuario)
    
    # percorre conexões
    for amigo in rede[usuario]:
        explorar_rede(rede, amigo, visitados)

explorar_rede(rede, "Renato")