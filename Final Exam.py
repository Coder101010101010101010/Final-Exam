# Joe Hill
# Final Exam Number's code

print ("hope you like numbers")

# For Loops
# counting

print ("do you like to count to 100? Well to bad if you don't")
for i in range(101):
    print(i)


# while loops

my_number = 42

print ("Guess a number between 1 and 50")
print ("")

guess = int(input("Enter a guess: "))

while guess != my_number:
    print ("")
    print ("Wrong number, guess again")
    guess = int(input("Enter a guess: "))

print ("")
print ("Good job you have guessed it")


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
        
