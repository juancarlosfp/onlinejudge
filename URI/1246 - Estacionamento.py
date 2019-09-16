def buscaVaga(estacionamento, tam):

	vaga = 0
	i = 0
	for i in range(len(estacionamento)):
		if(estacionamento[i] == 0):

			vaga += 1
			if(vaga == tam):
				return i - tam + 1
		else:
			vaga = 0
	return -1
def removeCarro(estacionamento, placa, carros):

	for i in range(carros[placa][1]):
		estacionamento[carros[placa][0] + i] = 0

def eventoVaga(op, estacionamento, inicioVaga, tam, placa):
	for i in range(tam):
		estacionamento[inicioVaga + i] = placa

i = 0
valor = 0
while True:
	try:
		val = input()
		c, n = map(int, val.split())
		estacionamento = [0 for i in range(c)]
		espacos = c
		carros = {}
		for i in range(n):
			evt = input().split()
			if(evt[0] == "C" or evt[0] == "c"):
				placa, tam = int(evt[1]), int(evt[2])
				if(espacos >= tam):
					index = buscaVaga(estacionamento, tam)
					if(index != -1):
						eventoVaga(1, estacionamento, index, tam, placa)
						carros[placa] = (index, tam)
						espacos -= tam
						valor += 10
			elif(evt[0] == "S" or evt[0] == "s"):
				placa = int(evt[1])
				removeCarro(estacionamento, placa, carros)
				espacos += carros[placa][1]
				del carros[placa]
			
		print(valor)
		valor = 0
	except EOFError:
		break