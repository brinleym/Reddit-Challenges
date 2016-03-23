import csv

class Presidents:

	def __init__(self):
		self.birth_years = []
		self.death_years = []

class Results:

	def __init__(self):
		self.years = []
		self.num_alive = []
		self.max_alive = 0
		self.max_year = 0

	def set_years(self, start, end):

		for i in range(int(start), end + 1):
			self.years.append(i)
			self.num_alive.append(0)

def findMostYearWhenMostAlive(start, end, presidents):

	myResults = Results()
	myResults.set_years(start, end)

	# loop through list of years
	for i in range(len(myResults.years)):
		year = myResults.years[i]
		for index in range(len(presidents.birth_years)):

			# corner case: if president is still alive
			if presidents.death_years[index] == "":
				if(int(year) >= int(presidents.birth_years[index])):
					# increment num alive during that year
					myResults.num_alive[i] += 1  
			else:
				if(int(year) >= int(presidents.birth_years[index]) and int(year)
					<= int(presidents.death_years[index])):

					# increment num alive during that year
					myResults.num_alive[i] = myResults.num_alive[i] + 1 

	analyzeResults(myResults)
	reportResults(myResults)

def analyzeResults(results):

	for i in range(len(results.years)):
		if results.num_alive[i] > results.max_alive:
			results.max_alive = results.num_alive[i]
			results.max_year = results.years[i]


def reportResults(results):

	for i in range(len(results.years)):
		year = results.years[i]
		num_alive_in_year = results.num_alive[i]
		print str(year) + ": " + str(num_alive_in_year) + " presidents alive."

	print "Winning year is " + str(results.max_year) + ": " + str(results.max_alive)
				

with open("input.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	#for row in reader:
			#print(row['PRESIDENT'], row[' BIRTH DATE'], row['BIRTH PLACE'], 
				#row['DEATH DATE'], row['LOCATION OF DEATH'])


	myPresidents = Presidents()

	# get starting point --> first president's birth year
	first_president = reader.next()
	gw_birth_year = first_president[" BIRTH DATE"].split(" ")[2]
	myPresidents.birth_years.append(gw_birth_year)
	gw_death_year = first_president["DEATH DATE"].split(" ")[2]
	myPresidents.death_years.append(gw_death_year)

	for row in reader:
		myPresidents.birth_years.append(row[" BIRTH DATE"].split(" ")[2])
		if row["DEATH DATE"] != " ":
			myPresidents.death_years.append(row["DEATH DATE"].split(" ")[2])
		else:
			myPresidents.death_years.append("")

	findMostYearWhenMostAlive(gw_birth_year, 2016, myPresidents)




