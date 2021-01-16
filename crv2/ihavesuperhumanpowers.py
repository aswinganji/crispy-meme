from tkinter import*

root = Tk()
root.geometry("600x600")
root.title("TitleUsed413thtime")
from PIL import ImageTk,Image


inputy = Entry(root)

imagey = ImageTk.PhotoImage(Image.open("superpandapowers.jpg"))

def defy():
    try:
        croma= int(inputy.get())
        messagebox.showinfo("UNallowed(Opposite meaning)","Error day has not come back")
        
    except(ValueError):
        print("Error day has come back")
        messagebox.showinfo("Error","Error day has come back")
        
B2 = Button(root,image = imagey)
supwrbutton = Button(root,text="Text235timesused",command = defy)

inputy.pack()
supwrbutton.pack()
B2.pack()
root.mainloop()
