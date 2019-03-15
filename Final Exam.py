
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
