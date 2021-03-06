## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> 7
>> Counter({'PhD': 28, 'ScD': 5, 'MD': 1, 'degree': 1, 'BSEd': 1, '0': 1, 'JD': 1})


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> 5
>> Counter({'Professor of Biostatistics': 13, 'Associate Professor of Biostatistics': 12, 'Assistant Professor of Biostatistics': 11, 'Assistant Professor is Biostatistics': 1, 'title': 1})


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> set(['rhubb@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'nanditam@mail.med.upenn.edu', 'warren@upenn.edu', 'whwang@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'michross@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'bryanma@upenn.edu', 'wguo@mail.med.upenn.edu', 'bellamys@mail.med.upenn.edu', 'jaroy@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'mjoffe@mail.med.upenn.edu', 'weiyang@mail.med.upenn.edu', 'dxie@upenn.edu', 'mingyao@mail.med.upenn.edu', 'jellenbe@mail.med.upenn.edu', 'rshi@mail.med.upenn.edu', 'liy3@email.chop.edu', 'sellenbe@upenn.edu', 'rlocalio@upenn.edu', 'hsu9@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rxiao@mail.med.upenn.edu', 'email', 'sratclif@upenn.edu', 'jshults@mail.med.upenn.edu', 'shawp@upenn.edu', 'jinboche@upenn.edu', 'pgimotty@upenn.edu', 'sxie@mail.med.upenn.edu'])


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> 4
>> set(['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu'])

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> 'Landis': ['B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu'], 'Feng': ['Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], 'Sammel': ['Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu']

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>> ('Jonas', 'H.', 'Ellenberg'): ['Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], ('Hongzhe', 'Li'): ['Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu']

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

>> ('Scarlett', 'L.', 'Bellamy') : ['Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu'], ('Warren', 'B.', 'Bilker') : ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'], ('Matthew', 'W', 'Bryan') : ['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']


Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

