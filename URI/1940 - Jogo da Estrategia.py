J, R = map(int, input().split())
jogador = input().split()

i = 0
vez = 0
pontos = [0 for k in range(J)]


for x in jogador:
    pontos[vez] += int(x)
    vez += 1
    vez %= J

#while (i < len(jogador)):
    #pontos[vez] += int(jogador[i])
    #i += 1
    #vez += 1
    #vez = vez%J

indMax = -1
max = -1
# print(pontos)
for i in range(len(pontos)):
    if(pontos[i] >= max):
        indMax = i
        max = pontos[i]


print(indMax + 1)