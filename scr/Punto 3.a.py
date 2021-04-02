import numpy as np

p1=np.float128(102201)/np.float128(500)
p2=np.float128(102692)/np.float128(1000)
alpha=np.float128(0.2734)
beta=np.float128(0.4867)
np.float128(p1)
np.float128(p2)
np.float128(alpha)
np.float128(beta)

n=294 #Resultado del punto 2
m=155 #Resultado del punto 2


print("PUNTO 3")

def primera_parte (a, k,result):
    j = 1
    while j<k:
        result *= a/np.float128(j)
        j=j+np.float128(1)
    return np.float128(result)

def error (p, k):
    vector = []
    i= 1
    while i < k:
        vector.append (primera_parte(p/np.float128(2), np.float128(i),p/np.float128(2))*((p**np.float128(2))/(np.float128(i+1)*np.float128(i+2))))
        i=np.float128(i) + np.float128(1)
    return vector

resultado1=error(p1,n)
resultado2=error(p2,m)

k=0
sumatoria1=0
sumatoria2=0
while k<len(resultado1):
    sumatoria1=np.float128(sumatoria1)+resultado1[k]
    k+=1

j=0
while j<len(resultado2):
    sumatoria2= np.float128(sumatoria2)+resultado2[j]
    j+=1

print("Sumatorias parciales:",sumatoria1,sumatoria2)


def calculo_T(a,b,sum1,sum2):
    calculo=a*sum1+b*sum2
    return np.float128(calculo)

def cp_alpha(a,b,sum1,sum2,e):
    t=calculo_T(a,b,sum1,sum2)
    tperturbado=calculo_T(a*(np.float128(1)+e),b,sum1,sum2)
    return (tperturbado - t)/(e*t)

def cp_beta (a,b,sum1,sum2,e):
    t=calculo_T(a,b,sum1,sum2)
    tperturbado=calculo_T(a,b*(np.float128(1)+e),sum1,sum2)
    return (tperturbado - t)/(e*t)

def cp_total(a,b,sum1,sum2,h1,h2):
    cp1=cp_alpha(a,b,sum1,sum2,h1)
    cp2=cp_beta(a,b,sum1,sum2,h2)
    return abs(cp1)+abs(cp2)

#SI QUIERO VER EL CP_ALPHA PARA DISTINTOS h POSITIVOS LLAMO A ESTA FUNCIÓN
def calcular_h1_pos(a,b,sum1,sum2):
    e=0.1
    while (e>10**-15): #Deducción a partir del gráfico del cp respecto a e
        print(abs(cp_alpha(a, b, sum1, sum2, e)))
        e=e/10
    return e

#SI QUIERO VER EL CP_ALPHA PARA DISTINTOS h NEGATIVOS LLAMO A ESTA FUNCIÓN
def calcular_h1_neg(a,b,sum1,sum2):
    e=0.1
    while (e>10**-15): #Deducción a partir del gráfico del cp respecto a e
        print(abs(cp_alpha(a, b, sum1, sum2, -e)))
        e=e/10
    return e
#calcular_h1_pos(np.float128(alpha),np.float128(beta),np.float128(sumatoria1),np.float128(sumatoria2))
#print("NEGATIVAS")
#calcular_h1_neg(np.float128(alpha),np.float128(beta),np.float128(sumatoria1),np.float128(sumatoria2))

#VALORES PARA H POSITIVO
h1=np.float128(10**-11) #Deducido a partir del gráfico. Después el cp varía mucho más
h2=np.float128(0.1)    #No varía el cp ya que la sumatoria2 es muy chica respecto a sumatoria1

#VALORES PARA H NEGATIVO
h1n=np.float128((10**-11)) #Deducido a partir del gráfico. Después el cp varía mucho más
h2n=np.float128(0.1)    #No varía el cp ya que la sumatoria2 es muy chica respecto a sumatoria1

#IMPRIMO VALOR DE CP TOTAL CON PERTURBACIONES POSITIVAS
print ("Cp perturbaciones con h positiva= ",cp_total(np.float128(alpha),np.float128(beta),np.float128(sumatoria1),np.float128(sumatoria2),+h1,+h2))

#IMPRIMO VALOR DE CP TOTAL CON PERTURBACIONES NEGATIVAS
print ("Cp perturbaciones con h negativa= ",cp_total(np.float128(alpha),np.float128(beta),np.float128(sumatoria1),np.float128(sumatoria2),-h1n,-h2n))

print("Con h negativo tenemos una mejor estimación del pc")
#IMPRIMO VALOR DE CP CALCULADO ANALÍTICAMENTE
cp_analitico=((sumatoria1)*alpha+(sumatoria2)*beta)/calculo_T(alpha,beta,sumatoria1,sumatoria2)
print("Cp analitico=",cp_analitico)


#HACEMOS UNA FUNCIÓN PARA PODER APROVECHAR AL MÁXIMO LOS VALORES DE CPBETA PARA DISTINTOS H

def cpbeta(a,b,e):
    sum1 = 0
    sum2 = 0
    l=0
    while l < len(resultado1):
        sum1 = np.float128(sum1) + resultado1[l]
        l += 1

    m = 0
    while m < len(resultado2):
        sum2 = np.float128(sum2) + resultado2[m]
        m += 1

    cp = (((a*sum1)+(b*(1+e))*sum2)-(a*sum1+b*sum2))/((a*sum1+b*sum2)*e)
    return cp

#SI QUIERO H NEGATIVOS PASO POR PARÁMETRO -e
def calcular_h1(a,b):
    e=0.1
    while (e>10**-15): #Deducción a partir del gráfico del cp respecto a e
        print(abs(cpbeta(a, b, e)))
        e=e/10
    return e


#IMPRIME LOS CPBETA: DAN TODOS 0. Los comentamos para no imprimir tantas cosas

#print("CPBETA:")
#calcular_h1(alpha,beta)


