import random # biblioteca para gerar numeros aleatórios

def bubble_sort(vetor):
    n = len(vetor)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1

    return comparacoes, trocas


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave
        movimentacoes += 1

    return comparacoes, movimentacoes


# gerando vetor aleatório
vetor = [random.randint(0, 1000) for _ in range(100)]

# cópias p cada algoritmo
vetor_bubble = vetor.copy()
vetor_insertion = vetor.copy()

# executando algoritmos
b_comp, b_trocas = bubble_sort(vetor_bubble)
i_comp, i_mov = insertion_sort(vetor_insertion)

# exibindo resultados
print("=== Bubble Sort ===")
print("qtd de comparações:", b_comp)
print("qtd de trocas:", b_trocas)

print("\n === Insertion Sort ===")
print("qtd de comparações:", i_comp)
print("qtd de movimentações:", i_mov)