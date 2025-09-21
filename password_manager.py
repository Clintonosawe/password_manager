import hashlib #Module helps to encrypt string 
import getpass #Module helps to hide string 

password_manager = {} 

def create_account(): 
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    password_manager[username] = hashed_password 
    print("Account created successfully!")
