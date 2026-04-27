def contagem_regressiva (n):
    if n == 0:
        return 0
    else: 
        print (n)
        contagem_regressiva(n-1)
    
contagem_regressiva(5)
