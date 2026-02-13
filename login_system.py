#LA 6
name = "Peregrine901"
password = "59233"

username = input("Enter username: ")
userpasswrd = input("Enter password: ")

if username == name:
    if userpasswrd == password:
        print("Welcome! Login successful.")
    
    else:
        print("incorrect password")
else:
    print("user not found")
