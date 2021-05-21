class Calculator:
    #made them static methods so that I don't have to create an object.
    def add(self, value1, value2) : return value1 + value2

    def subtract(self, value1, value2): return value1 - value2

    def multiply(self, value1, value2) : return value1 * value2

    def divide(self, value1, value2) : return value1 / value2

    def divisible(self, value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False

    def inchtocm(self, value1): return value1 * 2.54

    def triangle_area(self, height, width): return height*width/2



#Test Cases
my_calc = Calculator()

print(my_calc.add(1,1))
print(my_calc.subtract(1,1))
print(my_calc.multiply(1,2))
print(my_calc.divisible(4,2))
print(my_calc.divisible(3,2))
print(my_calc.divisible(3,0))
print(my_calc.divide(4,2))
print(my_calc.inchtocm(2))
print(my_calc.triangle_area(2,2))