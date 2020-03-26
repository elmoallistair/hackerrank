# Written: 18-Jan-2020
# https://www.hackerrank.com/challenges/30-scope

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(difference, self.maximumDifference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)