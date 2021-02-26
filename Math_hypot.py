import math  #importing the library from which to use the hypot function

def main():
    side1=float(input("Enter the length of side 1: "))   
    side2=float(input("Enter the length of side 2: "))
    
    print("The length of the hypotenuse is ", format(math.hypot(side1,side2), '.2f'))  #calling the hypot function from math and printing
main()