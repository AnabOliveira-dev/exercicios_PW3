# merge sort:   dividindo recursivamente um array não ordenado ao meio até 
#               obter subconjuntos de um único elemento (que já estão ordenados), 
#               para então intercalar (merge) essas partes em ordem, 
#               criando uma estrutura ordenada final


def merge_sort(vetor, nivel=0):
    # mostrando o vetor sendo processado (divisão)
    print("  " * nivel + f"Dividindo: {vetor}")

    if len(vetor) <= 1:
        return vetor

    # separando o vetor
    meio = len(vetor) // 2
    esquerda = vetor[:meio]
    direita = vetor[meio:]

    # dividindo recursivamente
    esquerda_ordenada = merge_sort(esquerda, nivel + 1)
    direita_ordenada = merge_sort(direita, nivel + 1)

    # juntando (merge)
    return merge(esquerda_ordenada, direita_ordenada)


def merge(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # adicionando o restante
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    return resultado

vetor = [8, 3, 5, 2, 9, 1]
ordenado = merge_sort(vetor)

print("\nVetor ordenado:", ordenado)