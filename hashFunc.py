from tkinter import *
from tkinter import messagebox
import os
import base64
import time
import hashlib

db_name = 'test.db'
table_name = 'users'

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
        messagebox.showinfo("LOGIN ERROR", "          THIS LOGIN ALREADY EXISTS        ")
    print(null)
    # ==========================================================================
    

def hash_func(password, login, time):
    qwe = len(login)

    obj = password 
    textUtf8 = obj.encode("utf-8")
    hash_object = hashlib.md5(textUtf8)
    place = hash_object.hexdigest()

    obj1 = place + login
    textUtf8 = obj1.encode("utf-8")
    hash_object1 = hashlib.md5(textUtf8)
    place1 = hash_object1.hexdigest()

    obj2 = place1 + time 
    textUtf8 = obj2.encode("utf-8")
    hash_object2 = hashlib.md5(textUtf8)
    place2 = hash_object2.hexdigest()

    obj3 = place2 + str(qwe)
    textUtf8 = obj3.encode("utf-8")
    hash_object3 = hashlib.md5(textUtf8)
    place3 = hash_object3.hexdigest()

    placeHash = place[0:20] + place1[10:30] + place2[4:20] + place3[10:20]

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
        return messagebox.showwarning("PASSWORD",        place        )
    else:
        return messagebox.showwarning("PASSWORD","""        SORRY, I DON'T KNOW YOU DUDE        """)

# =====================================================
def admin():
    win.destroy()

    master = Tk()

    master.title("Добро пожаловать в приложение ")
    master.config(bg = 'grey')
    master.geometry('500x500')
    master.resizable(0, 0)



    master.mainloop()

def user():
    global wuser
    global Username
    global password

    win.destroy()

    wuser = Tk()
    wuser.title("Добро пожаловать в приложение ")
    wuser.config(bg = 'grey')
    wuser.geometry('500x500')
    wuser.resizable(0, 0) 

    # Defining the first row
    lblfrstrow = Label(wuser, text ="Login -", )
    lblfrstrow.place(x = 170, y = 170)
     
    Username = Entry(wuser, width = 35)
    Username.place(x = 240, y = 170, width = 100)
      
    lblsecrow = Label(wuser, text ="Password -")
    lblsecrow.place(x = 170, y = 230)
     
    password = Entry(wuser, width = 35, show="*")
    password.place(x = 240, y = 230, width = 100)
     
    submitbtn = Button(wuser, text ="Login",
                          bg ='blue', command = submitact)
    submitbtn.place(x = 270, y = 270, width = 55)

    submitbtn = Button(wuser, text ="Register",
                          bg ='blue', command = register)
    submitbtn.place(x = 200, y = 270, width = 55)
    
    wuser.mainloop()

def register():

    wuser.destroy()

    global wregister
    global ssr_login
    global ssr_name
    global ssr_lname
    global ssr_psw
    global ssr_psw2

    wregister = Tk()
    wregister.title("Добро пожаловать в приложение ")
    wregister.config(bg = 'grey')
    wregister.geometry('500x500')
    wregister.resizable(0, 0) 

    lblfrstrow = Label(wregister, text ="Login -", )
    lblfrstrow.place(x = 20, y = 10)
     
    ssr_login = Entry(wregister, width = 35)
    ssr_login.place(x = 100, y = 10, width = 100)
    
    lblthrrow = Label(wregister, text ="Name -", )
    lblthrrow.place(x = 20, y = 50)
     
    ssr_name = Entry(wregister, width = 35)
    ssr_name.place(x = 100, y = 50, width = 100)
    
    lblfrrow = Label(wregister, text ="Lname -", )
    lblfrrow.place(x = 20, y = 90)
     
    ssr_lname = Entry(wregister, width = 35)
    ssr_lname.place(x = 100, y = 90, width = 100)
    
    lblsecrow = Label(wregister, text ="Password -")
    lblsecrow.place(x = 20, y = 130)
     
    ssr_psw = Entry(wregister, width = 35, show = "*")
    ssr_psw.place(x = 100, y = 130, width = 100)
    
    lblfirow = Label(wregister, text ="ReturnPass -")
    lblfirow.place(x = 20, y = 170)
     
    ssr_psw2 = Entry(wregister, width = 35, show = "*")
    ssr_psw2.place(x = 100, y = 170, width = 100)
    
    submitbtn = Button(wregister, text ="Register",
                          bg ='blue', command = insertRegister)
    submitbtn.place(x = 40, y = 210, width = 55)
    
    submitbtn = Button(wregister, text ="Back",
                          bg ='blue', command = user)
    submitbtn.place(x = 100, y = 210, width = 55)
    

    wregister.mainloop()

def insertRegister():
    scr_login = ssr_login.get()
    scr_name = ssr_name.get()
    scr_lname = ssr_lname.get()
    scr_psw = ssr_psw.get()
    scr_psw2 = ssr_psw2.get()

    if scr_psw == scr_psw2:
        scr_time = time.strftime("%X")
        scr_hash_psw = hash_func(scr_psw, scr_login, scr_time)

        result = insert_db(db_name, table_name, scr_login, scr_hash_psw, scr_name, scr_lname, 'A', scr_time)
        
        print(result)

        if result == None:
            messagebox.showinfo("LOGIN SUCCESSFULLY", "         REGISTRATION WAS SUCCESSFUL        ")

    elif scr_psw != scr_psw2:
        messagebox.showwarning("PASSWORD FAILED","        PLEASE TRY AGAIN PASSWORD        ")

def submitact():

    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")

    result = check_user(user, passw)
    print(result)

def main():
    global win

    win = Tk()

    win.title("Добро пожаловать в приложение ")
    win.config(bg = 'grey')
    win.geometry('500x500')
    win.resizable(0, 0)

    btn = Button(win, text="Admin", command=admin)
    btn.grid(column=1, row=0)
    btn.place(x=140, y=200, width = 100, height = 30)

    btn = Button(win, text="User",command=user)
    btn.grid(column=2, row=0)
    btn.place(x=260, y=200, width = 100, height = 30)

    win.mainloop()

main()
  
