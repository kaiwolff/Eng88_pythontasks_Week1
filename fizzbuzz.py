# The Problem
#
# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
#
# NOTE -> Must be in class and method format

#start by going through values from 1 to 100. Note the range has to be 101 as the last value isn't printed

for i in range(1,101):
    #set up conditions. Priorities are:
    # 1. Fizzbuzz, as we want to print neither fizz nor buzz, but a combo
    # 2. is it it fizz or buzz, as we don't want to print hte number if it fizzes or buzzes
    # 3. print the number if no conditions met
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:#no fizzbuzz, check for fizz
        print("Fizz")
    elif i % 5 == 0: #No fizzbuzz, no fizz, check for buzz
        print("Buzz")
    else: #if nothign else print the number
        print(i)