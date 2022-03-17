# Notes:
# ord() returns ASCII value of input
# chr() returns letter of ASCII value
# i.e.:
# ord("A") returns so A_val = 65
# chr(A_val + 3) would returns D(ASCII 68)
# variable.upper() will make a message all uppercase

def get_shift():
    global shift 
    shift = int(input("Enter the shift value: "))
    shift = shift % 26
    return shift

def get_message():
    global message
    message = input("Enter the message you want to use: ")
    message.upper()
    return message

def encrypt():
    get_shift()
    get_message()
    outputVal = ""
    for i in range(len(message)):
        ASCII_Val = ord(message[i])
        if ASCII_Val >= 65 and ASCII_Val <= 90:
            New_Val = ASCII_Val + shift
            if New_Val > 90:
                New_Val -= 26
            elif New_Val < 65:
                New_Val += 26
        else:
            New_Val = ASCII_Val
        Character = chr(New_Val)
        outputVal += Character
    print(outputVal)

def brute_decrypt():
    get_message()
    for ii in range(26):
        outputVal = ""
        for i in range(len(message)):
            ASCII_Val = ord(message[i])
            if ASCII_Val >= 65 and ASCII_Val <= 90:
                New_Val = ASCII_Val + ii
                if New_Val > 90:
                    New_Val -= 26
                elif New_Val < 65:
                    New_Val += 26
            else:
                New_Val = ASCII_Val
            Character = chr(New_Val)
            outputVal += Character
        print(outputVal)

menuChoice = 0
while menuChoice != 3:
    print("\n1. Encrypt")
    print("2. Brute-Force Decrypt")
    print("3. Close Program")
    menuChoice = int(input("Please enter your menu choice: "))
    if menuChoice == 1:
        print("1. Encrypt")
        # Add call to subroutine
        encrypt()
    elif menuChoice == 2:
        print("2. Brute-Force Decrypt")
        # Add call to subroutine
        brute_decrypt()
    elif menuChoice == 3:
        print("Goodbye")
        input("Press enter to close")