# Exercise how to debug

import pdb

def  sum(num1, num2):
    pdb.set_trace()
    
    return num1 + num2

sum(2,'bunny')

