import re
import hashlib

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
    
# Run the program
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")  # Ask user for a password
    result = check_password_strength(user_password)  # Evaluate password strength
    print(result)  # Print the result


