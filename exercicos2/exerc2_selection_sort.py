# selection sort: funciona dividindo a lista em uma parte ordenada e outra desordenada, 
#                 selecionando repetidamente o menor elemento da parte desordenada e movendo-o 
#                 para o final da parte ordenada.

def selection_sort_desc(vetor):
    n = len(vetor)  #tamanho do vetor
    trocas = 0      #numero de trocas

    for i in range(n):
        # assumindo que o maior elemento está na posição i
        indice_max = i

        # procurando o maior elemento no restante do vetor
        for j in range(i + 1, n):
            if vetor[j] > vetor[indice_max]:
                indice_max = j

        # trocade posição se necessário
        if indice_max != i:
            vetor[i], vetor[indice_max] = vetor[indice_max], vetor[i]
            trocas += 1

    return vetor, trocas

vetor = [5, 3, 8, 4, 2]
ordenado, total_trocas = selection_sort_desc(vetor)

print("Vetor ordenado (decrescente):", ordenado)
print("Total de trocas:", total_trocas)