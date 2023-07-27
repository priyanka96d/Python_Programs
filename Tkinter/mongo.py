from pymongo import MongoClient
import csv
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import *



client=MongoClient('mongodb://localhost:27017')
db=client['Term_Project']
print(db)

s1_veggies=db.s1_veggies
s1_plants=db.s1_plants
print("collection: ",s1_plants)

s1_v_data = [
  { "_id":1,"name": "tomatoes", "price": "$37"},
  { "_id":2,"name": "chilli", "price": "$27"},
  { "_id":3,"name": "okra", "price": "$2"},
  { "_id":4,"name": "egg-plant", "price": "$21"},
  { "_id":5,"name": "beans", "price": "$5"},
  { "_id":6,"name": "oregeno", "price": "$2"},
  { "_id":7,"name": "basil", "price": "$1"},
  { "_id":8,"name": "cilantro", "price": "$31"},
  
]
s1_p_data=[{"_id":1,"plant_name": "Rose", "price": "$37"},
           {"_id":2,"plant_name": "Lily", "price": "$39"}]
        
data_price=[]
data_vegname=[]
result=s1_veggies.insert_many(s1_v_data)
#print(result.inserted_ids)
result=s1_plants.insert_many(s1_p_data)
data_all=[]


header = ['Index','Name', 'Price']

with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
    for index in s1_veggies.find():
        writer.writerow([str(index['_id']),str(index['name']),str(index['price'])])


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
print("----------------------",output_vegname)
for index in output_vegname:
    print(index)

def op_1():
    
    print("----------------------------")
    data=LB1.get(First,last=none)
    print(data)

def operation():
    print("under operation function")
    data=str(combo.get())
    for index in s1_veggies.find({"name":data}):
            data=str(index['name'])
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
"""



for obj in s1_veggies.find():
    
    data_price.append(obj["price"])
print("price        ",data_price)


for obj in s1_veggies.find():
    data_vegname.append(obj['name'])
print("veg name: ",data_vegname)

str1 = ",".join(data_vegname)
print("string  :",str1)
for index in str1.split(","):
                                  
    print(index)



root = tk.Tk()
root.geometry("400x300")




with open('veg.txt', 'w') as data:
    
    for index in s1_veggies.find():
        #writer = write.writer(data)
        
        data.write(str(index['_id']))
        data.write("\t")
        data.write(str(index['name']))
        data.write("    \t")
        data.write(str(index['price']))
        data.write("\n")


x = PrettyTable()
i=0
x.field_names = ["Id", "Veg-Name", "Price"]
for index in s1_veggies.find({},{'_id':1,'name':1,'price':1}):
    x.add_row([index["_id"],index["name"],index["price"]])
    
l=Label(root,text=x)
l.grid(row=0,column=0)
print(x)

tk.mainloop()
"""
    


