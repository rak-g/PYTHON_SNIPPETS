alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Input a message to be communicated
# Enter shift value to move to alphabets to respective index positions
# Encrypt the message as per shift value
# Decrypt the message as per shift value

# Caesar function for encryption-decryption
def caesar(start_text, shift_amount, encrypt_direction_decrypt):
    end_text = ""
    if encrypt_direction_decrypt == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {encrypt_direction_decrypt}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, encrypt_direction_decrypt=direction)

# #Message Encryption
# def encrypt(plain_text,shift_amount):
#     encoded_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         encoded_text += new_letter
#     print(f"The encoded text is {encoded_text}")
#     
# 
# 
# 
# #Message Decryption
# def decrypt(cipher_text,shift_amount):
#     decoded_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decoded_text += new_letter
#     print(f"The decoded text is {decoded_text}")
#     
# 
# 
# if(direction=="encode"):
#     encrypt(plain_text=text, shift_amount=shift)
# elif(direction=="decode"):
#     decrypt(cipher_text=text, shift_amount=shift)
