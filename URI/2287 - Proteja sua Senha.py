def pegarLetrasPadrao():
	dados = input().split()
	letras = dados[10:]
	padrao = [[int(dados[i]),int(dados[i+1])] for i in range(0,10,2)]
	
	return letras,padrao

def qualNumeros(letras,padrao):
	senha = []
	for i in range(6):
		if letras[i] == 'A':
			senha.append(padrao[0])
		elif letras[i] == 'B':
			senha.append(padrao[1])
		elif letras[i] == 'C':
			senha.append(padrao[2])
		elif letras[i] == 'D':
			senha.append(padrao[3])
		else:
			senha.append(padrao[4])
	return senha

def checagemParPar(referencia,lista,mapa):
	
	if len(referencia) == len(lista):
		for i in range(6):
			if referencia[i][0] in lista[i]:
				mapa[i][0] +=1
				
			elif referencia[i][1] in lista[i]:
				mapa[i][1] += 1
	return None
	
def quemGanha(ref,conc,m):
	string = ""
	for i in range(6):

		if conc[i][0] == m-1:
			string += "%d "%ref[i][0] 
		else:
			string += "%d "%ref[i][1]
	print(string)

	return None


n = int(input())
t = 0

while n != 0:
	count = [[0,0] for i in range(6)]
	words,pattern = pegarLetrasPadrao()
	primeiraSenha = qualNumeros(words,pattern)

	
	t +=1
	print("Teste",t)
	for i in range(n-1):

		words,pattern = pegarLetrasPadrao()
		senha = qualNumeros(words,pattern)
		
		checagemParPar(primeiraSenha,senha,count)
	
	quemGanha(primeiraSenha,count,n)
	print()
	n = int(input())