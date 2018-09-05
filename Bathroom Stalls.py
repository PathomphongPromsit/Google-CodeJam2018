def calche(N,K,i):
	list_block = []
	
	list_block.append(N)
	while K != 0:
		wide = max(list_block)
		index_wide = list_block.index(wide) 
		del list_block[index_wide]
		mid = int(wide/2)
		left = wide-(mid+1)
		right = wide-(left+1)
		list_block.append(left)
		list_block.append(right)


		if K == 1: #konsudtai
			print("Case #" + str(i+1)+":",right,left)
			#print(right,left)

		K -=1





if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		N,K = [int(j) for j in input().split()]
		calche(N,K,i)