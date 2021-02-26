def feet_to_inches(feet1):
    feet1 = feet1*12; #converting feet to inches
    return feet1;		#returning the conversion
def main(): 
    feet=float(input("Enter the number of feet:"));  #Getting input as a float
    inches=feet_to_inches(feet);			#sending to the function to convert to inches
    print(feet, "feet  = ", format(inches, '.2f'), "inches") 	#printing the converted feet to inches
    
main()