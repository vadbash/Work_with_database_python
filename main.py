import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                    database="homework",
                                    user="vadim",
                                    password="vadim")

cursor=connection.cursor()

#Parametry dla logina v database

def login():

    name = input("Enter name: ")

    password = input("Enter password: ")

    enter = cursor.execute("select name, password from customer where name = %s and password = %s" ,(name, password))

    if name == '':
        print("Your name is empty, try one more time later")
        exit()

    if password == '':
        print("Your password is empty, try one more time later")
        exit()
    

    if not cursor.fetchone():
        print("You don't have an account, or password is incorrect")
    else:
        print("Login successful, HI")

#Parametry dla reestracii v database

def formreg():

    name = input("Hello, enter your username: ")

    password = input("Then enter password: ")

    enter = cursor.execute("select name, password from customer where name = %s and password = %s" ,(name, password))

    if name == '':
        print("Your name is empty, try one more time later")
        exit()

    if password == '':
        print("Your password is empty, try one more time later")
        exit()

    if cursor.fetchone() is None:

        cursor.execute("insert into customer(name, password) values(%s, %s)" ,(name, password))
        connection.commit()
        print('Regestration successful')
    else:
        print('User with such name is already registered, try one more time later')

#Zapyt na reestraciu chi login

typing = input("Do you want registration or login into account (R or L): ")
if typing == 'R':
    formreg()
elif typing == 'L':
    login()

#Perevirka na puste znachenna

if typing == '' or typing == ' ':
    print("You are not typing anything, try one more time later")

cursor.execute("select * from customer")
data=cursor.fetchall()
cursor.close()