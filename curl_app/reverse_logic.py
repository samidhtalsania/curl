global chars 
chars = list()
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
powers_62 = list()
powers_62 = [1,3844,239328,14776336,916132832,56800235584]
# convert from base 62 to base 10 id

def cropurl(curl_string):
	str = getString(curl_string)
	return str

def getString(curl_string):
	length = len(curl_string)-1
	tempSum = 0
	for char in curl_string:
		tempIndex = chars.index(char) #returns the index of th character from chars array
		tempVal = tempIndex*powers_62[length]
		length -= 1
		tempSum += tempVal
	return tempSum
