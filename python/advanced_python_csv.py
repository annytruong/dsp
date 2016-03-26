# part 2
import csv

email = []
with open('faculty.csv','rb') as f:
	reader = csv.reader(f)
	for row in reader:
		email.append(row[3])
f.close()

with open('emails.csv', 'wb') as a:
	writer = csv.writer(a)
	for row in email:
		writer.writerow([row])
a.close()
