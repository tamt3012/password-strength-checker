import re
import hashlib
import requests

# List of common weak passwords
COMMON_WEAK_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "12345678", "111111", "123123",
    "abc123", "password1", "1234", "12345", "admin", "letmein", "welcome"
]

def check_password_strength(password):
    """
    This function evaluates the strength of a password based on:
    - Common weak passwords list
    - Length (Minimum 8 characters)
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """
    if password.lower() in COMMON_WEAK_PASSWORDS:
        return "Weak password. Avoid using common passwords."

    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special_chars": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    #Count how many criteria are met
    score = sum(strength_criteria.values())

    #Provide feedback
    if score == 5:
        return "Password is strong."
    elif score >= 3:
        return "Password is moderate. Consider adding more complexity."
    else:
        return "Weak password. Please include a mix of uppercase, lowercase, digits, and special characters."
    
def check_if_pwned(password):
    """
    Uses the Have I Been Pwned API to check if the password has appeared in known data breaches.
    """
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error checking for breaches. Please try again later."
    
    hashes = (line.split(":") for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return f"Password has been found in {count} breaches. Choose a different one."
        
    return "This password has not been found in any known breaches."

# Run the program
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    
    # Check password strength
    result = check_password_strength(user_password)
    print(result)

    # Check if password has been pwned
    if not result.startswith("Weak"):
        breach_result = check_if_pwned(user_password)
        print(breach_result)






