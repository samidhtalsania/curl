# global counter 
# counter = 0
global chars 
chars = list()
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cropurl(count):
	str = getString(count)
	# global counter
	str = "www.cropurl.com/"+str
	return str
	# counter += 1
	


def getString(count):
	str = ""
	if count<62:
		return chars[count]
	else:
		while(1):
			x = count // 62 #0
			y = count % 62 #1
			str += chars[y]#01
			count = x #0
			if x<62:
				str += chars[x]
				break
			
		return str[::-1]