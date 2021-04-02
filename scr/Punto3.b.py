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
sumatoria64 = (2.661098206940074)*(10**46) #Calculado con el mismo código pero sin escribir np.float128. Por default trabaja en np.float64
cp_perturbaciones=1.0000000034524349414 #Resultado del punto 3.1
mu10_64=0.5*(10**-15) #Resultado del punto 1
mu10_128=0.5*(10**-19) #Resultado del punto 1


def primera_parte (a, k,result):
    j = 1
    while j<k:
        result=np.float128(result) * np.float128(a/np.float128(j))
        j=np.float128(j)+np.float128(1)
    return np.float128(result)

def error (p, k):
    vector = []
    i= 1
    while i < k:
        vector.append (np.float128(primera_parte(np.float128(p/np.float128(2)), np.float128(i),np.float128(p/np.float128(2)))*((np.float128(p**np.float128(2)))/(np.float128(i+1)*np.float128(i+2)))))
        i=np.float128(i) + np.float128(1)
    return np.float128(vector)


resultado1=0
resultado2=0
np.float128(resultado1)
np.float128(resultado2)

resultado1=np.float128(error(np.float128(p1),n))
resultado2=np.float128(error(np.float128(p2),m))

k=0
sumatoria1=0
sumatoria2=0
np.float128(sumatoria1)
np.float128(sumatoria2)
while k<len(resultado1):
    sumatoria1=np.float128(np.float128(sumatoria1)+np.float128(resultado1[k]))
    k+=1

print("Sumatoria1=", sumatoria1)
j=0
while j<len(resultado2):
    sumatoria2= np.float128(np.float128(sumatoria2)+np.float128(resultado2[j]))
    j+=1

print("Sumatoria2=", sumatoria2)
def calculo_T(a,b,sum1,sum2):
    calculo=np.float128(np.float128(np.float128(a)*np.float128(sum1))+np.float128(np.float128(b)*np.float128(sum2)))
    return np.float128(calculo)

