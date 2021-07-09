import random

def criar_matriz(ordem,intervalo):    
    matriz =[]
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            numero = random.randint(intervalo[0],intervalo[1])
            linha.append(numero)
        matriz.append(linha)
    return matriz

def somar(a, b):
    c = []
    for i in range(len(a)):
        aux = []
        for j in range(len(a[0])):
            aux.append(a[i][j] + b[i][j])
        c.append(aux)
    return c
        

def subtrair(a, b):
    c = []
    for i in range(len(a)):
        aux = []
        for j in range(len(a[0])):
            aux.append(a[i][j] - b[i][j])
        c.append(aux)
    return c

def particionar(matriz):
    p1 = matriz
    p2 = matriz
    p3 = matriz
    p4 = matriz
    while(len(p1) > len(matriz)/2):
        p1 = p1[:len(p1)//2]
        p2 = p2[:len(p2)//2]
        p3 = p3[len(p3)//2:]
        p4 = p4[len(p4)//2:]
    while(len(p1[0]) > len(matriz[0])/2):
        for i in range(len(p1[0])//2):
            p1[i] = p1[i][:len(p1[i])//2]
            p2[i] = p2[i][len(p2[i])//2:]
            p3[i] = p3[i][:len(p3[i])//2]
            p4[i] = p4[i][len(p4[i])//2:]
    return p1,p2,p3,p4



