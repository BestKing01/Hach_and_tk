import hashFunc

def hash_func(password, login, time):
    import hashlib

    qwe = len(login)
    
    obj = password 
    hash_object = hashlib.md5(b'obj')
    place = hash_object.hexdigest()
    
    obj1 = place + login
    hash_object1 = hashlib.md5(b'obj1')
    place1 = hash_object1.hexdigest()

    obj2 = place1 + time 
    hash_object2 = hashlib.md5(b'obj2')
    place2 = hash_object2.hexdigest()

    obj3 = place2 + str(qwe) 
    hash_object3 = hashlib.md5(b'obj3')
    place3 = hash_object3.hexdigest()
    
    placeHash = place[0:5] + place1[2:6] + place2[3:8] + place3[2:5]

    return placeHash

def check_user(login, password):
    import sqlite3  

    db_name = 'test.db'
    table_name = 'users'

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    check_query = ('SELECT * FROM ' + table_name + ' WHERE login = \"' + login + "\"")
    cursor.execute(check_query)
    place = cursor.fetchone()

    time_place = place[5]
    psw_place = place[1]
    lgn_place = place[0]

    conn.close()

    a = hash_func(password, login, time_place)

    if a == psw_place and login == lgn_place:
        return place
    else:
        print("Error")


def insert_db(db_name, table_name, login, password, name, surname, status, time_bd):
    result = '?????'
    import sqlite3
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    create_query = (
                'INSERT INTO ' + table_name + ' (login, password, name, surname, status, time_bd) VALUES (\'' + login + '\', \'' + password + '\', \'' + name + '\', \'' + surname + '\', \'' + status + '\', \'' + time_bd + '\');')
    try:
        cursor.execute(create_query)
        conn.commit()
    except sqlite3.Error as er:
        print(er)
    # ==========================================================================
    


choice = input(" To sign up: 1  \n To sign in: 2\n")
if choice == '1':
    import getpass

    scr_lgn = input("Login: ")
    scr_name = input("Name: ")
    scr_lname = input("Lname: ")
    scr_psw = getpass.getpass("Password: ")
    scr_psw2 = getpass.getpass("Return Password: ")

    db_name = 'test.db'
    table_name = 'users'

    if scr_psw == scr_psw2:
        import time

        scr_time = time.strftime("%X")
        scr_hash_psw = hash_func(scr_psw, scr_lgn, scr_time)

        result = insert_db(db_name, table_name, scr_lgn, scr_hash_psw, scr_name, scr_lname, 'A', scr_time)
        print(result)

    elif scr_psw != scr_psw2:
        print("Passwords don't coincidence")


elif choice == '2':
    import getpass

    login = input("Login: ")
    password = getpass.getpass("Password: ")

    result = check_user(login, password)

    print(result)

else:
    print("Error:try again!")
