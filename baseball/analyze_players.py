'''
1) read the CSV using the CSV standard library module
2) compute the quantiles (25th, 50th, and 75th) percentile for player height (and print that out) statistics module '''
import csv
import statistics
import math

# iterable list with single-character strings as items
def find_height(my_list):
	first_number = -1
	for word in my_list:
		for char in word:
			if char <= "9" and char >= "0" and len(char) == 1:
				if first_number == -1:
					first_number = ord(char) - 48
				else:
					return first_number * 10 + ord(char) - 48
	return -1
l = []
with open('mlb_players.csv', newline = '') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
	for row in spamreader:
		height = find_height(row)
		if height != -1:
			l.append(height)
l = sorted(l)
quartile1 = str(statistics.median(l[0:math.ceil((len(l)-1)/2)]))
median = str(statistics.median(l))
quartile2 = str(statistics.median(l[math.ceil(len(l)/2):]))
print("25th percentile: " + quartile1 + " inches.\n50th percentile: " + median + " inches.\n75th percentile: " + quartile2 + " inches.")