#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
	with open(data, 'r') as a:
		football = [row for row in csv.reader(a.read().splitlines())]
	return football
   # COMPLETE THIS FUNCTION

def get_min_score_difference(football):
	football.pop(0)
	goals = [row[5] for row in football]
	goals_allowed = [row[6] for row in football]
	values = [abs(float(x) - float(y)) for x, y in zip(goals, goals_allowed)]
	return values.index(min(values))
	# COMPLETE THIS FUNCTION

def get_team(index_value, football):
	teams = [row[0] for row in football]
	return teams[index_value]
    # COMPLETE THIS FUNCTION

data = read_data("football.csv")
min_score = get_min_score_difference(data)
team = get_team(min_score, data)

print data
print min_score
print team
