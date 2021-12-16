import random
import string

print("HELLO,, WELCOME TO DARK CYBER WEAPON PASSWORD GENERATOR")

print(" ____        _        ____    ____  ")
print(" |  _ \     / \      / ___|  / ___| ")
print(" | |_) |   / _ \     \___ \  \___ \ ") 
print(" |  __/   / __ _\     ___) |  ___) | ")   
print(" |_|     /_/     \_   |____/  |____/ ")   

print(" __        __   ___    ____    ____ ")
print(" \ \      / /  / _ \  |  _ \  |  _ \ ")
print("  \ \ /\ / /  | | | | | |_) | | | | | ")
print("   \ V  V /   | |_| | |  _ <  | |_| | ")
print("    \_/\_/     \___/  |_| \_\ |____/ ")
print(" ")
print("           @## FROM DARK CYBER WEAPON")

 
length = int( input( '\nENTER YOUR PASSWORD LENGTH: ' ))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)

password = " ".join(temp)
print(" ")
print(" ")
print(password)
print(" ")
print(" ")

print("@#### COPY GENARATOD PASSWORD AND SAVE THIS STRONG PASSWORD ####@..")
