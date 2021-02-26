def main():
    total_val=0
    max_val=int(input("Enter the number of values you will enter: "))   #getting int input from user
    for max_val in range(max_val):   #loop however many times specificed by user 
        value=float(input("Enter a value: "))	#user enters value
        total_val+= value					#value= old value + entered value
    print("The sum is: ", total_val)
main()