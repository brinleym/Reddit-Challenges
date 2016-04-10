from sys import argv


print len(argv)

guesses = []

script, inputfile = argv

with open(inputfile, "r") as f:
	hats = f.read().splitlines()

print hats
print len(hats)

# black == odd number of blacks
# white == even number of blacks
# loop through hats,
# if first person sees even number of black hats before him, say white
# if first person sees odd number of black hats before him, say black

# for each person after first, if number of black hats (even or odd) is
# different than previous guess, say black, else, say white

def countEvenBlacks(pos):

	#print ""
	#print "Counting blacks ahead..."

	num_blacks = 0

	for i in range(pos + 1, len(hats)):
		if hats[i] == 'Black':
			num_blacks += 1;

	#print("Number of blacks: " + str(num_blacks))


	# if blacks ahead is even
	if num_blacks % 2 == 0:
		#print "Even number of blacks!"
		return True;

	#print "Odd number of blacks!"
	return False;

def guess():

	# first guess
	if(countEvenBlacks(0)):
		guesses.append(True)
		print "Guess: White"
	else:
		guesses.append(False)
		print "Guess: Black"

	for i in range(1, len(hats)):

		prev_guess = guesses[i - 1]
		even_blacks_ahead = countEvenBlacks(i)

		if(even_blacks_ahead == prev_guess):
			guesses.append(even_blacks_ahead)
			print "Guess: White"
		else:
			guesses.append(even_blacks_ahead)
			print "Guess: Black"

		print ""

guess()
