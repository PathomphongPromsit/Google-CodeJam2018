
def try_delete(summ):
	global list_wut
	global ans
	global SUM
	#print("LW",list_wut)

	copy_list = list_wut[:]
	copy_list_two = list_wut[:]
	copy_list_three = list_wut[:]

	max_value = max(copy_list)
	max_index = copy_list.index(max_value) 

	copy_list[max_index] = copy_list[max_index]-1
	

	max_value_two = max(copy_list)
	max_index_two = copy_list.index(max_value_two) 

	#print("CPL1",copy_list,max_index,max_index_two)
	
	copy_list_two[max_index] = copy_list_two[max_index]-1
	copy_list_two[max_index_two] = copy_list_two[max_index_two]-1

	#print("CPL2",copy_list_two)

	copy_list_three[max_index] = copy_list_three[max_index]-1
	#print("CPL%3",copy_list_three)

	if max(copy_list_two) <= ((summ-2)/2):
		list_wut = copy_list_two
		first = chr(65+max_index)
		secound = chr(65+max_index_two)
		block = " "
		block = " "
		block = block+first+secound
		#print(block)
		SUM = summ-2

		return block

	elif max(copy_list_three) <= ((summ-1)/2):
		list_wut = copy_list_three
		block = " "
		block = block+chr(65+max_index)
		#print(block)
		SUM = summ-1

		return block



if __name__ == "__main__":

	T = int(input())
	for i in range(T):
		ans =""
		pack = int(input())
		list_wut = []
		SUM = 0
		
		list_wut =[int(k) for k in input().split()]
		
		for l in range(pack):
			value = list_wut[l]
			SUM += value
			#print(chr(65+l))
		dell= -1
		while dell!= 0:
			RE = try_delete(SUM)
			ans=ans+RE
			dell = SUM


		print("Case #" + str(i+1)+":"+str(ans))

		#print 'Value is "' + str(value) + '"'

	

