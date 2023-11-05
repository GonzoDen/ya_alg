def merge_sort (arr):
	f = [] * len(arr)

	def recursive_sort (a_s, a_e):
		if a_e <= a_s: return

		mid = (a_s + a_e) // 2
		recursive_sort(a_s, mid)
		recursive_sort(mid+1, a_e)
		merge(a_s, mid, a_e)

	def merge(a_s, mid, a_e):

	#lo = a_l = left
	#mid = a_r 
	#mid+1=b_l
	#hi = b_r

		f[a_s:a_e+1] = arr[a_s:a_e+1]

		a_l = a_s
		b_l = mid+1

		for i in range (a_s, a_e+1):
			if a_l > mid:
				arr[i] = f[b_l]
				b_l += 1
			elif b_l > a_e:
				arr[i] = f[a_l]
				a_l += 1
			elif f[a_l] > f[b_l]:
				arr[i] = f[b_l]
				b_l += 1
			else:
				arr[i] = f[a_l]
				a_l += 1
	
	recursive_sort(0, len(arr)-1)

n = int(input()) 
arr = [int(x) for x in input().split()]
merge_sort(arr)
result = " ".join(map(str, arr))
print(result)