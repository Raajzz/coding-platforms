# METHOD 1 | top down dp

dp_look_up = {}

def getNthFib(n):
	try:
		if((dp_look_up[n] == 0) or (dp_look_up[n])):
			return dp_look_up[n]
	except:		
		if((n == 1) or (n == 2)):
			dp_look_up[n] = n-1
		else:
			dp_look_up[n] = getNthFib(n-1) + getNthFib(n-2)
		return dp_look_up[n]

print(getNthFib(1))

# METHOD 2 | bottom up dp