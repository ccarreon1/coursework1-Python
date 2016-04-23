import random
password = '' # this creates a string variable which will be used as the final password
passlength = random.randint(8,13) # this will determind the length of the password
for i in range(passlength): #loop repeated depending on pass length
    x = random.randint(1,3) # creates a random number used to determing if char value is a number , cap letter or lower case
    if x == 1:  
       password += chr(random.randint(48,57)) # generates a random char number value and adds it to password string
    elif x == 2:
        password += chr(random.randint(65,90)) # generates a upper case char value and add to password string
    else:
        password += chr(random.randint(97,122)) # generates a lower case char value and add to password string
print(password) # prints password on screen
