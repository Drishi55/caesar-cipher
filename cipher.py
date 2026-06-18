print("===== Caesar Cipher =====")

message = input("Enter your message: ")
shift = int(input("Enter shift number: "))
choice = input("Type 'encode' or 'decode': ")

result = ""

for letter in message:
    if choice == "encode":
        result = result + chr(ord(letter) + shift)
    else:
        result = result + chr(ord(letter) - shift)

print("Result:", result)
print("=========================")
