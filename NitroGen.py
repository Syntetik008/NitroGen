#imports
import random
import sys

loopnum = 0

many = input("How many to generate: ")  # asks for how many links to generate

f= open("output.txt","w+")  # creating output.txt

while loopnum < int(many):  # loop
    result_str = ''.join((random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890') for i in range(16)))  # generate link
    print("https://discord.gift/" + result_str)  # show link
    f.write("https://discord.gift/" + result_str + "\n")  # adding links to output.txt
    loopnum += 1

input("ok? (press any button)")
