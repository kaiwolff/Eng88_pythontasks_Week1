# The FizzBuzz task

My first iteration was to simply ensure the logic was being executed correctly

```
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

```
Note that placing Fizzbuzz as the first if statement ensures no duplicate printouts for FizzBuzz numbers. I initially only used printouts, and haven't yet packaged the logic into a class and method format.