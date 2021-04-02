p1=102201/500
p2=102692/1000
error_total=10**(-6)
error1= error_total/2
error2= error1

print("PUNTO 2")

def decrece (p):
    k=0
    while ((p**2)/((k+1)*(k+3)*4)>1):
        k=k+1
    return k

decrece1=decrece(p1)
decrece2=decrece(p2)

print("La serie 1 decrece en n =",decrece1)
print("La serie 2 decrece en m =",decrece2)

def primera_parte (a, k):
    result = a
    j = 1
    while j<k:
        result *= a/j
        j=j+1
    return result

def error (p, k):
    vector = []
    i= decrece(p)
    while i < k:
        vector.append (primera_parte(p/2, i)*((p**2)/((i+1)*(i+2))))
        i+=1
    return vector

resultado1=error(p1,1000)
resultado2=error(p2,1000)


k=0
while resultado1[k]>error1:
    k = k + 1
k=k+decrece1
print("Las n necesarias =",k)

k=0
while resultado2[k]>error2:
    k = k + 1
k=k+decrece2
print("Las m necesarias =", k)


