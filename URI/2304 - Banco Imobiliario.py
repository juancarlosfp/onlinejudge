#receber variaveis ValorInicial e qndJogadas

n = input().split()
n[0],n[1] = int(n[0]),int(n[1])

#adicionar ValorInicial para cada jogador

D, E, F = n[0],n[0],n[0]

#repetir o numero de jogadas que cada jogador 

for i in range(n[1]):
  dados = input().split() #pegar valor de cada linha, testar de é jogada de C/V ou de A 
  #testar se é jogada de C/V ou de A
  
  
  
  #teste para C/V 
  

  
  if(len(dados)==3):
    valorJogada = int(dados[2])
    if(dados[0] == 'C'):
      if(dados[1]=='D'):
        D -= valorJogada
      elif dados[1]=='E':
        E -= valorJogada
      else:
        F -= valorJogada
    if(dados[0] == 'V'):
      if(dados[1]=='D'):
        D += valorJogada
      elif dados[1]=='E':
        E += valorJogada
      else:
        F += valorJogada
  else:
    #teste para A 
    
    valorJogada = int(dados[3])
    
    if(dados[0] == 'A'):
      if(dados[1]=='D'):
        if(dados[2] == 'E'):
          
          E -= valorJogada

        else:
          
          F -= valorJogada
          
        D += valorJogada
        
      elif(dados[1]=='E'):
        if(dados[2] == 'D'):
          
          D -= valorJogada

        else:
          
          F -= valorJogada
          
        E += valorJogada
        
      elif(dados[1]=='F'):
        if(dados[2] == 'D'):
          
          D -= valorJogada

        else:
          
          E -= valorJogada
          
        F += valorJogada
        
print(D,E,F)