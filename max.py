def main():
    value1=int(input("Enter the first value: "))  #getting two int inputs from user
    value2=int(input("Enter the second value: "))
    max1=maximum(value1, value2)		#calling the maximum 
    print("The maximum is: ", max1)     #printing the max of those two values
    
def maximum(a, b):	
    if(a<b):		#if the first value is less than the second
        return b	#return the second as the max
    else:
        return a	#else return the first
main()