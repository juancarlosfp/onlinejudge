lis = input().split()

x = lis[0]
y = lis[1]

while(int(x) != 0 and int(y) != 0):
    nova_lis = ""
    for valor in y:
        if(valor != x):
            nova_lis += valor

    if(nova_lis == ""):
        nova_lis += "0"
    print(int(nova_lis))
    lis = input().split()
    x = lis[0]
    y = lis[1]