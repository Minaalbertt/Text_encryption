from tkinter import *
from tkinter import messagebox
import base64
import os



def decrypt():
    global text2
    def popup(event):
        rightmenu.tk_popup(event.x_root,event.y_root)

    def copy():
        text2.event_generate('<<Copy>>')

    def paste():
        text2.event_generate('<<Paste>>')

    def cut():
        text2.event_generate('<<Cut>>')


    def selectall():
        text2.event_generate('<<SelectAll>>')
    try:
        password = code.get()

        if password=="04112009":
            screen2=Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message=text1.get(1.0,END)
            decode_message = message.encode("ascii")
            base64_bytes=base64.b64decode(decode_message)
            decrypt=base64_bytes.decode("ascii")


            Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
            text2 = Text(screen2,font="Rpboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=380,height=150)

            text2.insert(END,decrypt)
            text2.bind('<Button-3>',popup)
        elif password == "":
            messagebox.showerror("Encryption","Input Password")
        elif password != "04112009":
            messagebox.showerror("Encryption","invalid Password")
        rightmenu = Menu(text2,tearoff=FALSE)
        rightmenu.add_command(label='Copy',accelerator='CTRL+C',command=copy)
        rightmenu.add_command(label='Cut',accelerator='CTRL+X',command=cut)
        rightmenu.add_command(label='Paste',accelerator='CTRL+V',command=paste)
        rightmenu.add_separator()
        rightmenu.add_command(label='Select All',accelerator='CTRL+A',command=selectall)
    except Exception:
        messagebox.showerror("Encryption","Error: could not decrypt")
def encrypt():
    global text2
    def popup(event):
        rightmenu.tk_popup(event.x_root,event.y_root)

    def copy():
        text2.event_generate('<<Copy>>')

    def paste():
        text2.event_generate('<<Paste>>')

    def cut():
        text2.event_generate('<<Cut>>')


    def selectall():
        text2.event_generate('<<SelectAll>>')
    try:
        password = code.get()

        if password=="04112009":
            screen1=Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")

            message=text1.get(1.0,END)
            encode_message = message.encode("ascii")
            base64_bytes=base64.b64encode(encode_message)
            encrypt=base64_bytes.decode("ascii")


            Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
            text2 = Text(screen1,font="Rpboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=380,height=150)

            text2.insert(END,encrypt)
            text2.bind('<Button-3>',popup)
        elif password == "":
            messagebox.showerror("Encryption","Input Password")
        elif password != "04112009":
            messagebox.showerror("Encryption","invalid Password")

        rightmenu = Menu(text2,tearoff=FALSE)
        rightmenu.add_command(label='Copy',accelerator='CTRL+C',command=copy)
        rightmenu.add_command(label='Cut',accelerator='CTRL+X',command=cut)
        rightmenu.add_command(label='Paste',accelerator='CTRL+V',command=paste)
        rightmenu.add_separator()
        rightmenu.add_command(label='Select All',accelerator='CTRL+A',command=selectall)
    except Exception:
        messagebox.showerror("Encryption","Error: could not encrypt")




def main_screen():
    
    global screen
    global code
    global text1
    def popup(event):
        rightmenu.tk_popup(event.x_root,event.y_root)

    def copy():
        text1.event_generate('<<Copy>>')

    def paste():
        text1.event_generate('<<Paste>>')

    def cut():
        text1.event_generate('<<Cut>>')


    def selectall():
        text1.event_generate('<<SelectAll>>')
    screen = Tk()
    screen.title("Text Encryption")
    screen.resizable(False,False)
    screen.geometry("375x398")
    
    def reset():
        code.set("")
        text1.delete(1.0,END)
        
    
    Label(text="Enter text for encryption and decryption",font=("calbri",13)).place(x=10,y=10)
    text1 = Text(font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    text1.bind('<Button-3>',popup)
    
    
    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)
    
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
    
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height=2,width=50,bg="#1089ff",bd=0,fg="white",command=reset).place(x=10,y=300)
    rightmenu = Menu(text1,tearoff=FALSE)
    rightmenu.add_command(label='Copy',accelerator='CTRL+C',command=copy)
    rightmenu.add_command(label='Cut',accelerator='CTRL+X',command=cut)
    rightmenu.add_command(label='Paste',accelerator='CTRL+V',command=paste)
    rightmenu.add_separator()
    rightmenu.add_command(label='Select All',accelerator='CTRL+A',command=selectall)
    screen.mainloop()


main_screen()