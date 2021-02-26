#Benjamin Stanelle 1001534907
def main():
    words_List=[]
    new_List=[]
    file_Name=input("Enter the file  name: ")   #entering a text file name
    read_File= open(file_Name,'r')          #opening text file for reading
    my_List=read_File.readlines()            #reading up until new line and storing in array

    uppercase_Char=0   #initializing values
    lowercase_Char=0
    digit_Char=0
    space_Char=0
        
    for i in range(len(my_List)): #double for loop to get characters stored in 2d array
        for j in range(len(my_List[i])):
            if(ord(my_List[i][j])==32):  #comparing the ascii value of the characters to the ascii table
                space_Char+=1
            if(ord(my_List[i][j])<=57 and (ord(my_List[i][j])>=48)):
                digit_Char+=1
            if(ord(my_List[i][j])<=122 and (ord(my_List[i][j])>=97)):
                lowercase_Char+=1
            if(ord(my_List[i][j])<=90 and (ord(my_List[i][j])>=65)):
                uppercase_Char+=1
                
    print("The number of uppercase characters is: ",uppercase_Char)            
    print("The number of lowercase characters is: ",lowercase_Char)
    print("The number of digit characters is: ",digit_Char)
    print("The number of space characters is: ", space_Char)
    
    read_File.close()          #closing file for reading
    append_File= open(file_Name,'a+')      #opening file for appending
    #appending to that file
    append_File.write("\nThe number of uppercase characters is: %d\r\n" %uppercase_Char)
    append_File.write("The number of lowercase characters is: %d\r\n" %lowercase_Char)
    append_File.write("The number of digit characters is: %d\r\n" %digit_Char)
    append_File.write("The number of space characters is: %d\r\n" %space_Char)
    
main()