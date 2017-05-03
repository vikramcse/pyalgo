"""
    GCD (Greatest Common Divisor)
    ---------------------------
   greatest common divisor (gcd) of two or more integers, when at least one of 
   them is not zero, is the largest positive integer that divides the numbers 
   without a remainder.

   e.g: he GCD of 8 and 12 is 4.
"""


class GCD():
    """
        Finds the GCD of numbers in a list.
        Input: List of numbers you want to find the GCD of
            e.g. gcd([1, 2, 3]) or gcd(8, 4)
        Returns: GCD of all numbers
    """

    def gcd(self, a, b=None):
        if a != None and b != None:
            if a > 1 and b > 1:
                while a:
                    a, b = b % a, a
                return b
            else:
                raise TypeError("The values must be non zero")
        elif b is None:
            if type(a) == list:
                if len(a) >= 2:
                    return reduce(self.gcd, a)
                else:
                    IndexError("There must be atleast two arguments")
            else:
                raise IndexError("If there is a single argument then it must be a list of values")
