print(""" Task 5: Write a program that reads the  input from the keyboard and converts into another number system as shown below
    (a) 3 digit Decimal to Octal  (b) 3 digit Decimal to Binary   (c) 3 digit Decimal to Hexadecimal

""")
input("Press Enter to Execute Program:")
#function for binary conversion
def dec_to_bin(n):
    binary=[] #number array for storing binary data
    #Binary Conversion Code
    while n > 0 :
        
        binary.append(n%2) #storing remainder in octal array 
        n = n//2
    return binary
 
#function for Octal conversion
def dec_to_oct(n):
    octal = [] #number array for storing octal data
    
    #Octal Conversion Code
    while (n != 0):
        octal.append(n % 8) #storing remainder in octal array
        n = n // 8
    return octal

#function for Hexadecimal conversion
def dec_to_hex(n):
    hexa = [] #number array for storing hexadecimal data

    #Hexadecimal Conversion Code
    while (n != 0):
        hexa.append(n % 16) #storing remainder in Hexadecimal array
        n = n // 16
    return hexa
    

def main():
    #Getting decimal number from user 
    decimal_number=int(input("Enter 3 digit decimal number:"))

    #calling binary conversion function
    binary_Value=dec_to_bin(decimal_number)
    print("\nEquivalent Binary Number: ")
    for i in reversed(binary_Value): #print reverse list    
        print(i,end='')

    #calling octal conversion function
    octal_value=dec_to_oct(decimal_number)#print reverse list
    print("\nEquivalent Octal Number: ")
    for j in reversed(octal_value):
        print(j, end = "")

    #calling hexadecimal conversion function
    hexadecimal=dec_to_hex(decimal_number)#print reverse list
    print("\nEquivalent Hexadecimal Number: ")
    for j in reversed(hexadecimal):
        print(j, end = "")
main()
