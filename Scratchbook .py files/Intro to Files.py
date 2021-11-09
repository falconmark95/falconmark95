# ~Introduction to file I/O~
# In order for the file to be able to be detected at this level you need to have it in the same
# folder as your current working program

myfile = open('Example Text File') # Opening a file
print(myfile.read())
# Calling the function again will start the scan at the end where it has already finished from first time
print(myfile.read()) # Statement will print nothing
myfile.seek(0) # Restarts the 'cursor' to the beginning of the file
print(myfile.read()) # Program is able to print out contents this iteration
myfile.close() # Closing file after finishing use

# Writing to a file
# By default 'the open()' function only allows us to read the file
# In order to write over the file we need to pass in the 'w' argument.
"""
NOTE: Opening a file with 'w' or 'w+' truncates the original, meaning that 
# anything that was in the original file is deleted!
"""
myfile = open('Second example text file', 'w+') # Passing 'w+' to allow for read and writing
myfile.write('This is the new line that replaced the original'
             '\nThis is the next line') # Writing content to new file
myfile.seek(0) # Restarting cursor
print(myfile.read()) # Reading file
myfile.close() # Closing file for best practice

# Appending to a file
# Passing the argument 'a' OPENS THE FILE AND PUTS THE POINTER AT THE END
# Like 'w+' does, 'a+' lets us read and write to a file.
# If the file does not exist then a new one will be created
testfile = open('test.txt', 'a+')
# Take note that every iteration that this code runs through will only append and not overwrite the contents
# being written in test.txt
testfile.write('\nThis text is being added to the new file')
testfile.write('\nAdding another line here\tand some content tabbed over here'
               '\n more items')
testfile.close()

# Passing variables within program into file
x = 1
name = 'mark'
# Testing usage of 'w'
testfile = open('test.txt', 'w+')
testfile.seek(0) # Restarting cursor
testfile.write(f"I am trying to see if I can pass an: "
               f"\ninteger: {x}"
               f"\nstring: {name}\n")
testfile.close()

testfile = open('test.txt', 'a+')
testfile.write(f"Now that you can add and append to a file"
               f"\npractice the usage for {name}\n")

# In this program below code it to where it starts at the end of the last .write() statement and appends to the file
# Tip: Get program to start writing at a specific index
testfile = open('test.txt', 'r+')
r_arg = (testfile.write(f"This file is testing the 'r+' argument\n"))
print(r_arg)
testfile.seek(0, 1)
print(testfile.tell())
testfile = open('test.txt', 'a+')
testfile.write('As a result the text overwrites what up to what characters were used'
               '\nIncluding the escape character.\n')
testfile.close()

# Iterating through a File
iter_file = open('newtest.txt', 'w') # Creating new file called 'newtest.txt'
iter_file.write('First Line'
                '\nSecond Line')
iter_file.seek(0)
for line in open('newtest.txt'):
    print(line)

"""
Extra notes on file arguments:

'r'
Opens a file for reading only. 
The file pointer is placed at the beginning of the file. 
This is the default mode.	

'rb'
Opens a file for reading only in binary format. 
The file pointer is placed at the beginning of the file. 
This is the default mode.

'r+'
Opens a file for both reading and writing. 
The file pointer placed at the beginning of the file.

'rb+'
Opens a file for both reading and writing in binary format. 
The file pointer placed at the beginning of the file.

'w'
Opens a file for writing only. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.

'wb'
Opens a file for writing only in binary format. 
Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

'w+'
Opens a file for both writing and reading. 
Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.

'wb+'
Opens a file for both writing and reading in binary format. 
Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.

'a'
Opens a file for appending. 
The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode. 
If the file does not exist, it creates a new file for writing.

'ab'
Opens a file for appending in binary format. 
The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode. 
If the file does not exist, it creates a new file for writing.

'a+'
Opens a file for both appending and reading. 
The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. 
If the file does not exist, it creates a new file for reading and writing.

'ab+'
Opens a file for both appending and reading in binary format. 
The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. 
If the file does not exist, it creates a new file for reading and writing.
"""
