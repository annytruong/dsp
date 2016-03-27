import csv

reader = csv.reader(open('faculty.csv'))

result = {}
for row in reader:
	key = row[0]
	if key in result:
		pass
	result[key] = row[1:]
#print result

#q6
faculty_dict = result.copy()
for key in faculty_dict.keys():
	faculty_dict[key.split()[-1]] = faculty_dict[key]
	del faculty_dict[key]
print faculty_dict

#q7
professor_dict = result.copy()
for key in professor_dict.keys():
	professor_dict[tuple(key.split(' '))] = professor_dict[key]
	del professor_dict[key]
print professor_dict

#q8
sorted_list = sorted(professor_dict, key=lambda x: x[-1]) 
#print sorted_list

# to print all of dictionary in order
for key in sorted_list:
	print key,":", professor_dict[key] #sorted but not as a dictionary

# to print first 3
print sorted_list[0],":",professor_dict[sorted_list[0]]
print sorted_list[1],":",professor_dict[sorted_list[1]]
print sorted_list[2],":",professor_dict[sorted_list[2]]"""
