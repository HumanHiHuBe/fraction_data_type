class Fraction:

    """Create Fractions and use addition subtraction multiply or divide as below
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

# first_fraction = Fraction(int(input("Enter Numerator for first Fraction:")),int(input("Enter denominator for first Fraction: ")))
# second_fraction = Fraction(int(input("Enter Numerator for second Fraction:")),int(input("Enter denominator for second Fraction: ")))

# print("first_fraction: ", first_fraction)
# print("second_fraction: ", second_fraction)
# print("first_fraction+second_fraction: ", first_fraction+second_fraction)
# print("first_fraction-second_fraction: ", first_fraction-second_fraction)
# print("first_fraction*second_fraction: ", first_fraction*second_fraction)
# print("first_fraction/second_fraction: ", first_fraction/second_fraction)
