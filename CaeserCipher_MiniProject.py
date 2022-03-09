alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP         `"Y8ba.  .adPPwPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88

           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP        88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def encrypt(para_text, para_shift):
    cipher_text = ""
    for letter in para_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + para_shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

def decrypt(para_text, para_shift):
    cipher_text = ""
    for letter in para_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - para_shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The decoded text is {cipher_text}")

repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        if direction == "encode":
            encrypt(text, shift)
        else:
            decrypt(text, shift)
    else:
        print("Invalid Input!")
    repeat = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    while repeat != "yes" and repeat != "no":
        repeat = input("Wrong Input! Kindly type 'Yes' if you want to continue, otherwise type 'No':\n")
print("Thank You for coming here!!!")