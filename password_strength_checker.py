import string

def check_password_strength(password: str) -> dict:
    """
    Check the strength of a password and return:
    - score
    - rating
    - feedback suggestions
    """

    feedback = []
    score = 0

    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Length scoring
    if length == 0:
        feedback.append("Password is empty.")
    elif length < 8:
        score += 10
        feedback.append("Use at least 8 characters.")
    elif length < 12:
        score += 20
    else:
        score += 30

    # Lowercase
    if has_lower:
        score += 15
    else:
        feedback.append("Add at least one lowercase letter.")

    # Uppercase
    if has_upper:
        score += 15
    else:
        feedback.append("Add at least one uppercase letter.")

    # Digit
    if has_digit:
        score += 20
    else:
        feedback.append("Add at least one number.")

    # Special character
    if has_special:
        score += 20
    else:
        feedback.append("Add at least one special character (e.g. !, @, #, $).")

    # Score limit
    if score > 100:
        score = 100

    # Rating based on score
    if length == 0:
        rating = "Invalid"
    elif score < 40:
        rating = "Weak"
    elif score < 70:
        rating = "Moderate"
    elif score < 90:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "score": score,
        "rating": rating,
        "feedback": feedback
    }


def main():
    print("=== Password Strength Checker ===")

    while True:
        pwd = input("\nEnter a password (or type 'exit' to quit): ")

        if pwd.lower() == "exit":
            print("Exiting... Goodbye!")
            break

        result = check_password_strength(pwd)

        print(f"\nScore   : {result['score']}/100")
        print(f"Rating  : {result['rating']}")

        if result["feedback"]:
            print("Suggestions:")
            for f in result["feedback"]:
                print(f" - {f}")
        else:
            print("Your password is strong.")


if __name__ == "__main__":
    main()