#Sumatorias calculadas sin iterar. Dan el mismo resultado
suma1=0
np.float128(suma1)
suma1=np.float128(resultado1[0])+np.float128(resultado1[1])+np.float128(resultado1[2])+np.float128(resultado1[3])+np.float128(resultado1[4])+np.float128(resultado1[5])+np.float128(resultado1[6])+np.float128(resultado1[7])+np.float128(resultado1[8])+np.float128(resultado1[9])+np.float128(resultado1[10])+np.float128(resultado1[11])+np.float128(resultado1[12])+np.float128(resultado1[13])+np.float128(resultado1[14])+np.float128(resultado1[15])+np.float128(resultado1[16])+np.float128(resultado1[17])+np.float128(resultado1[18])+np.float128(resultado1[19])+np.float128(resultado1[20])+np.float128(resultado1[21])+np.float128(resultado1[22])+np.float128(resultado1[23])+np.float128(resultado1[24])+np.float128(resultado1[25])+np.float128(resultado1[26])+np.float128(resultado1[27])+np.float128(resultado1[28])+np.float128(resultado1[29])+np.float128(resultado1[30])+np.float128(resultado1[31])+np.float128(resultado1[32])+np.float128(resultado1[33])+np.float128(resultado1[34])+np.float128(resultado1[35])+np.float128(resultado1[36])+np.float128(resultado1[37])+np.float128(resultado1[38])+np.float128(resultado1[39])+np.float128(resultado1[40])+np.float128(resultado1[41])+np.float128(resultado1[42])+np.float128(resultado1[43])+np.float128(resultado1[44])+np.float128(resultado1[45])+np.float128(resultado1[46])+np.float128(resultado1[47])+np.float128(resultado1[48])+np.float128(resultado1[49])+np.float128(resultado1[50])+np.float128(resultado1[51])+np.float128(resultado1[52])+np.float128(resultado1[53])+np.float128(resultado1[54])+np.float128(resultado1[55])+np.float128(resultado1[56])+np.float128(resultado1[57])+np.float128(resultado1[58])+np.float128(resultado1[59])+np.float128(resultado1[60])+np.float128(resultado1[61])+np.float128(resultado1[62])+np.float128(resultado1[63])+np.float128(resultado1[64])+np.float128(resultado1[65])+np.float128(resultado1[66])+np.float128(resultado1[67])+np.float128(resultado1[68])+np.float128(resultado1[69])+np.float128(resultado1[70])+np.float128(resultado1[71])+np.float128(resultado1[72])+np.float128(resultado1[73])+np.float128(resultado1[74])+np.float128(resultado1[75])+np.float128(resultado1[76])+np.float128(resultado1[77])+np.float128(resultado1[78])+np.float128(resultado1[79])+np.float128(resultado1[80])+np.float128(resultado1[81])+np.float128(resultado1[82])+np.float128(resultado1[83])+np.float128(resultado1[84])+np.float128(resultado1[85])+np.float128(resultado1[86])+np.float128(resultado1[87])+np.float128(resultado1[88])+np.float128(resultado1[89])+np.float128(resultado1[90])+np.float128(resultado1[91])+np.float128(resultado1[92])+np.float128(resultado1[93])+np.float128(resultado1[94])+np.float128(resultado1[95])+np.float128(resultado1[96])+np.float128(resultado1[97])+np.float128(resultado1[98])+np.float128(resultado1[99])+np.float128(resultado1[100])+np.float128(resultado1[101])+np.float128(resultado1[102])+np.float128(resultado1[103])+np.float128(resultado1[104])+np.float128(resultado1[105])+np.float128(resultado1[106])+np.float128(resultado1[107])+np.float128(resultado1[108])+np.float128(resultado1[109])+np.float128(resultado1[110])+np.float128(resultado1[111])+np.float128(resultado1[112])+np.float128(resultado1[113])+np.float128(resultado1[114])+np.float128(resultado1[115])+np.float128(resultado1[116])+np.float128(resultado1[117])+np.float128(resultado1[118])+np.float128(resultado1[119])+np.float128(resultado1[120])+np.float128(resultado1[121])+np.float128(resultado1[122])+np.float128(resultado1[123])+np.float128(resultado1[124])+np.float128(resultado1[125])+np.float128(resultado1[126])+np.float128(resultado1[127])+np.float128(resultado1[128])+np.float128(resultado1[129])+np.float128(resultado1[130])+np.float128(resultado1[131])+np.float128(resultado1[132])+np.float128(resultado1[133])+np.float128(resultado1[134])+np.float128(resultado1[135])+np.float128(resultado1[136])+np.float128(resultado1[137])+np.float128(resultado1[138])+np.float128(resultado1[139])+np.float128(resultado1[140])+np.float128(resultado1[141])+np.float128(resultado1[142])+np.float128(resultado1[143])+np.float128(resultado1[144])+np.float128(resultado1[145])+np.float128(resultado1[146])+np.float128(resultado1[147])+np.float128(resultado1[148])+np.float128(resultado1[149])+np.float128(resultado1[150])+np.float128(resultado1[151])+np.float128(resultado1[152])+np.float128(resultado1[153])+np.float128(resultado1[154])+np.float128(resultado1[155])+np.float128(resultado1[156])+np.float128(resultado1[157])+np.float128(resultado1[158])+np.float128(resultado1[159])+np.float128(resultado1[160])+np.float128(resultado1[161])+np.float128(resultado1[162])+np.float128(resultado1[163])+np.float128(resultado1[164])+np.float128(resultado1[165])+np.float128(resultado1[166])+np.float128(resultado1[167])+np.float128(resultado1[168])+np.float128(resultado1[169])+np.float128(resultado1[170])+np.float128(resultado1[171])+np.float128(resultado1[172])+np.float128(resultado1[173])+np.float128(resultado1[174])+np.float128(resultado1[175])+np.float128(resultado1[176])+np.float128(resultado1[177])+np.float128(resultado1[178])+np.float128(resultado1[179])+np.float128(resultado1[180])+np.float128(resultado1[181])+np.float128(resultado1[182])+np.float128(resultado1[183])+np.float128(resultado1[184])+np.float128(resultado1[185])+np.float128(resultado1[186])+np.float128(resultado1[187])+np.float128(resultado1[188])+np.float128(resultado1[189])+np.float128(resultado1[190])+np.float128(resultado1[191])+np.float128(resultado1[192])+np.float128(resultado1[193])+np.float128(resultado1[194])+np.float128(resultado1[195])+np.float128(resultado1[196])+np.float128(resultado1[197])+np.float128(resultado1[198])+np.float128(resultado1[199])+np.float128(resultado1[200])+np.float128(resultado1[201])+np.float128(resultado1[202])+np.float128(resultado1[203])+np.float128(resultado1[204])+np.float128(resultado1[205])+np.float128(resultado1[206])+np.float128(resultado1[207])+np.float128(resultado1[208])+np.float128(resultado1[209])+np.float128(resultado1[210])+np.float128(resultado1[211])+np.float128(resultado1[212])+np.float128(resultado1[213])+np.float128(resultado1[214])+np.float128(resultado1[215])+np.float128(resultado1[216])+np.float128(resultado1[217])+np.float128(resultado1[218])+np.float128(resultado1[219])+np.float128(resultado1[220])+np.float128(resultado1[221])+np.float128(resultado1[222])+np.float128(resultado1[223])+np.float128(resultado1[224])+np.float128(resultado1[225])+np.float128(resultado1[226])+np.float128(resultado1[227])+np.float128(resultado1[228])+np.float128(resultado1[229])+np.float128(resultado1[230])+np.float128(resultado1[231])+np.float128(resultado1[232])+np.float128(resultado1[233])+np.float128(resultado1[234])+np.float128(resultado1[235])+np.float128(resultado1[236])+np.float128(resultado1[237])+np.float128(resultado1[238])+np.float128(resultado1[239])+np.float128(resultado1[240])+np.float128(resultado1[241])+np.float128(resultado1[242])+np.float128(resultado1[243])+np.float128(resultado1[244])+np.float128(resultado1[245])+np.float128(resultado1[246])+np.float128(resultado1[247])+np.float128(resultado1[248])+np.float128(resultado1[249])+np.float128(resultado1[250])+np.float128(resultado1[251])+np.float128(resultado1[252])+np.float128(resultado1[253])+np.float128(resultado1[254])+np.float128(resultado1[255])+np.float128(resultado1[256])+np.float128(resultado1[257])+np.float128(resultado1[258])+np.float128(resultado1[259])+np.float128(resultado1[260])+np.float128(resultado1[261])+np.float128(resultado1[262])+np.float128(resultado1[263])+np.float128(resultado1[264])+np.float128(resultado1[265])+np.float128(resultado1[266])+np.float128(resultado1[267])+np.float128(resultado1[268])+np.float128(resultado1[269])+np.float128(resultado1[270])+np.float128(resultado1[271])+np.float128(resultado1[272])+np.float128(resultado1[273])+np.float128(resultado1[274])+np.float128(resultado1[275])+np.float128(resultado1[276])+np.float128(resultado1[277])+np.float128(resultado1[278])+np.float128(resultado1[279])+np.float128(resultado1[280])+np.float128(resultado1[281])+np.float128(resultado1[282])+np.float128(resultado1[283])+np.float128(resultado1[284])+np.float128(resultado1[285])+np.float128(resultado1[286])+np.float128(resultado1[287])+np.float128(resultado1[288])+np.float128(resultado1[289])+np.float128(resultado1[290])+np.float128(resultado1[291])+np.float128(resultado1[292])
suma2=0
np.float128(suma2)
suma2=np.float128(resultado2[0])+np.float128(resultado2[1])+np.float128(resultado2[2])+np.float128(resultado2[3])+np.float128(resultado2[4])+np.float128(resultado2[5])+np.float128(resultado2[6])+np.float128(resultado2[7])+np.float128(resultado2[8])+np.float128(resultado2[9])+np.float128(resultado2[10])+np.float128(resultado2[11])+np.float128(resultado2[12])+np.float128(resultado2[13])+np.float128(resultado2[14])+np.float128(resultado2[15])+np.float128(resultado2[16])+np.float128(resultado2[17])+np.float128(resultado2[18])+np.float128(resultado2[19])+np.float128(resultado2[20])+np.float128(resultado2[21])+np.float128(resultado2[22])+np.float128(resultado2[23])+np.float128(resultado2[24])+np.float128(resultado2[25])+np.float128(resultado2[26])+np.float128(resultado2[27])+np.float128(resultado2[28])+np.float128(resultado2[29])+np.float128(resultado2[30])+np.float128(resultado2[31])+np.float128(resultado2[32])+np.float128(resultado2[33])+np.float128(resultado2[34])+np.float128(resultado2[35])+np.float128(resultado2[36])+np.float128(resultado2[37])+np.float128(resultado2[38])+np.float128(resultado2[39])+np.float128(resultado2[40])+np.float128(resultado2[41])+np.float128(resultado2[42])+np.float128(resultado2[43])+np.float128(resultado2[44])+np.float128(resultado2[45])+np.float128(resultado2[46])+np.float128(resultado2[47])+np.float128(resultado2[48])+np.float128(resultado2[49])+np.float128(resultado2[50])+np.float128(resultado2[51])+np.float128(resultado2[52])+np.float128(resultado2[53])+np.float128(resultado2[54])+np.float128(resultado2[55])+np.float128(resultado2[56])+np.float128(resultado2[57])+np.float128(resultado2[58])+np.float128(resultado2[59])+np.float128(resultado2[60])+np.float128(resultado2[61])+np.float128(resultado2[62])+np.float128(resultado2[63])+np.float128(resultado2[64])+np.float128(resultado2[65])+np.float128(resultado2[66])+np.float128(resultado2[67])+np.float128(resultado2[68])+np.float128(resultado2[69])+np.float128(resultado2[70])+np.float128(resultado2[71])+np.float128(resultado2[72])+np.float128(resultado2[73])+np.float128(resultado2[74])+np.float128(resultado2[75])+np.float128(resultado2[76])+np.float128(resultado2[77])+np.float128(resultado2[78])+np.float128(resultado2[79])+np.float128(resultado2[80])+np.float128(resultado2[81])+np.float128(resultado2[82])+np.float128(resultado2[83])+np.float128(resultado2[84])+np.float128(resultado2[85])+np.float128(resultado2[86])+np.float128(resultado2[87])+np.float128(resultado2[88])+np.float128(resultado2[89])+np.float128(resultado2[90])+np.float128(resultado2[91])+np.float128(resultado2[92])+np.float128(resultado2[93])+np.float128(resultado2[94])+np.float128(resultado2[95])+np.float128(resultado2[96])+np.float128(resultado2[97])+np.float128(resultado2[98])+np.float128(resultado2[99])+np.float128(resultado2[100])+np.float128(resultado2[101])+np.float128(resultado2[102])+np.float128(resultado2[103])+np.float128(resultado2[104])+np.float128(resultado2[105])+np.float128(resultado2[106])+np.float128(resultado2[107])+np.float128(resultado2[108])+np.float128(resultado2[109])+np.float128(resultado2[110])+np.float128(resultado2[111])+np.float128(resultado2[112])+np.float128(resultado2[113])+np.float128(resultado2[114])+np.float128(resultado2[115])+np.float128(resultado2[116])+np.float128(resultado2[117])+np.float128(resultado2[118])+np.float128(resultado2[119])+np.float128(resultado2[120])+np.float128(resultado2[121])+np.float128(resultado2[122])+np.float128(resultado2[123])+np.float128(resultado2[124])+np.float128(resultado2[125])+np.float128(resultado2[126])+np.float128(resultado2[127])+np.float128(resultado2[128])+np.float128(resultado2[129])+np.float128(resultado2[130])+np.float128(resultado2[131])+np.float128(resultado2[132])+np.float128(resultado2[133])+np.float128(resultado2[134])+np.float128(resultado2[135])+np.float128(resultado2[136])+np.float128(resultado2[137])+np.float128(resultado2[138])+np.float128(resultado2[139])+np.float128(resultado2[140])+np.float128(resultado2[141])+np.float128(resultado2[142])+np.float128(resultado2[143])+np.float128(resultado2[144])+np.float128(resultado2[145])+np.float128(resultado2[146])+np.float128(resultado2[147])+np.float128(resultado2[148])+np.float128(resultado2[149])+np.float128(resultado2[150])+np.float128(resultado2[151])+np.float128(resultado2[152])+np.float128(resultado2[153])
#print (np.float128(suma1))
#print (np.float128(suma2))



