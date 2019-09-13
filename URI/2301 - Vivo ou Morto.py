n = input().split()

qndParticipantes = int(n[0])
qndRodadas = int(n[1])

t=1
while qndParticipantes != 0 and qndRodadas != 0:
	ordem = input().split()
	ordem = [int(i) for i in ordem]

	
	for k in range(qndRodadas):

		dados = input().split()

		qndPartRodada = int(dados[0])
		comandoPart =int(dados[1])
	
		ordemRodada = [[ordem[i],int(dados[i+2])] for i in range(qndPartRodada)]
	
		x=0
		if(len(ordem)>1):
			while x<len(ordem):
				if ordemRodada[x][1] != comandoPart:
					ordemRodada.pop(x)
					ordem.pop(x)
				else:
					x+=1
	print("Teste",t)
	t+=1
	print(ordem[0])
	print()

	n = input().split()
	qndParticipantes = int(n[0])