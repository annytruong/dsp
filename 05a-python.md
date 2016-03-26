# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both made up of elements which include: string, integers, and other lists and tuples. Lists are mutable whereas tuples are immutable. Lists are homogenous sequences, while tuples are heterogeneous data structures. Tuples can be used as keys in dictionaries, whereas lists can be used as values. Dictionaries are indexed by keys, which can be any immutable type. As long as a tuple only contain numbers, strings, and other tuples, it can be used as a key. Lists cannot be used as keys since they can be modified.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are similar to lists in that both data types contain values without keys (unlike dictionaries). Both also support comprehensions (i.e. for x in list, for x in set). However, sets are unordered, thus cannot be indexed or sliced. Sets cannot have duplicates and the items must be hashable.  
  
>> Example:  
list_of_fruits = [apple, apple, banana, orange, kiwi, orange, orange]  
set(list_of_fruits) = [apple, banana, orange, kiwi]  
  
>> In terms of finding an element, sets perform much faster than lists. The time it takes to find an element in a list is proportional to the length of the list. Since sets are unordered and unduplicated, each element can be found using hash, it’s significantly faster than having to go through each index to find the element in list.  


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda function is a tool for building functions or function objects, similar to the def function. Lambda is anonymous (doesn’t require a name like in def), and is typically generated for a function that is only going to be used once. Lambda functions can only take a single expression (must return a value).  

>> Example:  
sorted_list = sorted(list, key=lambda x: x[-1])  


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is an efficient way to create new lists, usually when an operation is applied to elements of the original list. Map/filter is faster than list comprehension when lambda is not involved, but vice versa when lambda is involved. 

>> Example:  
squares = []  
for x in range(10):  
    squares.append(x**2)  

>> List comprehension:  
squares = [x**2 for x in range(10)]  

>> Map:  
squares = map(lambda x: x**2, range(10)]  

>> Filter:  
squares = filter(lambda x: x**2, range(10])  

>> Set comprehension:  
set(squares) = []  
squares = {x**2 for x in range[10]}  

>> Dictionary comprehension:  
squares = {}  
squares = {x: x**2 for x in range[10]}  


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





