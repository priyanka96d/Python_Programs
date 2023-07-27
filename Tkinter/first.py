import tkinter as tk
import tkinter as tk1
from tkinter import *
import tkinter.ttk as tkk
from pymongo import MongoClient
import csv



"""---Establish connection between momgodb and python-----"""
client=MongoClient('mongodb://localhost:27017')
db=client['veggie-database']
print(db)
"""----Creating Collection------"""
s1_veggies=db.s1_veggies
s1_plants=db.s1_plants
print("collection: ",s1_plants)
"""-----Creates Inserted data to be--------- """
s1_v_data = [
      { "_id":1,"veg_name": "tomatoes", "price": "$37"},
      { "_id":2,"veg_name": "chilli", "price": "$27"},
      { "_id":3,"veg_name": "okra", "price": "$2"},
      { "_id":4,"veg_name": "egg-plant", "price": "$21"},
      { "_id":5,"veg_name": "beans", "price": "$5"},
      { "_id":6,"veg_name": "oregeno", "price": "$2"},
      { "_id":7,"veg_name": "basil", "price": "$1"},
      { "_id":8,"veg_name": "cilantro", "price": "$31"},
  
    ]
s1_p_data=[{"_id":1,"plant_name": "Rose", "price": "$37"},
           {"_id":2,"plant_name": "Lily", "price": "$39"}]
        
data_price=[]
data_vegname=[]
"""---Inserted data in Collection----"""
#result=s1_veggies.insert_many(s1_v_data)
#print(result.inserted_ids)
#result=s1_plants.insert_many(s1_p_data)
data_all=[]

"""-----Creating CSV file to storing fetched data from collection-------"""
header = ['Index','Name', 'Price']

with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
    for index in s1_veggies.find():
        writer.writerow([str(index['_id']),str(index['veg_name']),str(index['price'])])


output_vegname = [] 
output_price=[]
output_index=[]
f = open( 'test.csv', 'r' ) #open the file in read universal mode
for line in f:
    cells = line.split( "," )
    output_vegname.append(cells[ 1 ]) #since we want the first, second and third column
    output_price.append(cells[2])
    output_index.append(cells[0])
f.close()
print(output_vegname)
for index in output_vegname:
    print(index)

def op_1():
    
    print("----------------------------")
    data=LB1.get(First,last=none)
    print(data)

def operation():
    print("under operation function")
    data=str(combo.get())
    for index in s1_veggies.find({"veg_name":data}):
            
        data=str(index['veg_name'])
        data_price=str(index['price'])
            
        data=data.replace('[',' ')
        data=data.replace(']',' ')
            #data=data.strip(',')
            
        LB1 = Listbox(root,height=4,bg='green')
        LB1.insert(1,data)
        LB1.insert(2,data_price)
        LB1.place(x=50,y=150)
            
            
        okay=Button(root,text="Done",width=10,height=1,command=op_1)
        okay.place(x=50,y=250)
            
            

root = tk.Tk()
root.geometry("400x300")
var = StringVar()
var1=StringVar()
combo=ttk.Combobox(root,values=output_vegname,state="readonly",width=30)
combo.place(x=50,y=50)
combo.current(1)

done=Button(root,text="Proceed",width=10,height=1,command=operation)
done.place(x=100,y=100)

root.mainloop()
"""----------------------------------------------------------------------------------------------------------------------------------"""
def press_okay():
        data_com1=str(combo.get())
        print("data is:",data_com1)

        data_com2=str(combo1.get())
        print("data of second combox is:",data_com2)
#season1 data
        if combo.get()=="Season1" and combo1.get()=="Veggies":
            print("you selected veggies from season1")
            #call_db(season1,veggies)
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season1-veggies data")
            

        if combo.get()=="Season1" and combo1.get()=="Decorative plants":
            print("you selected Decorative plants from season1")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season1-Decorative plants data")
            

        if combo.get()=="Season1" and combo1.get()=="Both":
            print("you selected veggies and Decorative plants from season1")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season1-veggies and Decorative plants data")
            
#season2 data
        if combo.get()=="Season2" and combo1.get()=="Veggies":
            print("you selected veggies from season2")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season2-veggies data")
            

        if combo.get()=="Season2" and combo1.get()=="Decorative plants":
            print("you selected Decorative plants from season2")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season2-Decorative plants data")
            

        if combo.get()=="Season2" and combo1.get()=="Both":
            print("you selected veggies and Decorative plants from season2")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season2-veggies and Decorative plants data")
            
# season3 data
        if combo.get()=="Season3" and combo1.get()=="Veggies":
            print("you selected veggies from season3")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season3-veggies data")
            

        if combo.get()=="Season3" and combo1.get()=="Decorative plants":
            print("you selected Decorative plants from season3")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season3-Decorative plants data")
            

        if combo.get()=="Season3" and combo1.get()=="Both":
            print("you selected veggies and Decorative plants from season3")
            window = tk.Toplevel(top)
            window.geometry("400x300")
            window.title("Season3-veggies and Decorative plants data")
            


top = Tk()

pad=3
top._geom='200x200+0+0'
top.geometry("{0}x{1}+0+0".format(
top.winfo_screenwidth()-pad, top.winfo_screenheight()-pad))
top.title("Final Exam-SET B")
top.configure(background='light blue')
top.resizable(False, False)
        
f = Frame(top,bg="yellow",width=1000,height=500)
f.place(x=200,y=80)
f.update()
    
logo = tk.PhotoImage(file="image1.gif")
    
L=Label(f,compound = tk.CENTER,text="Welcome to Gardening Shop, Here you get full information of your plants according to the season  ",image=logo,font = "Helvetica 16 bold italic")
L.place(width=1000,height=120)
    
L1 = Label( f, text="Click below buttons to select the season:",width=60,height=3,font = "Helvetica 16 bold italic",bg="blue")
L1.place(x=80,y=170)

combo = tkk.Combobox(f, values=["Season1", "Season2", "Season3"],width=60,height=60,state="readonly")
combo.place(x=400,y=250)
combo.current(0)

combo1 = tkk.Combobox(f, values=["Veggies", "Decorative plants", "Both"],width=60,height=5,state="readonly")
combo1.place(x=400,y=320)
combo1.current(0)

okay=Button(f,text="OKAY",fg="red",command=press_okay,width=10,height=1)
okay.place(x=400,y=390)

    
top.mainloop()
main()
