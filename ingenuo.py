def tradicional(a,b):    
    c = []
    for i in range(len(a)):
        aux = []
        for j in range(len(b)):
            soma = 0
            for k in range(len(a)):
                soma+=(a[i][k]*b[k][j])
            aux.append(soma)
        c.append(aux)
    return c
