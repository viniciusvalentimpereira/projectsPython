alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, code_direction):
  final_text = ""
  if code_direction == "decode":
    shift_amount *= -1
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      final_text += alphabet[new_position]
    else:
      final_text += char
  print(f"Here's the {code_direction}d text: {final_text}")

############################################################################
from art import logo
print(logo)
############################################################################
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(plain_text=text, shift_amount=shift, code_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_continue = False
    print("Goodbye")

