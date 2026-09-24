import secrets
import string


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

characters = letters + numbers + symbols
password = ""

for _ in range(16):
    x = secrets.choice(characters)
    password += x


print(password)