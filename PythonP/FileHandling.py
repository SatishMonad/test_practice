f = open("satish.txt")#to open a file
f = open("satish.txt", "r")#to read a file

print(f.read())

#if we want to open a file in a different location
f = open("D:\\myfiles\satish.txt", "r")
print(f.read()) 


#if we want to read first 5 characters of a file


f = open("satish.txt", "r")
print(f.read(5)) 


#if we want to read first line of a file 


f = open("satish.txt", "r")
print(f.readline()) 

#if we want to open file through loops
f = open("satish.txt", "r")
for x in f:
  print(x)


#if we want to close file 


f = open("satish.txt", "r")
print(f.readline())
f.close() 


#writing to an existing file

f = open("satish.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("satish.txt", "r")
print(f.read()) 



#to delete a file 

import os
os.remove("satish.txt") 
os.unlink("satish.txt")


#to delete an entire folder

import os
os.rmdir("myfolder") 



















