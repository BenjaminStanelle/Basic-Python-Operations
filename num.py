#Benjamin Stanelle 1001534907
def main():
    my_List=[]
    num_Elements= int(input("Enter the number of elements in the list: "))
    for x in range(num_Elements):
        value= float(input("Enter a new element for the list: "))
        my_List.append(value)
    print("Original List: ",my_List)
    
    min=my_List[0]
    max=my_List[0]
    total=0
    average=0
    for x in my_List:
        if x < min:
            min=x
        if x > max:
            max=x
        total+= x
    average=total/len(my_List)
    print("The min is: ",format(min, '.2f'))
    print("The max is: ",format(max, '.2f'))
    print("The total is: ",format(total, '.2f'))
    print("The average is: ",format(average, '.2f'))
main()