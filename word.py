#Benjamin Stanelle 1001534907
def main():
    words_List=[]
    file_Name=input("Enter the file  name: ")      #getting file name
    read_File= open(file_Name,'r')        #opening for reading
    my_List=read_File.readlines()         #reading file up until new line
    total_Values=0
    for i in range(len(my_List)):         #looping through the length of the list
        words_List.append(my_List[i].rstrip("\n").split(" "))   #striping down the array
        
    for i in range(len(words_List)):          #looping through and getting the words
        total_Values+=len(words_List[i])

    average=(total_Values)/len(my_List)  #calculating the average words per sentence
    print(words_List,"\n")
    print("The number of sentences is: ",len(words_List))
    print("The total number of words is: ",total_Values)
    print("The average number of words per sentence is: ",average)
    read_File.close()
    
main()