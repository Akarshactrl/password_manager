
master_pwd = input("what is the master password?")

def view(): #here we are using function calls
    #pass
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(':')
            #"hello:aku:yes:2"
            #["hello","aku","yes","2"] this is spli operator
            print("user:",user,"password:", password)

def add():
    #pass
    name = input('account name :')
    pwd = input('password :')

    with open('password.txt','a') as f:#here f is file saving in file with 'a' append mode means adding at last
        f.write(name + " " + pwd + "\n")#added password should be print in next line

while True:
    mode = input("would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
       view()
    elif mode == "add":
       add() #here we are using the above called functions to look more organised
    else:
        print("invalid mode")
