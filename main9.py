# exercise Error Handling

while True:
    try:
        my_age = int(input('How old are you? '))
        10/my_age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you') 
    finally:
        print('ok I am fine')
    print('Can you hear me ?')            

