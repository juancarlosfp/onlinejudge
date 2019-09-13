def nivelForca(valor):
	if valor == 3: #maior valor simbólico
		return 9
	elif valor == 2:
		return 8
	elif valor == 1:
		return 7
	elif valor == 13:
		return 6
	elif valor == 11:
		return 5
	elif valor == 12:
		return 4
	elif valor == 7:
		return 3
	elif valor == 6:
		return 2
	elif valor == 5:
		return 1
	elif valor == 4:
		return 0

n = int(input())
contador = [0,0] 

for i in range(n):
	contadorInt = [0,0]
	dados = input().split()
	dados = [int(x) for x in dados]
	a,b = dados[0:3],dados[3:]
	for j in range(3):
		if nivelForca(a[j]) >= nivelForca(b[j]):
			contadorInt[0] +=1
		elif nivelForca(a[j]) < nivelForca(b[j]):
			contadorInt[1] +=1
	if contadorInt[0] > contadorInt[1]:
		contador[0] +=1
	else:
		contador[1] +=1
print(contador[0],contador[1]) #imprime 