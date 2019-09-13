t = 0
x = int(input())

while (x != 0):
    t += 1
    print("Teste", t)

    nome_par = input()
    nome_impar = input()

    for i in range(x):
        a, b = map(int, input().split())
        if (a + b) % 2 == 0:
            print(nome_par)
        else:
            print(nome_impar)
    print()
    x = int(input())
    