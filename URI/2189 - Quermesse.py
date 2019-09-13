n = int(input())

count = 1
while(n != 0):
    lista = [int(x) for x in input().split()]
    vencedor = None
    for i in range(len(lista)):
        if(lista[i] == i+1 ):
            vencedor = i+1
            break

    print("Teste %d"%count)
    print(vencedor)
    print()
    count += 1
    n = int(input())
    