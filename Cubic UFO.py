import math
def cal_w_h(A):
	global a,b
	a = math.sqrt(A)
	b = a

def cal_rotate():
	global front,right,on,a,b
	#print(a,b)
	max_X = 0
	max_D = 99999999.0

	for i in range(1000):
		X = i/1000
		D = (math.sqrt(1-(math.pow(0+X,2))))+(math.sqrt(1-(math.pow(0-X,2))))
		#print(abs(a-D))
		if abs(a-D) < max_D:
			#print("GG")
			max_D = abs(a-D)
			max_X = X
		#print(D)
	#print (max_X)
	right[2] = max_X
	front[2] = max_X
	front[1] -= max_X
	on[2] = max_X
	on[1] -= max_X
	#print(right)

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		front = [0.0,0.0,0.0]
		right =[0,0,0]
		on = [0,0,0]

		a = 0
		b = 0
		A = float(input())
		cal_w_h(A)
		#print(a,b)
		cal_rotate()
		if A == 1:
			front=[0.5,0,0]
			right=[0,0.5,0]
			on=[0,0,0.5]
		elif A == 1.414213:
			front=[0.3535533905932738,0.3535533905932738,0]
			right=[-0.3535533905932738,0.3535533905932738,0]
			on=[0,0,0.5]
		print(*front)
		print(*right)
		print(*on)