sumatoria128=np.float128(calculo_T (np.float128(alpha),np.float128(beta),np.float128(sumatoria1),np.float128(sumatoria2)))
print ("Sumatoria total = ",np.float128(sumatoria128))

te= (np.float128(sumatoria128)-np.float128(sumatoria64))/(np.float128(sumatoria128)*(np.float128(mu10_64)))

print("PUNTO 3:")

print("INCISO 2: Te =",abs (np.float128(te)))


#3)III
print("INCISO 3:")
error_trunc=(10**-6)/sumatoria128
print("Se desprecia el error de truncamiento ya que es muy pequeño en relación a el error de redondeo y el inherente")
print("Error de truncamiento = ", error_trunc)
error_total=te*mu10_128
print("Error total (no hay error inhrente) =",error_total)

#3)IV
error_inherente=0.5*10**-4
error_nuevo=np.float128(cp_perturbaciones)*error_inherente
error_total2=error_nuevo+error_total
print("Se suma el nuevo error (inherente) =", error_nuevo)
print("INCISO 4: Se calcula el error error total=", error_total2)

#3)V

if(error_total>error_nuevo):
    print("INCISO 5: La fuente de error más importante es el error de redondeo")
else:
    print("INCISO 5: La fuente de error más importante es el error inherente")









