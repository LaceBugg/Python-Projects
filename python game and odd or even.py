def main():
    game=input('Do you want to play a game? ')
    if game=='yes':
        guessGame()
    if game=='no':
        numb=input('Do you want to go to my number program? ')
        if numb=='yes':
           oddEven()
    else:
        print('Goodbye')

def random():
    import random
    random.randint(1,50)
        
def guessGame():
    print('Try to guess my number')
    print('You have 10 tries to quess it')
    print('I am thining of a number between 1 and 50')

    import random 
    num=random.randint(1,50)

    guess(num)

def guess(num):
    counter=1
    if counter<=10:
        guessNum=int(input('What is your guess? '))
        if guessNum < num:
            print('Try again. Higher')
            counter=counter+1
            return guess(num)
        if guessNum > num:
            print('Try again. Lower')
            counter=counter+1
            return guess(num)
        if guessNum == num:
            print('CORRECT Good job!')
        else:
            print('Error')
    else:
        print('You have run out of guesses. Better luck next time')
    again()

def again():
        again=input('Do you want to play again? ')
        if again=='yes':
            guessGame()
        if again=='no':
            numb=input('Do you want to go to my number program? ')
            if numb=='yes':
               oddEven()
            else:
                print('Goodbye')
        else:
            print()


def oddEven():
    print()
    print('Welcome to is it ODD or EVEN?')
    num = int(input('Enter a number: '))
    if (num % 2) == 0:
        print(num,'is EVEN')
    else:
        print(num,'is ODD')
        prime = input('Do you want to know if it is prime? ')
        if prime == 'yes':
            isPrime(num)
        else:
            print('The end')

def isPrime(num):
    #print('Welcome to is it a prime number?')
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,'is NOT a prime number')
                break
        else:
            print(num,'IS a prime number')
    else:
        print(num,'is 1 or less and cannot be a prime number') 

main()
