import re

def password_strength_checker(password):
    strength_criteria = 0
    feedback = ""

    # Check length
    if len(password) >= 8:
        strength_criteria += 1
        feedback += "Good length. "
    else:
        feedback += "Password is too short. "

    # Check for uppercase letters
    if re.search("[A-Z]", password):
        strength_criteria += 1
        feedback += "Contains uppercase letters. "
    else:
        feedback += "No uppercase letters found. "

    # Check for lowercase letters
    if re.search("[a-z]", password):
        strength_criteria += 1
        feedback += "Contains lowercase letters. "
    else:
        feedback += "No lowercase letters found. "

    # Check for numbers
    if re.search("[0-9]", password):
        strength_criteria += 1
        feedback += "Contains numbers. "
    else:
        feedback += "No numbers found. "

    # Check for special characters
    if re.search("[^A-Za-z0-9]", password):
        strength_criteria += 1
        feedback += "Contains special characters. "
    else:
        feedback += "No special characters found. "

    # Determine password strength
    if strength_criteria == 0:
        return "Very Weak", feedback
    elif strength_criteria == 1:
        return "Weak", feedback
    elif strength_criteria == 2:
        return "Moderate", feedback
    elif strength_criteria == 3:
        return "Strong", feedback
    elif strength_criteria == 4:
        return "Very Strong", feedback
    else:
        return "Excellent", feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength_checker(password)
    print(f"Password Strength: {strength}")
    print(feedback)

if __name__ == "__main__":
    main()