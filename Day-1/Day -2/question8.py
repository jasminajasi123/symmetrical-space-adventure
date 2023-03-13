# Write a program that accepts a comma separated sequence of words as input and prints the words in a 
#comma-separated sequence after sorting them alphabetically.

#Suppose the following input is supplied to the program:

#without,hello,bag,world
#Then, the output should be:

#bag,hello,without,world

list1 = ['bunny','shkulaku','renato','jasmin','esmi','egli']
print(list1.sort())
print(list1)

my_list = input('give your favourite name : ').split(',')
my_list.sort()
print(my_list)
