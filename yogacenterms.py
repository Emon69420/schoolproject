# yoga center manager

import mysql.connector 
mycon = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'YOGA')
print(mycon)

def authen(user, passwo):
    query = 'SELECT PASSWORD FROM USER WHERE NAME = %s'
    data = user
    if query == passwo:
        return 'user authenticated'
    else:
        return 'wrong credentials'
def accCreation(user, passwo):
    query = "INSERT INTO USER(`NAME`, `PHONE`, `PASSWORD`) VALUES(%s, %s, %s)"
    VALUES = 






print("1) LOG INTO EXISTING ACCOUNT")
print("2) CREATE NEW ACCOUNT")

selection = int(input("select an option: "))

if selection == 1:
    user = input('enter username : ')
    passwo = input('enter password for the corresponding username: ')
    authen(user, passwo)
else:
    user = input('create new username: ')
    passwo = input('enter password for the new account: ')
    pho = int(input("enter phone number to be associated to the account: "))
    accCreation(user, passwo)
