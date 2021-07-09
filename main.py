import strassen as st
import ingenuo as ig
import gerenciadorDeMatrizes as gm
import time
import timeit
import matplotlib.pyplot as plt

kMax = int(input("Digite o kMax: "))
while(kMax < 5):
    print("Entrada inválidada! Informe um valor >= 5")
    kMax = int(input("Digite o kMax: "))
r = int(input("Digite o r: "))
intervalo = []
for i in range(2):
    if(i == 0):
        print("aMin")
    else:
        print("aMax")
    intervalo.append(int(input("Digite o valor: " )))

y_normal = []
x_normal = []
y_strassen =[]
x_strassen = []


print(intervalo)
for i in range(5,kMax+1):
    inicio = timeit.default_timer() 
    a = gm.criar_matriz(2**i,intervalo)
    b = gm.criar_matriz(2**i,intervalo)
    c = []  
    for j in range(r):
        c = ig.tradicional(a,b)
    fim = timeit.default_timer()
    y_normal.append((fim - inicio)/r)        
    x_normal.append(2**i)

print("fim tradicional")
for i in range(5,kMax+1):
    inicio = timeit.default_timer() 
    a = gm.criar_matriz(2**i,intervalo)
    b = gm.criar_matriz(2**i,intervalo)
    c = []  
    for j in range(r):
        c = st.strassen(a,b,2**i)
    fim = timeit.default_timer()
    y_strassen.append((fim - inicio)/r)        
    x_strassen.append(2**i)
print("Fim Strassen")

plt.xlabel("Ordem")
plt.ylabel("Tempo")
plt.plot(x_normal,y_normal,label="Tradicional")
plt.plot(x_strassen,y_strassen,label="Strassen")
plt.legend()
plt.show()
    

    
                         
    
