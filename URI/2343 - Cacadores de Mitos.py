n = int(input())
mapa = []
temp = []
t = 0
count = 0

for i in range(507):
	temp = []
	for j in range(507):
		temp.append(0)
	mapa.append(temp)

while count < n and t != 1:
	dados = input().split()
	x = int(dados[0])
	y = int(dados[1])
	mapa[x][y] += 1
	
	if mapa[x][y] > 1:
		t=1
	else:
		count +=1
print(t)