import random

def run_guess(guess, answer):
    if 0 < guess < 22:
        if guess == answer:
            print('you a\'re a genius')
            return True
    else:
        print('hey bobo I say between 2 ~ 22') 
        return False
if __name__ == '__main__' :
    answer = random.randint(2,22)
    while True: 
        try:
            guess = int(input('please tell me the random number between 2 ~ 22: '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('enter a number')
            continue     

