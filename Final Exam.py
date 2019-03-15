# functions
# your age next year


age1 = 1

try:
    age2 = int(input('Enter your age: '))
except ValueError:
    print('\n''That wasn\'t an integer for your age')

age = age1 + age2

print ('You will be ' + str(age) + ' years old next year')
print ('')