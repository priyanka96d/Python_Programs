import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image
import tkinter.ttk as tkk

top = tk.Tk()

pad=3
top._geom='200x200+0+0'
top.geometry("{0}x{1}+0+0".format(
top.winfo_screenwidth()-pad, top.winfo_screenheight()-pad))
top.title("TERM-PROJECT(NURSERY)")
top.configure(background='light blue')
top.resizable(False, False)
w=top.winfo_screenwidth()-pad
h=top.winfo_screenheight()-pad
print(w)
print(h)

canvas=Canvas(width=w,height=h-50,bg="blue")
canvas.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open('Webp.net-resizeimage.jpg'))
canvas.create_image(0,0,image=img,anchor=NW)

f = Frame(top,bg="yellow",width=1000,height=500)
f.place(x=200,y=80)
f.update()
    
logo = tk.PhotoImage(file="image3.gif")
    
L=Label(f,compound = tk.CENTER,text="Welcome to Priyanka's Gardening Shop,\n'we might think we are nurturing our garden but ofcourse its our garden that is really nurturing us'\n-Genny Uglow  ",image=logo,fg="yellow",font = "Helvetica 16 bold italic")
L.place(width=1000,height=120)


L1 = Label( f, text="Here you get full information of your plants according to the season",width=60,height=3,font = "Helvetica 16 bold italic",bg="light green")
L1.place(x=80,y=170)

combo1 = tkk.Combobox(f, values=["Season1", "Season2", "Season3"],width=60,height=60,state="readonly")
combo1.place(x=400,y=250)
combo1.current(0)

combo2 = tkk.Combobox(f, values=["Veggies", "Decorative plants", "Both"],width=60,height=5,state="readonly")
combo2.place(x=400,y=320)
combo2.current(0)

okay=Button(f,text="OKAY",fg="red",command=press_okay,width=10,height=1)
okay.place(x=400,y=390)

    
top.mainloop()




top.mainloop()
