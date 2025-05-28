"""Challenge: Smart Access Control System
You're designing the entry logic for a secure building.
People should be allowed entry only if they meet the following rules:

🛡️ Entry Rules:
If the person is an employee and has a valid badge, they may enter.

If they are a guest, they must be on the approved guest list and must not be banned.

Anyone else is denied access.
"""
is_employee = bool(input("Are you an employee?True or False: "))        # True or False
has_badge   = bool(input("Do you have a badge?True or False: "))       # True or False
is_guest    = bool(input("Are you a guest?True or False: "))      # True or False
is_approved_guest = bool(input("Are you an approved guest?True or False: "))  # True or False
is_banned   = bool(input("Are you banned?True or False: "))       # True or False

if is_employee  and has_badge:
    print("Access granted to employee")
elif is_guest and is_approved_guest:
    print("Access granted to guest")
else:
    print("Access denied")







