import math

def multi(A):
	global a, b
	gg = int(math.sqrt(A))
	#print(gg)
	while A % gg != 0:
		gg -= 1
	a = gg
	b = int(A/gg)

def check(I, J):
	#print("IJ",I,J)
	global I_st, J_st, chk_matrix
	#print("ST",I_st,J_st)
	chk_matrix[I-I_st][J-J_st] = 1

def next(m,n):
	global a,b,m_current,n_current
	
	if (n+1) <= (b-2):
		n +=1
	elif (n+1) > (b-2):
		n = 1
		if (m+1) <= (a-2):
			m +=1
		elif (m+1) > (a-2):
			m = 1
	m_current = m
	n_current = n
if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		a = 0
		b = 0
		A = int(input())
		multi(A)
		#print("AB",a,b)
		#print(2,2) #sent st nd
		
		I_re = -2
		J_re = -2
		
		chk = 0

		chk_matrix = [[0 for i in range(b)]for j in range(a)]
		#print(chk_matrix)

		chk_st = 0
		chk_J_st = 0

		I_st = 0
		J_st = 0

		m_current = 1
		n_current = 1
		
		q = int(2)
		p = int(2)
		print(q,p)
		
		while chk == 0:
			I_re, J_re = [int(i) for i in input().split()]
				
			if (I_re == 0 and J_re == 0) or (I_re == -1 and J_re == -1):
				chk = 1
				break
			else:

				#CHK POINT KUD
				if chk_st ==0:
					#print("GGWP")
					I_st = I_re
					J_st = J_re
					chk_st =1
					chk_matrix[0][0]=1
				elif chk_st == 1:
					#print("GG")
					check(I_re, J_re)
				#print("CHKMT",chk_matrix)
				
				sent = 0
				while sent == 0:
					#print("MNCR",m_current,n_current)

					#eight
					lo = chk_matrix[m_current-1][n_current-1]
					mo = chk_matrix[m_current-1][n_current]
					ro = chk_matrix[m_current-1][n_current+1]
					l = chk_matrix[m_current][n_current-1]
					r = chk_matrix[m_current][n_current+1]
					# lu = chk_matrix[m_current+1][n_current-1]
					# mu = chk_matrix[m_current+1][n_current]
					# ru = chk_matrix[m_current+1][n_current+1]

					if chk_matrix[m_current][n_current] == 0 or(lo == 0 or mo == 0 or ro == 0 or l == 0 or r == 0):# or lu == 0 or mu == 0 or ru == 0):

						print(int(m_current+I_st),int(n_current+J_st))
						sent = 1
					else:
						next(m_current,n_current)





				

				#print(chk_matrix)
				#print(I_st,J_st)