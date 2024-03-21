
def add():
    user_name = input("Please enter a User Name: ")
    pswd = input("Please Enter a Password: ")
    with open('password.txt', 'a')as f:
        f.write(user_name + "|" + pswd + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f:
            print(line)
        


while True:
    mode = input('Welcome to Password Manager for adding password type add for viewing type view and q to quit ').lower()
    if mode == "q":
        break

    if mode == 'add':
        add()

    elif mode == 'view':
        view()

    else:
        print('Invalid Syntax')
        continue