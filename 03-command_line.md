# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

•	pwd – print working directory;

•	hostname – computer’s name;

•	mkdir – make a directory;

•	cd – change directory;

•	cd .. – move up one directory;

•	ls – list directory;

•	rmdir – remove directory;

•	pushd – takes current directory and pushes it into a list for later, then it changes into another directory. “Save where I am, then go here.”;

•	popd – takes the last directory you pushed and pops it off, taking you back there;

•	touch – create empty file;

•	new-item – create empty file (on Windows);

•	cp – copy a file;

•	mv – rename a file;

•	less – view a file;

•	more – view a file (Windows);

•	cat – stream a file;

•	rm – remove a file;

•	a | b – takes the output from command a and “pipes” it to command b;

•	a < b – takes and sends the input from the file on the right (b) to the program on the left (a);

•	a > b – takes the output of command a then writes it to file b;

•	a >> b – takes the output of the command a then appends it to file b;

•	* – wildcard matching

•	find . -name “*.txt” -print – find files in current directory with name *.txt and print

•	cat > somefile.txt – cat will read what you type and write into somefile.txt, ctrl-d to exit

•	grep – look inside files

•	man – command help

•	help – command help (Windows)

•	apropos – for when you forget the name of a command but you know what it does, looks through help files

•	env – print out the environment

o	env | grep anny – print out the environment but pipes through grep to find variables with anny

•	echo – show environment variable

•	export – set an environment variable

•	unset – unset an environment variable

•	exit – exit terminal

•	xargs – construct argument lists and execute utility

•	sudo – execute a command as another user

•	chmod – change file modes or Access Control Lists

•	chown – change file owner and group



---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
`ls` - list directory. 

`ls -a` - list all files and folders

`ls -l` - list in long format

`ls -lh` - list using unit suffixes (byte, kilobyte)

`ls -lah` - list using unit suffixes and include directory entries whose name begin with a dot

`ls -t` - list directory, sort by time modified 

`ls -Glp` - list directory, enable colorized output, long format, write / after names of directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
'ls -c' - display files by timestamp

'ls -m' - display the names as comma-separated list

'ls -q' - display nonprinting characters as ?

'ls -r' - display in reverse order

'ls -R' - display subdirectories



---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is used to divide a big list of arguments into small list received from standard input when used with find and grep.

Example: find . -name "*.tmp" | xargs grep "Anny". 
This will find all the .tmp files from the current directory and then look for the word "Anny" in each tmp file.
 

