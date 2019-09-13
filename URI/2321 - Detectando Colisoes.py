ret1 = input().strip()
ret1 = ret1.split()
ret1 = [int(x) for x in ret1]
ret2 = input().strip()
ret2 = ret2.split()

ret2 = [int(x) for x in ret2]
x0,y0,x1,y1 = [],[],[],[]
x0.extend([ret1[0],ret2[0]])
y0.extend([ret1[1],ret2[1]])
x1.extend([ret1[2],ret2[2]])
y1.extend([ret1[3],ret2[3]])

if (x1[0] < x0[1]) or (x1[1]<x0[0]) or (y1[0] < y0[1]) or (y1[1] < y0[0]):
	print(0)
else:
	print(1)
