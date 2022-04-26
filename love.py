import mysql.connector as c 
from tkinter import *
from PIL import ImageTk, Image
window = Tk()

conn = c.connect(host = "localhost", user = "root", passwd = "Hsjaiswal.3110#", database = "pythondb")

mycursor = conn.cursor()

# table = "CREATE TABLE love (name VARCHAR(255), partner_name VARCHAR(255), gender VARCHAR(255), result INT)"
# mycursor.execute(table)
window.configure(background="pink")

yourName = StringVar()
partnerName = StringVar()
Gender = StringVar()
window.title("LOVE 💖 & FRIENDSHIP 🤗 CALCULATOR")

def break_line():
    return Label(text="\n").pack()

def calculate():
    name = yourName.get()
    pname = partnerName.get()
    gender = Gender.get()

    #CHECKING THE GENDER                   
    if(gender == "same"):
        Label(text="Friendship").pack()
        Label(text= f"{name} 🤗 {pname}").pack()
        gender = "same"
    else:
        Label(text="Love").pack()
        Label(text= f"{name} ❤ {pname}").pack()
        gender = "different"

    score = 0  
    vowels=["a","e","i","o","u"]  

    #BOTH FIRST NAME HAVE THE SAME NUMBER OF VALUES
    if len(name) == len(pname):
        score += 30

    #BOTH FIRST NAME STARTS WITH VOVELS OR CONSONENTS
    if ((name[0] in vowels) and (pname[0] in vowels)) or ((name[0] not in vowels) and (pname[0] not in vowels)):
        score += 15

    #BOTH FIRST NAME HAVE THE SAME NUMBER OF VOVELS
    vname = 0
    for i in name:
        if(i in vowels):
            vname += 1
    vpname = 0
    for i in pname:
        if(i in vowels):
            vpname += 1
    if (vpname == vname):
        score += 20

    #BOTH NAME HAVE AT LEAST ONE VOVELS
    no_of_vovel_name = 0
    for i in name:
        if(i in vowels):
            no_of_vovel_name = 1
            break
    
    no_of_vovel_pname = 0
    for i in pname:
        if(i in vowels):
            no_of_vovel_pname = 1
            break
    if(no_of_vovel_pname == 1 and no_of_vovel_name ==1):
        score +=15

    #CHECKING THE LAST CHARACTER OF NAME
    if(name[len(name)-1]== pname[len(pname)-1]):
        score +=20
    
    Label(text=f"{score}%").pack()
    
    sql = "INSERT INTO love (name, partner_name, gender, result) VALUES (%s, %s, %s, %s)"
    val = (name, pname, gender, score)

    mycursor.execute(sql, val)
    conn.commit()

bg =ImageTk.PhotoImage(Image.open("E:\\python\\project\\love_calculator\\bg.jpg"))

pic = Label(window, image=bg).place(x=0,y=0)
heading = Label(text="Calculate your love/friendship with your partner\n", foreground="red", background="pink", font=("Arial",14)).pack(pady=20)
your_name = Label(text="Enter your name ", foreground="red", background="pink", font=("Arial",14)).pack()
entry_your_name = Entry(window, textvariable=yourName).pack()
break_line()
partner_name = Label(text="Enter partner name ", foreground="red", background="pink", font=("Arial",14)).pack()
entry_partner_name = Entry(window, textvariable=partnerName).pack()
break_line()
same_gender = Radiobutton(window, text = "Both are of same gender", variable=Gender, value="same", foreground="red", background="pink").pack()
diff_gender = Radiobutton(window, text = "Both are of diff gender", variable=Gender, value="different", foreground="red", background="pink").pack()
break_line()
btn = Button(text="Calculate", command= calculate, foreground="pink", background="red" ).pack()
break_line()
note = Label(window, text="This is only for fun. Don't take it seriously").pack()

window.mainloop()
