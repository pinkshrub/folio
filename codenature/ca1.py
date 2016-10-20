gen0 = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

def generate(array, generations, rule):



	def makeruleset(rule):
		binary_rule = format(rule,"08b")
		return [i for i in binary_rule]



	ruleset = makeruleset(rule)

	def rules(left, mid, right):
		if (left == 1 and mid == 1 and right == 1):
			return int(ruleset[0])
		elif (left == 1 and mid == 1 and right == 0):
			return int(ruleset[1])
		elif (left == 1 and mid == 0 and right == 1):
			return int(ruleset[2])
		elif (left == 1 and mid == 0 and right == 0):
			return int(ruleset[3])
		elif (left == 0 and mid == 1 and right == 1):
			return int(ruleset[4])
		elif (left == 0 and mid == 1 and right == 0):
			return int(ruleset[5])
		elif (left == 0 and mid == 0 and right == 1):
			return int(ruleset[6])
		elif (left == 0 and mid == 0 and right == 0):
			return int(ruleset[7])
		else:
			return 0;



	prev = array
	for g in range(0, generations):
		print array, g, prev, gen0
		prev = array
		for i in range(1,len(array)-1):
			left = prev[i-1]
			mid  = prev[i]
			right= prev[i+1]
			newstate = rules(left, mid, right)
			array[i] = newstate



# for i in range(0,4):
# 	print 'this is rule' + str(i)
# 	generate(gen0,5,i)

print "ruleset the next"
print gen0
generate(gen0,10,1)
print "ruleset the next"
print gen0
generate(gen0,10,2)
print "ruleset the next"
print gen0
generate(gen0,10,3)