# bubbles sort: ordena uma lista comparando elementos adjacentes e trocando-os de lugar se estiverem na ordem errada. Compara pares vizinhos.

def bubble_sort(vetor):
    n = len(vetor)
    
    for i in range(n):
        # Percorre o vetor até a parte não ordenada
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                # Troca os elementos
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
        
        # Mostra o vetor após cada iteração completa
        print(f"Iteração {i + 1}: {vetor}")

# Exemplo de uso
vetor = [5, 3, 8, 4, 2]
print("vetor original: ", vetor)
bubble_sort(vetor)