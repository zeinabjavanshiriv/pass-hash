import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_pass(password, stored_pass):
    return hash_password(password) == hash_password(stored_hash)


stored_hash = "SilverStar"
print("=======================\nWelcome\n=======================\n")
while True:
    menu = input("1.Hash the password\n2.verify password\n3.Exit\nSelect one: ")
    if menu == "1":
        password = input("Enter your pass: ")
        hashed = hash_password(password)
        print(f"Your Hash is: {hashed}")
        break
    elif menu == "2":
        password = input("Enter the stored password: ")
        if stored_hash == password:
            print("It's true!")
        else:
            print(
                "=======================\nIt's wrong!\nTry again!\n======================="
            )
            continue
    elif menu == "3":
        print("=======================\nBye!\n=======================")
    else:
        print(
            "=======================\nInvaild input try again!\n======================="
        )
        continue
