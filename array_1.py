from tkinter import *
import random
root=Tk()

root.title("Multidimensonal array")
root.geometry("500x500")
root.configure(background="Yellow")

label_1 = Label(root)

array_3D = [
    [
        ['1','2','3','4','5','6'],
        ['Head','Tail'],
        ['A','B','C','D','E','F','G','H']
    ]
]
#print(array_3D[0][2][4])

def password():
    r1=random.randint(0,5)
    r2=random.randint(0,1)
    r3=random.randint(0,7)

    letter1 = str(array_3D([0][0][r1]))
    letter2 = array_3D([0][1][r2])
    letter3 = array_3D([0][2][r3])

    label_1 ["text"] = letter1 + "" + letter2 + "" + letter3



btn = Button(root,text="New Password",bg="Light green",fg="Red",command=password)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

label_1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()