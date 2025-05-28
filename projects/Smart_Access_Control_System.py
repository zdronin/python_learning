"""Challenge: Smart Access Control System
You're designing the entry logic for a secure building.
People should be allowed entry only if they meet the following rules:

🛡️ Entry Rules:
If the person is an employee and has a valid badge, they may enter.

If they are a guest, they must be on the approved guest list and must not be banned.

Anyone else is denied access.
"""
def to_bool(value):
    """Converts user input into a proper boolean."""
    return value.strip().lower() in ["true", "t", "yes", "y"]

# Prompt for inputs
is_employee = to_bool(input("Are you an employee? (True/False): "))
has_badge = to_bool(input("Do you have a badge? (True/False): "))
is_guest = to_bool(input("Are you a guest? (True/False): "))
is_approved_guest = to_bool(input("Are you an approved guest? (True/False): "))
is_banned = to_bool(input("Are you banned? (True/False): "))

# Access logic
if is_employee and has_badge:
    print("Access granted to employee.")
elif is_guest and is_approved_guest and not is_banned:
    print("Access granted to guest.")
else:
    print("Access denied.")