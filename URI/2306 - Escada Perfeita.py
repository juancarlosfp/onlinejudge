n = int(input()) 
pilhas = input().split()
pilhas = [int(x) for x in pilhas]

soma = 0

for x in pilhas:
	soma += x

a0 = int(soma/n - ( n - 1)/2)

pilhasNova = [( a0 + y ) for y in range(n)]
somaNew = 0
for x in pilhasNova:

	somaNew += x

if somaNew == soma :
	i = 0

	t = 0

	while i < n :
		if pilhas[i] > pilhasNova[i] :
			t += pilhas[i] - pilhasNova[i]
			pilhas[i] -= t
		elif pilhas[i] < pilhasNova[i] : 
			t+=pilhasNova[i] - pilhas[i]
			pilhas[i] += t
		
		i+=1

	print(int(t/2))
else:
	print("-1")