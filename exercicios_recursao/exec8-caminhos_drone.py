def contar_caminhos(n, m):
    # caso base: chegou na última linha ou última coluna
    if n == 1 or m == 1:
        return 1
    
    # soma dos caminhos possíveis
    return contar_caminhos(n - 1, m) + contar_caminhos(n, m - 1)

print(contar_caminhos(2, 2))  # 2
print(contar_caminhos(3, 3))  # 6