import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 4:
        remarks = "Strong password"
    elif strength == 3:
        remarks = "Moderate password"
    else:
        remarks = "Weak password"

    return remarks

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(check_password_strength(user_password))
