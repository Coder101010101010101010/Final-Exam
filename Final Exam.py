'''
Joe Hill
Final Exam
Numbers are Funner
This program has multiple number games have fun!
'''

print ("Joe Hill")
print ('')
print ("Numbers are Funner")
print ('')
print ("hope you like numbers")

# For Loops
# counting

print ('')
print ("do you like to count?")
print ('')
for i in range(1, 11):
    print(i)


# while loops
# guess my number

my_number = 42
print ('')
print ("Guess a number between 1 and 50")
print ("")

guess = int(input("Enter a guess: "))

while guess != my_number:
    print ("")
    print ("Wrong number, guess again")
    guess = int(input("Enter a guess: "))

print ("")
print ("Good job you have guessed it")


# functions
# your age next year


age1 = 1

try:
    age2 = int(input('Enter your age: '))
except ValueError:
    print('\n''That wasn\'t an integer for your age')

age = age1 + age2

print ('you will be ' + str(age) + ' years old next year')
print ('')

# Parameters/Arguments
# counting 7 times

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('you are reading this 7 times you just wnt back and counted',7)

# break and continue
# math problem


print ("")

print ('you will be asked one math problem')
print ('1 a coder has 1000 ones and zeros he losses 330 ones and 99 zeros how many zeros and ones does he have left? ')

while True:
    answer = int(input('Enter an answer '))
    if answer > 571:
        print ("to high try again ")

    elif answer <571:
        print ("to low try again ")
    
    else:
        print ("you got it right ")
        break
        
print ('')
print ('you are done!')