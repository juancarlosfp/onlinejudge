n = int(input())
M = 0
H = [[0]]*n

maiorIda = [[x+1,0] for x in range(n)]
maiorVolta = [[x+1,0] for x in range(n)]


for i in range(n):
  dados = input().split()
  M = int(dados[0])
  H[i] = [int(x) for x in dados[1:]]

  for j in range(M-1):
    if H[i][j] < H[i][j+1]:

      maiorIda[i][1] += H[i][j+1] - H[i][j]

    else:

      maiorVolta[i][1] += H[i][j] - H[i][j+1]

for i in range(n):
  for j in range(i,n):
    if maiorIda[i][1] > maiorIda[j][1]:
      
      maiorIda[i],maiorIda[j] = maiorIda[j], maiorIda[i]
    elif maiorIda[i][1] == maiorIda[j][1]:
      if maiorIda[i][0] > maiorIda[j][0]:

        maiorIda[i][0],maiorIda[j][0] = maiorIda[j][0],maiorIda[i][0]

    if maiorVolta[i][1] > maiorVolta[j][1]:
      
      maiorVolta[i],maiorVolta[j] = maiorVolta[j], maiorVolta[i]
    elif maiorVolta[i][1] == maiorVolta[j][1]:
      if maiorVolta[i][0] > maiorVolta[j][0]:

        maiorVolta[i],maiorVolta[j] = maiorVolta[j],maiorVolta[i]


if maiorIda[0][1]<maiorVolta[0][1]:

  print(maiorIda[0][0])

elif maiorIda[0][1]>maiorVolta[0][1]:

  print(maiorVolta[0][0])

else:
  if maiorVolta[0][0] < maiorIda[0][0]:
    print(maiorVolta[0][0])
  else:
    print(maiorIda[0][0])