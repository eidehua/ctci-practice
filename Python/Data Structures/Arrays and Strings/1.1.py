#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# assumption: assume uppercase and lowercase are different characters
def has_unique_chars(string):
	counts = {} # dictionary to see if we have seen the character already
	for i in range(0, len(string)):
		char = string[i]
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

