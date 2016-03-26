import csv

f = open('faculty.csv') #read in csv file

csv_f = csv.reader(f) #read csv file

name = []
degree = []
title = []
email = []
for row in csv_f:
	name.append(row[0])
	degree.append(row[1])
	title.append(row[2])
	email.append(row[3])

#q1
#replace the . to make the list more uniform
degree = ([i.replace('.', '') for i in degree])
#some people have multiple degrees
degree = ([i.split(" ")[0] for i in degree])
#print the length of the set (which removes duplicates)
#to find the different degrees
print len(set(degree))
#find the number of occurence per degree
from collections import Counter
print Counter(degree)

#q2
print len(set(title))
print Counter(title)

#q3
print set(email)

#q4
import re
#find domain in email
domain = []
for str in email:
	match = re.search('([\w.-]+)@([\w.-]+)', str)
	if match:
		domain.append(match.group(2)) #group 2 is the host
print set(domain)
print len(set(domain))

f.close()
