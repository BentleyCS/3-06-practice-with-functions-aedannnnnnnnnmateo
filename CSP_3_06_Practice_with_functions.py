#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)
pass

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    s = (a + b + c)/2
    return s
print(semiPerimeter(6,7,8))
#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s,a,b,c):
    result = s * (s-a) * (s-b) * (s-c)
    return result
print(multiplyDifferences(1,2,3,4))

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    area = multiplyDifferences(s, a, b, c) ** 0.5
    return area
print(herons(1,2,3))

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator():
    num =int(input("Give me a number: "))
    return num * 2
print(denominator())

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a,b):
    a = int(input("Give me a number: "))
    b = int(input("Give me another number: "))
    a = a * -1
    return (-a+b , -a-b)
print(plusMinus())

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    result = b**2 - (4*a*c)
    return result
print(mainCalc(10,12,20))

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"
    x1 = (-b+ math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1,x2
print(quadratic(1,12,20))

