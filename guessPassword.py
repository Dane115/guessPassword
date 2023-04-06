import random


password = int(input("What is a password using only 4 digits? "))

guessPassword = random.randint(0, 9999)
count = 0

print(f"Your password you chose is {password}")

while guessPassword != password:
    count = count + 1
   
    guessPassword = random.randint(0, 9999)
    print(f"My guess is going to be {guessPassword}")
    print(f"Count is: {count}")
    
print(f"Cracked it! it took me {count} iterations to guess your 4 digit code")
    


