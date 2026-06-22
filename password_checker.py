import hashlib
import random
import string
import urllib.request

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short!")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    if any(c in "!@#$%" for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score == 4:
        print("Strength: STRONG password!")
    elif score >= 2:
        print("Strength: MEDIUM password")
    else:
        print("Strength: WEAK password!")

    for tip in feedback:
        print("-", tip)

def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice("!@#$%"))
    for i in range(length - 3):
        password.append(random.choice(chars))
    random.shuffle(password)
    return "".join(password)

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = "https://api.pwnedpasswords.com/range/" + prefix
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        for line in data.splitlines():
            h, count = line.split(":")
            if h == suffix:
                print("WARNING! Found in " + count + " breaches!")
                return
        print("SAFE! Not found in any breach.")
    except:
        print("Could not check breach database.")

print("=== Password Security Checker ===")
print("1. Check my password")
print("2. Generate a strong password")
choice = input("Choose 1 or 2: ")

if choice == "1":
    password = input("Enter password: ")
    print("")
    check_strength(password)
    print("")
    check_breach(password)
elif choice == "2":
    new_password = generate_password()
    print("")
    print("Your generated password: " + new_password)
    print("")
    check_strength(new_password)
else:
    print("Invalid choice!")
