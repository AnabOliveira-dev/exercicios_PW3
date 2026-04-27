# para milhares de logs, usar algoritmos como bubble/insertion sort não é adequado,
# esses algoritmos funcionam melhor com listas pequenas.

# o algoritmo ideal é o Merge Sort, pois mesmo com grande volume de dados ele consegue se manter estável.


def merge_sort(logs):
    if len(logs) <= 1:
        return logs

    #separando o array
    meio = len(logs) // 2
    esquerda = merge_sort(logs[:meio])
    direita = merge_sort(logs[meio:])

    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        # comparando direta das strings de timestamp
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    return resultado

# exemplo
logs = [
    "2025-03-01 10:15:30",
    "2024-12-25 08:00:00",
    "2025-03-01 09:00:00",
    "2023-01-01 00:00:01"
]

#chamando função 
ordenado = merge_sort(logs)

#exibindo
for log in ordenado:
    print(log)