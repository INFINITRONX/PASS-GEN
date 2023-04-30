import os
import random
import string
os.system("clear")
logo = """
█▀█ ▄▀█ █▀ █▀   █▀▀ █▀▀ █▄░█
█▀▀ █▀█ ▄█ ▄█   █▄█ ██▄ █░▀█"""
print("              _______________                        |*\_/*|________")
print("             |  ___________  |     .-.     .-.      ||_/-\_|______  |")
print("             | |           | |    .****. .****.     | |           | |")
print("             | |   0   0   | |    .*****.*****.     | |   0   0   | |")
print("             | |     -     | |     .*********.      | |     -     | |")
print("             | |   \___/   | |      .*******.       | |   \___/   | |")
print("             | |___     ___| |       .*****.        | |___________| |")
print("             |_____|\_/|_____|        .***.         |_______________|")
print("               _|__|/ \|_|_.............*.............._|________|_ ")
print("              / ********** \                          / ********** \ ")
print("            /  ************  \                      /  ************  \ ")
print("           --------------------                    --------------------")
print("")
print(logo)
print("")


length = int( input( '\n[+] Enter Length Of Password:>  ' ))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower+upper+num+symbols

temp = random.sample(all, length)

password = "".join(temp)
print(" ")
print(" ")
print("[+] Your Genarated Password Is :> ", password)
print(" ")
print(" ")


