from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key



key = load_key() 
fer = Fernet(key)



def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,password = data.split("|")
            print("User:",user, ", Password:", fer.decrypt(password.encode()).decode()) # It takes all the regular string from add()
                                                                               #Converts the string to bytes (from encode) and then decrypt that bytes 
def add():
    name = input ("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n") #decode converts bites into regular string

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) To quit (q)? ")
    if mode =="q":
        print("Thank you! ")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue