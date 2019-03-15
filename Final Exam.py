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
print ('You are done!')