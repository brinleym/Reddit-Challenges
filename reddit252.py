from sys import argv

def find_leftmost_pair(s):

	char_arr = list(s)

	print_arr(char_arr)

	temp_arr = []

	myPair = Pair(char_arr[0], 0, 0) # instantiate Pair() with first char

	temp_arr.append(char_arr[0]) # push first char to temp arr

	print_arr(temp_arr)

	for i in range(1, len(char_arr)):

		curr_char = char_arr[i] # store char at pos i
		print "Current char: " + curr_char

		print "Temp arr: "
		print_arr(temp_arr)

		# if current char is in temp_arr, duplicate found!
		if curr_char in temp_arr:

			# if diff btwn curr_char and its duplicate exceeds that of the 
			# current result held in myPair
			if i - char_arr.index(curr_char) > myPair.diff:

				# update myPair
				# myPair.char = curr_char
				# myPair.first_index = pos of curr_char's duplicate
				# myPair.second_index = pos of curr_char
				myPair = Pair(curr_char, char_arr.index(curr_char), i)

				# remove all items from temp_arr up to first's pos
				temp_arr[0:temp_arr.index(curr_char)] = []

			# if diff btwn curr_char and its duplicate does not exceed that of the 
			# current result held in myPair
			else:
				# find index of second in myPair
				second_temp_index = temp_arr[1:].index(myPair.char)

				# remove all items from temp_arr after second's pos
				temp_arr[second_temp_index + 2:] = []

		# append curr_char to temp_arr
		temp_arr.append(curr_char)
		print "New temp arr: "
		print_arr(temp_arr)

	return myPair

def print_arr(arr):

	for item in arr:
		print item

def update_string(s, pair):

	s = s[:pair.first_index] + s[pair.first_index + 1:] # remove first in pair
	s = s[:pair.second_index - 1] + s[pair.second_index:] # remove second in pair

	s += pair.char # append second in pair to end

	print s

	return s

def decode(s):

	pair = find_leftmost_pair(s)

	while pair.second_index is not 0:
		s = update_string(s, pair)
		pair = find_leftmost_pair(s)

class Pair:

	def __init__(self, char, first, second):
		self.char = char
		self.first_index = first
		self.second_index = second
		self.diff = self.second_index - self.first_index

script, s = argv

decode(s)


