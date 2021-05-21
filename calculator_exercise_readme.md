# Calculator Exercise Readme

In this first iteration, I set up the functions inside a class. In order to be able to call them without instantiating, I packaged them under ```@staticmethod```. Here is the class in the first iteration

```
class Calculator:
    #made them static methods so that I don't have to create an object.
    
    def add(value1,value2) : return value1 + value2

    def subtract(value1, value2): return value1 - value2

    def multiply(value1, value2) : return value1 * value2

    def divide(value1, value2) : return value1 / value2

    def divisible(value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

    def inchtocm(value1): return value1 * 2.54

    def triangle_area(height, width): return height*width/2

```
The test cases could then be called simpy using ```Calculator.[method]([args] ``` . The output is as expected. Test cases are below:

```
#Test Cases

print(Calculator.add(1,1))
print(Calculator.subtract(1,1))
print(Calculator.multiply(1,2))
print(Calculator.divisible(4,2))
print(Calculator.divisible(3,2))
print(Calculator.divisible(3,0))
print(Calculator.divide(4,2))
print(Calculator.inchtocm(2))
print(Calculator.triangle_area(2,2))
```

The next iteration would be to not use static methods (as this was advised against by Sharukh).