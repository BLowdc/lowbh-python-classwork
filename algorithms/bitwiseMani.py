def toLowercase(txt):
    result = ""
    for char in txt:
        ascii_val = ord(char) | 0b00100000 # Set the 6th bit to 1
        result += chr(ascii_val)
    return result
# end function
def toUppercase(txt):
    result = ""
    for char in txt:
        ascii_val = ord(char) & 0b11011111 # Set the 6th bit to 0
        result += chr(ascii_val)
    return result
# end function
def toggleCase(txt):
    result = ""
    for char in txt:
        ascii_val = ord(char) ^ 0b00100000 # Toggle the 6th bit
        result += chr(ascii_val)
    return result
# end function
def addCommas(num):
    new_num = ""
    num_str = str(num)[::-1]
    for n in range(len(num_str)):
        if n % 3 == 0 and n != 0:
            new_num += ","
        # end if
        new_num += num_str[n]
    return new_num[::-1]
# end function

# main
while True:
    option = int(input("Choose an option:\n1. To Lowercase\n2. To Uppercase\n3. Toggle Case\n4. Add Commas\n5. Exit\n"))
    if option == 5:
        break
    text = input("Enter a string or number:")
    if option == 1:
        print(toLowercase(text))
    elif option == 2:
        print(toUppercase(text))
    elif option == 3:
        print(toggleCase(text))
    elif option == 4:
        print(addCommas(text))
    # end if
# end while