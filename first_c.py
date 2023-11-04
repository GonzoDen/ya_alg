n = int(input()) 
a = [int(x) for x in input().split()]
m = int(input()) 
b = [int(x) for x in input().split()]

a_l = 0
b_l = 0
a_r = len(a)-1
b_r = len(b)-1

f = []

while (b_l <= b_r):
	if a[a_l] <= b[b_l]:
		f.append(a[a_l])
		a_l += 1
	else:
		f.append(b[b_l])
		b_l += 1

while (a_l <= a_r):
	f.append(a[a_l])
	a_l += 1

print(f)


