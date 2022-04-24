from tkinter import *

window = Tk()

window.geometry("500x650")
window.configure(background="pink")

yourName = StringVar()
partnerName = StringVar()
Gender = StringVar()
window.title("LOVE 💖 & FRIENDSHIP 🤗 CALCULATOR")

def break_line():
    return Label(text="\n", background="pink").pack()

def calculate():
    name = yourName.get()
    pname = partnerName.get()
    gender = Gender.get()
    Label(text=gender).pack()

    #CHECKING THE GENDER                   
    if(gender == "same"):
        Label(text= f"{name} 🤗 {pname}").pack()
    else:
        Label(text= f"{name} ❤ {pname}").pack()

    score = 0  
    vowels=["a","e","i","o","u"]  
    vowels_name=0  
    vowels_pname=0

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
    

heading = Label(text="Calculate your love/friendship with your partner\n", foreground="red", background="pink", font=("Arial",14)).pack()
your_name = Label(text="Enter your name ", foreground="red", background="pink", font=("Arial",14)).pack()
entry_your_name = Entry(window, textvariable=yourName).pack()
break_line()
partner_name = Label(text="Enter partner name ", foreground="red", background="pink", font=("Arial",14)).pack()
entry_partner_name = Entry(window, textvariable=partnerName).pack()
break_line()
same_gender = Radiobutton(window, text = "Both are of same gender", variable=Gender, value="same").pack()
diff_gender = Radiobutton(window, text = "Both are of diff gender", variable=Gender, value="different").pack()
break_line()
btn = Button(text="Calculate", command= calculate ).pack()
window.mainloop()
