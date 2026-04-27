def soma_elementos (vetor, i=0):
    if i == len(vetor):
        return 0
    else:
        return vetor[i] + soma_elementos(vetor, i + 1)

print(soma_elementos([4,7,2,9]))