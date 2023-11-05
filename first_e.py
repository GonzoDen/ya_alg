n = int(input()) 

arr = []

for i in range (0, n):
	a = int(input())
	arr.append(a)

print(arr)

phase = 1 #TODO
count = [0] * 10

#TODO: when ints, the digits for odnoznchnye are lost

for i in range(0, len(arr)):
	remainder = arr[i] % 10 ** phase
	if remainder == 0:
		count[remainder] += 1
	elif remainder == 1:
		count[remainder] += 1
	elif remainder == 2:
		count[remainder] += 1
	elif remainder == 3:
		count[remainder] += 1
	elif remainder == 4:
		count[remainder] += 1
	elif remainder == 5:
		count[remainder] += 1
	elif remainder == 6:
		count[remainder] += 1
	elif remainder == 7:
		count[remainder] += 1
	elif remainder == 8:
		count[remainder] += 1
	else:
		count[remainder] += 1

print(count)

pos = [0] * 10
for i in range (1, 10):
	pos[i] = count[i-1] + pos[i-1]

print(pos)

f = []


for i in range(0, len(arr)):
	remainder = arr[i] % 10 ** phase #TODO repetition

	if remainder == 0:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1
	elif remainder == 1:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1
	elif remainder == 2:		
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1
	elif remainder == 3:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	elif remainder == 4:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	elif remainder == 5:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	elif remainder == 6:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	elif remainder == 7:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	elif remainder == 8:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1

	else:
		f.insert(pos[remainder], arr[i])
		pos[remainder] += 1


print(f)


