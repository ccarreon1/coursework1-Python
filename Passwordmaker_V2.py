import random

password = '' # this creates a string variable which will be used as the final password
passlength = random.randint(8,13) # this will determind the length of the password

capletter = random.randint(1,passlength) #used so it guarantees atleast one capital letter is present
lowercase = random.randint(1,passlength) # used so it guarantees atleast one lower case letter is prestn
while capletter == lowercase: #make sures the capital letter and lower case value is not at the same position
    lowercase = random.randint(1,passlength)
number = random.randint(1,passlength)# used so it guarantees atleast one number will be present in password
while number == capletter or number == lowercase: # makes the number will not be in the same possition as  cap letter and lower case
    number = random.randint(1,passlength)

prevcharvalue = "aa" #varible used make sure no consecutive password is duplicate
for i in range(passlength): #loop repeated depending on pass length
    x = random.randint(1,3) # creates a random number used to determing if char value is a number, cap letter or lower case
    valid = False # boolean variable used to make sure char value is valid
    while not valid:
        if i == number or x == 1 and  i != capletter and i != lowercase:  
            charvalue= chr(random.randint(ord('0'),ord('9'))) # generates a number used for the password based on ascii values for numbers
        elif i == capletter or x == 2 and i !=lowercase and i != number:
            charvalue= chr(random.randint(ord('A'),ord('Z'))) # generates a upper case value based on ascii values for capital letters
        elif x == 3 or i == lowercase:
            charvalue= chr(random.randint(ord('a'),ord('z'))) # generates a lower case value based on ascii value for lower case values
        if charvalue != prevcharvalue: #compares value created and prevous value to make sure they are not identical or loop will be repeated
            valid = True
    password += charvalue #adds the new value to the password variable
    prevcharvalue = charvalue # replaces prevcharvalue with char value created used for test if loop repeats

print(password) # displays password
