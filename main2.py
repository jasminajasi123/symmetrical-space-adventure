# exercise logical operators

num1 = 3
num2 = 7

if num1 < num2 and num2 < num1:
    print('It\'s wrong')
elif num1 > 0 or num2 < 9:
    print('you are right') 
elif num2 > num1 and not num1 > num2:
    print('It\'s completely wrong') 
          
