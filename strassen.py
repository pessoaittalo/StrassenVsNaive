import gerenciadorDeMatrizes as gm
import ingenuo as ig



def strassen(a, b,ordem):
    # Caso Base
    if (len(a) == 2**5):
        c = gm.criar_matriz(2**5,[0,0])
        c = ig.tradicional(a,b)
        return c
    else:
       
        a11, a12, a21, a22 = gm.particionar(a)
        b11, b12, b21, b22 = gm.particionar(b)
        
        p1 = strassen(gm.somar(a11,a22), gm.somar(b11,b22), ordem/2)
        p2 = strassen(gm.somar(a21,a22), b11, ordem/2)
        p3 = strassen(a11, gm.subtrair(b12,b22), ordem/2)        
        p4 = strassen(a22, gm.subtrair(b21,b11), ordem/2)
        p5 = strassen(gm.somar(a11,a12), b22, ordem/2)        
        p6 = strassen(gm.subtrair(a21,a11), gm.somar(b11,b12), ordem/2)        
        p7 = strassen(gm.subtrair(a12,a22), gm.somar(b21,b22), ordem/2)
        
        c11 = gm.somar(gm.subtrair(gm.somar(p1, p4), p5), p7)
        c12 = gm.somar(p3, p5)
        c21 = gm.somar(p2, p4)        
        c22 = gm.somar(gm.subtrair(gm.somar(p1, p3), p2), p6)

        c = gm.criar_matriz(len(c11)*2,[0,0])
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j] = c11[i][j]
                c[i][j+len(c11)] = c12[i][j]
                c[i+len(c11)][j] = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c
  
