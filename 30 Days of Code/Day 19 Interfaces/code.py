# Written: 31-Jan-2020
# https://www.hackerrank.com/challenges/30-interfaces

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor = list()
        for i in range(1, n+1):
            if n%i == 0:
                divisor.append(i)
        return sum(divisor)

        # Shorter code:
        # return sum([i for i in range(1, n+1) if n%i == 0])

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)