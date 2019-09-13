n, distMax = map(int, input().split())

pista = [int(x) for x in input().split()]

#subtrações 2 a 2
flag = True
for i in range(1, len(pista)):
    soma = pista[i] - pista[i-1]
    if(soma >distMax):
        flag = False
        break

if(flag == True):
    soma = 42195 - pista[-1]
    if(soma > distMax):
        flag = False

if(flag == False):
    print("N")
else:
    print("S")