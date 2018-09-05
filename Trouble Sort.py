def tripple_sort(list_data):
	global L_data, let_done
	chk = 0
	for i in range(L_data-2):
		#print(i)
		one = list_data[i]
		
		three = list_data [i+2]
		#print(one,three)
		if one > three:
			list_data[i] = three
			list_data[i+2] = one
			chk = 1

	if chk == 0:
		let_done = True

	return (list_data)

def tripple_sort_chek(list_data):
	global L_data
	chk = 0
	error = -1
	for i in range(L_data-1):
		#print(i)
		one = list_data[i]
		two = list_data [i+1]
		#print(one,three)
		if one > two:
			chk = 1
			error = i 
			break
	if chk == 1:
		return error
	else:
		return "OK"


if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		let_done = False
		L_data = int(input())
		list_data = [int(j) for j in input().split()]

		while let_done == False:
			list_data = tripple_sort(list_data)
		ans = tripple_sort_chek(list_data)
		print("Case #" + str(i+1)+": "+str(ans))
		
