# Write a program that accepts a sequence of whitespace separated words as input 
#and prints the words after removing all duplicate words and sorting them alphanumerically.

#Suppose the following input is supplied to the program:

#hello world and practice makes perfect and hello world again
#Then, the output should be:

#again and hello makes perfect practice world

my_sentence = input().split(',')
words = []
def exp(words):
    for words in my_sentence:
        if words.add(words + words):
            return words.remove()
        
        
my_sentence.sort()
print(my_sentence)        

    
  
 



       




    
my_sentence.sort()
