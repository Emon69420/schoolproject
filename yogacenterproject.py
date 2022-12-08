import mysql.connector
from datetime import datetime
mycon = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'YOGA')
cur = mycon.cursor()
def authen(user, passwo):
    cur.execute('SELECT * FROM USER')
    data = cur.fetchall()
    for row in data:
        if (user in row) and (passwo in row):
            i = 1
            while i == 1:
                
                print('1) view all the available courses')
                print('2) start a  new booking')
                print('3) get help regarding a course')
                print('4) get user data')
                selection = int(input('select an option from above: '))
                if selection == 1 :
                    cur.execute('select * from exercises')
                    data = cur.fetchall()
                    print( 'SNo., Name Of Asan, Difficulty')
                    for row in data:
                        print(row)
                    i = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                    if  i == 1:
                        continue;
                    else:
                        break;
                elif selection == 2:
                    print('ID| NAME OF EXERCISE| DIFFICULTY')
                    cur.execute('select * from exercises')
                    data = cur.fetchall()
                    print( 'SNo., Name Of Asan, Difficulty')
                    for row in data:
                        print(row)
                    username = user
                    query =  'SELECT ID FROM USER WHERE NAME = %s'
                    data = (user,)
                    cur.execute(query, data)
                    fetchedID = cur.fetchone()
                    (ID,) = fetchedID
                    print(type(ID))
                    exercise = input('enter the name of the exercise you want to practise from above: ')
                    timing = input('enter your desired timing for the practise, also specify am or pm: ')
                    mode = input('enter desired mode for the exercise (offline/online): ')
                    query = 'INSERT INTO BOOKINGS(`USER ID`, `USER NAME`, `EXERCISE NAME`, `TIMING`, `MODE OF APPOINTMENT`) VALUES(%s , %s, %s, %s, %s)'
                    val = (ID, username,exercise, timing, mode)
                    cur.execute(query, val)
                    mycon.commit()
                    print('booking successful')
                    cur.execute('select * from bookings order by `BOOKING ID` desc limit 1')
                    info = cur.fetchall()
                    print('(USER ID |  USER NAME | TIMING | MODE | BOOKING ID)')
                    for row in info:
                        print(row)
                    i = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                    if  i == 1:
                        continue;
                    else:
                        break;
                elif selection == 3:
                    helpreq = input('Write the content for help required with within 100 words: ')
                    query =  'SELECT ID FROM USER WHERE NAME = %s'
                    data = (user,)
                    cur.execute(query, data)
                    fetchedID = cur.fetchone()
                    (ID,) = fetchedID
                    date = datetime.today().strftime('%Y-%m-%d')
                    print(date)
                    query = 'INSERT INTO QUERIES(`HELP`, `DATE`, `USER ID`) VALUES(%s, %s, %s)'
                    val = (helpreq, date, ID)
                    cur.execute(query, val)
                    mycon.commit()
                    
                    query = 'SELECT * FROM QUERIES WHERE `USER ID` = %s'
                    data = (ID,)
                    cur.execute(query, data)
                    
                    info = cur.fetchall()

                    print('|QUERY ID| QUERY CONTENT | DATE OF QUERY | USER ID |')
                    for row in info:
                        print(row)
                    i = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                    if  i == 1:
                        continue;
                    else:
                        break;
                elif selection == 4:
                    j = 1
                    while j == 1:
                        print('1) update phone nummber')
                        print('2) view all the past bookings')
                        print('3) view all the queries for helpdesk')
                        selection = int(input(' enter the option to continue with: '))
                        if selection == 1:
                            newNumber= int(input('enter new number: '))
                            query =  'SELECT ID FROM USER WHERE NAME = %s'
                            data = (user,)
                            cur.execute(query, data)
                            fetchedID = cur.fetchone()
                            (ID,) = fetchedID
                            query = 'UPDATE USER SET `PHONE` = %s where `ID` = %s '
                            data = (newNumber, ID)
                            cur.execute(query, data)
                            mycon.commit()
                            print('sucessfully updated the number')
                            j = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                            if  j == 1:
                                continue;
                            else:
                                break;
                        elif selection == 2:
                            query =  'SELECT ID FROM USER WHERE NAME = %s'
                            data = (user,)
                            cur.execute(query, data)
                            fetchedID = cur.fetchone()
                            (ID,) = fetchedID
                            query = 'SELECT * FROM BOOKINGS WHERE `USER ID` = %s'
                            data = (ID,)
                            cur.execute(query, data)
                            rows = cur.fetchall()
                            print('USER ID| USER NAME| EXERCISE NAME | TIMING | MODE OF APPOINTMENT | BOOKING ID')
                            for data in rows:
                                print(data)
                            j = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                            if  j == 1:
                                continue;
                            else:
                                break;
                        elif selection == 3:
                            query =  'SELECT ID FROM USER WHERE NAME = %s'
                            data = (user,)
                            cur.execute(query, data)
                            fetchedID = cur.fetchone()
                            (ID,) = fetchedID
                            query = 'SELECT * FROM QUERIES WHERE `USER ID` = %s'
                            data = (ID,)
                            cur.execute(query, data)
                            rows = cur.fetchall()
                            print('QUERY ID| HELP CONTENT | DATE | USER ID')
                            for data in rows:
                                print(data)
                            j = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                            if  j == 1:
                                continue;
                            else:
                                break;
                        elif selection == 4:
                            query =  'SELECT ID FROM USER WHERE NAME = %s'
                            data = (user,)
                            cur.execute(query, data)
                            fetchedID = cur.fetchone()
                            (ID,) = fetchedID
                            query = ' SELECT EXERCISES.`DIFFICULTY` FROM BOOKINGS INNER JOIN EXERCISES ON BOOKINGS.`EXERCISE NAME`=EXERCISES.`EXERCISE` WHERE `USER ID` = %s LIMIT 10'
                            data = (ID,)
                            cur.execute(query, data)
                            value = cur.fetchall()
                            rowsFetched = cur.rowcount
                            i = 0
                            for data in value:
                                (diff,) = data
                                i = i + diff
                            print('your difficulty level', (i/rowFetched) )
                            j = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                            if  j == 1:
                                continue;
                            else:
                                break;

                        i = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
                        if  i == 1:
                                continue;
                        else:
                                break;
def accCreation(user, passwo, pho):
    query = "INSERT INTO USER(`NAME`, `PHONE`, `PASSWORD`) VALUES(%s, %s, %s)"
    VALUES = (user, pho, passwo)
    cur.execute(query, VALUES)
    mycon.commit()
    return 'user created'


i = 1
while i == 1:
    print("1) LOG INTO AN EXISTING ACCOUNT")
    print("2) CREATE A NEW ACCOUNT")

    selection = int(input("select an option:"))

    if selection == 1:
        user = input('enter username : ')
        passwo = input('enter password for the corresponding username: ')
        authen(user, passwo)
        
    elif i == 2:
        user = input('create new username: ')
        passwo = input('enter password for the new account: ')
        pho = int(input("enter phone number to be associated to the account: "))
        j = accCreation(user, passwo, pho)
        i = int(input("ENTER 1 TO CONTINUE OR ANY OTHER NUMBER TO EXIT"))
        if i == 1:
            continue;
        else:
            break;
    else:
        print('thank you for thinking about yoga center')
        i = 2
            
