import numpy as np
print("PUNTO 1")
def mantisa_10_sp(i,j,k):
    a=10
    b=1
    while k>b:
        i=i+np.float32(b)
        j=j/np.float32(a)
        k=np.float32(b)+j
    return i-np.float32(b)



def mantisa_2_sp(i,j,k):
    a=2
    b=1
    while k>b:
        i=i+np.float32(b)
        j=j/np.float32(a)
        k=np.float32(b)+j
    return i-np.float32(b)

def mantisa_10_dp(i,j,k):
    while k>1:
        i=i+1
        j=j/10
        k=1+j
    return i-1

def mantisa_2_dp(i,j,k):
    while k>1:
        i=i+1
        j=j/2
        k=1+j
    return i-1

mant10_sp=mantisa_10_sp(np.float32(1),np.float32(1),np.float32(2))
mant2_sp=mantisa_2_sp(np.float32(1),np.float32(1),np.float32(2))
mant10_dp=mantisa_10_dp(1,1,2)
mant2_dp=mantisa_2_dp(1,1,2)


print ("Simple precisión: mantisa trabajando en decimal =", mant10_sp)
print ("Simple precisión: mantisa trabajando en binario =", mant2_sp)
print ("Doble precisión: mantisa trabajando en decimal =", mant10_dp)
print ("Doble precisión: mantisa trabajando en binario =", mant2_dp)

def unidad_de_maquina (m,b):
    return 0.5*b**(1-m)

mu10_sp=unidad_de_maquina(mant10_sp,10)
mu2_sp=unidad_de_maquina(mant2_sp,2)
mu10_dp=unidad_de_maquina(mant10_dp,10)
mu2_dp=unidad_de_maquina(mant2_dp,2)

print("Simple precisión: unidad de máquina en decimal =", mu10_sp)
print("Simple precisión: unidad de máquina en binario =", mu2_sp)
print("Doble precisión: unidad de máquina en decimal =", mu10_dp)
print("Doble precisión: unidad de máquina en binario =", mu2_dp)





def mantisa_10_128(i,j,k):
    a=10
    b=1
    while k>b:
        i=i+np.float128(b)
        j=j/np.float128(a)
        k=np.float128(b)+j
    return i-np.float128(b)


def mantisa_2_128(i,j,k):
    a=2
    b=1
    while k>b:
        i=i+np.float128(b)
        j=j/np.float128(a)
        k=np.float128(b)+j
    return i-np.float128(b)
def unidad_de_maquina (m,b):
    return 0.5*b**(1-m)

mant2_128=mantisa_2_128(np.float128(1),np.float128(1),np.float128(2))
mant10_128=mantisa_10_128(np.float128(1),np.float128(1),np.float128(2))

mu2_128=unidad_de_maquina(mant2_128,2)
mu10_128=unidad_de_maquina(mant10_128,10)


print ("Np.float128: mantisa trabajando en binario =", mant2_128)
print("Np.float128: mantisa trabajando en decimal =", mant10_128)
print("Np.float128: unidad de máquina en binario =", mu2_128)
print("Np.float128: unidad de máquina en decimal =",mu10_128)
