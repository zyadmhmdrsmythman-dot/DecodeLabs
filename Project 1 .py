import string

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1

if score <= 1:
    print("Weak Password")
elif score <= 3:
    print("Medium Password")
else:
    print("Strong Password")
