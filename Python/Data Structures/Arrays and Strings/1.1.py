#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# assumption: assume uppercase and lowercase are different characters
def has_unique_chars(str):
	counts = {} # dictionary to see if we have seen the character already
	for i in range(0, len(str)):
		char = str[i]
		if char in counts:
			return False
		counts[char] = True
	return True
		
	
print has_unique_chars("HIiiH")
assert has_unique_chars("HIiiH") == False
print has_unique_chars("HiI")
assert has_unique_chars("HiI") == True

'''
Input is a string of length n
Time Complexity: O(n), since in the worst case we need to look at the entire string 
Space Complexity: O(n), to store all the unqiue chars in our counts dictionary
'''

#Improved solution (from book): there are only a finite amount of different characters that exist. 
#So while the string may be arbitrarily large, we only need a O(1) extra space to check if characters are duplicated

#Assume 256 possible unique characters (ASCII)
#function ord() would get the int value of the char. 
#And in case you want to convert back after playing with the number, function chr() does the trick.	
def has_unique_chars_2(str):
	if len(str) > 256:
		return False
	char_set = [False for i in range(256)] # list comprehension, for creating a boolean array all initialized to false
	for i in range(0, len(str)):
		char_val = ord(str[i])
		if(char_set[char_val]):
			return False
		char_set[char_val] = True
	return True

print("=====")	
print has_unique_chars_2("HIiiH")
assert has_unique_chars_2("HIiiH") == False
print has_unique_chars_2("HiI")
assert has_unique_chars_2("HiI") == True
	


#What if you cannot use additional data structures?

#Have to compare each char with every other char.

def has_unique_chars_extra(str):
	for i in range(0, len(str)):
		curr_char = str[i]
		for j in range(i+1, len(str)):
			compare_char = str[j]
			if(curr_char == compare_char):
				return False
	return True
	
print("=====")	
print has_unique_chars_extra("HIiiH")
assert has_unique_chars_extra("HIiiH") == False
print has_unique_chars_extra("HiI")
assert has_unique_chars_extra("HiI") == True

'''
Input is a string of length n
Time Complexity: O(n**2), since we need to compare every character with every other character
Slightly less than n**2 iterations, however. (Because we only have to check each pair once)
Space Complexity: O(1). Did not use any extra space
'''