# insertion sort:   ordenando um elemento de cada vez, inserindo-o 
#                   na posição correta dentro de uma sublista já ordenada à esquerda

def insertion_sort_palavras(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        # comparando ignorando maiúsculas/minúsculas
        while j >= 0 and vetor[j].lower() > chave.lower(): # deixando todas as letras minusculas
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave

    return vetor

palavras = ["Banana", "maçã", "Abacaxi", "laranja", "uva"]
ordenado = insertion_sort_palavras(palavras)

print("Ordenado:", ordenado)