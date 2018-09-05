def cal_damage(program):
	damage = 0
	strength = 1
	#print("CD",program)
	for i in program:
		if i == "S":
			damage += strength
		elif i == "C":
			#print("GG")
			strength = strength*2
	#print(damage)
	return (damage)

def swap(program):
	global index_S, LP, fix
	for i in range(LP-1):
		if program[i] == "C" and program[i+1] == "S":
			program[i] = "S"
			program[i+1] = "C"
			break
	

	return(program)
if __name__ == "__main__":
	T = int(input())
	
	for i in range(T):
		shield, program = [i for i in input().split()]
		shield = int(shield)
		program = list(program)
		count_S = 0
		fix = 0
		for j in program:
			if j == "S":
				count_S +=1
		
		if count_S > shield:
			print("Case #" + str(i+1)+": IMPOSSIBLE")
		
		else:
			LP =len(program)
			count_swap = 0
			damage = cal_damage(program)
			#print("DM",damage)
			index_S =0
			while damage > shield:
				program = swap(program)
			#print("PG",program)
				damage = cal_damage(program)
				#print("DM",damage)
				count_swap += 1
			print("Case #" + str(i+1)+": "+str(count_swap))
			