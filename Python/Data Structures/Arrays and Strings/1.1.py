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