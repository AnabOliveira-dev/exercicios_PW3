# intruções: Você recebe uma lista de jogadores com nome e pontuação.
#           Ordene os jogadores por pontuação (decrescente).
#           Em caso de empate, ordene alfabeticamente pelo nome.
#           Restrição: não usar funções prontas de ordenação. 

def ordenar_jogadores(jogadores):
    for i in range(1, len(jogadores)):
        chave = jogadores[i]
        j = i - 1

        while j >= 0:
            # pontuação decrescente
            if jogadores[j]["pontuacao"] < chave["pontuacao"]:
                jogadores[j + 1] = jogadores[j]
            
            # empate -> nome crescente
            elif (jogadores[j]["pontuacao"] == chave["pontuacao"] and
                  jogadores[j]["nome"].lower() > chave["nome"].lower()):
                jogadores[j + 1] = jogadores[j]
            
            else:
                break

            j -= 1

        jogadores[j + 1] = chave

    return jogadores

# exemplo
jogadores = [
    {"nome": "Carlos", "pontuacao": 100},
    {"nome": "Ana", "pontuacao": 150},
    {"nome": "Bruno", "pontuacao": 100},
    {"nome": "Daniel", "pontuacao": 150},
    {"nome": "Eduarda", "pontuacao": 150},
]

# chamando função
ordenado = ordenar_jogadores(jogadores)

# exibindo
for j in ordenado:
    print(j)