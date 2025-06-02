def validate_password(**kwargs):
    password = kwargs.get("password", "")
    if len(password) < 8:
        return "Password too short"
    if not any(c.islower() for c in password):
        return "Password must include a lowercase letter"
    if not any(c.isupper() for c in password):
        return "Password must include an uppercase letter"
    if not any(c.isdigit() for c in password):
        return "Password must include a digit"
    return "Password is strong"

user_input = input("Enter a password to validate: ")
result = validate_password(password=user_input)
print(result)
