class Fraction:
    
    """Create Fractions and use addition subtraction multily or divide as below
    x = Fraction(3,4)
    y = Fraction(5,6)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    """
    
    # Instantiating numerator and denominator
    def __init__(self, num, den):
        self.num = num
        self.den = den
      
    # String representation
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
      
    # Defining Addition
    def __add__(fo1, fo2):
        return Fraction(fo1.num * fo2.den + fo1.den * fo2.num, fo2.den * fo1.den)
      
    # Defining Subtraction
    def __sub__(fo1, fo2):
        return Fraction(fo1.num * fo2.den - fo1.den * fo2.num, fo2.den * fo1.den)
      
    # Defining Multiplication
    def __mul__(fo1, fo2):
        return Fraction(fo1.num * fo2.num, fo1.den * fo2.den)
      
    # Defining Division
    def __truediv__(fo1, fo2):
        return Fraction(fo1.num * fo2.den, fo2.num * fo1.den)
       
x = Fraction(3,4)
y = Fraction(5,6)
print("x: ", x)
print("y: ", y)
print("x+y: ", x+y)
print("x-y: ", x-y)
print("x*y: ", x*y)
print("x/y: ", x/y)
