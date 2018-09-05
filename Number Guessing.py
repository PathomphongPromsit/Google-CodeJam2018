testcase = int(input())
i = 0
while i  != testcase:
	a, b = [int(k) for k in input().split()]
	N = int(input())
	
	n = 0
	
	recive = "GGWP"
	
	start = a+1 #upper 
	stop  = b

	while (recive != "CORRECT") and recive != "WRONG_ANSWER" and n !=N:
		
		mid = int((start+stop)/2)
		print(mid)

		recive = str(input())
		if recive == "TOO_SMALL":
			start = mid+1
		elif recive == "TOO_BIG":
			stop = mid-1

			
		
		n+=1
	i+= 1
