
from tkinter import *
def main():
    def dectobin(n):
         binary=[]
         while n > 0 :
            
            binary.append(n%2)
            n = n//2
        
        
         return binary
        
    def calculate():
        decimal = user_value.get()
        decimal=int(decimal)

        O_val=oct(decimal).replace("0o","")
        value_octal.set(O_val)
        
        #bval=bin(decimal).replace("0b","")
        #value_Binary.set(bval)
        bval=dectobin(decimal)
    
        
        value_Binary.set(bval)

        h_val=hex(decimal).replace("0x","")
        value_hexa.set(h_val)
    def reset_value():
        user_value.set(0)
        value_octal.set(" ")
        value_Binary.set(" ")
        value_hexa.set(" ")

    top = Tk()
    
    top.title("coversion")
    
    user_input = Label( top, text="Enter your input  ")
    user_input.grid(row=0,column=0,padx=5,pady=5,sticky=W+N)
    
    L1 = Label( top, text="3 digit Decimal to Octal  ")
    L1.grid(row=1,column=0,padx=5,pady=5,sticky=W+N)
    L2 = Label( top, text="3 digit Decimal to Binary   ")
    L2.grid(row=2,column=0,padx=10,pady=10,sticky=S+W)
    L3 = Label( top, text="3 digit Decimal to Hexadecimal   ")
    L3.grid(row=3,column=0,padx=10,pady=10,sticky=S+W)

    user_value=StringVar()
    value = Entry( top, bd =5,textvariable=user_value)
    value.grid(row=0,column=1,padx=5,pady=5,sticky=N+E)
    
    value_octal = StringVar()
    E1 = Entry( top, bd =5,textvariable= value_octal)
    E1.grid(row=1,column=1,padx=5,pady=5,sticky=N+E)

    value_Binary=StringVar()
    E2 = Entry( top, bd =5,textvariable= value_Binary)
    E2.grid(row=2,column=1,padx=5,pady=5,sticky=S+E)

    value_hexa=StringVar()
    E3 = Entry( top, bd =5,textvariable= value_hexa)
    E3.grid(row=3,column=1,padx=5,pady=5,sticky=S+E)

    reset=Button( top, text="Reset", fg="red",width="12",command=reset_value)
    reset.grid(row=4,column=0,padx=5,pady=5,sticky = S+W)

    convert=Button( top, text="calculate", fg="Green",width="12",command=calculate)
    convert.grid(row=4,column=1,padx=5,pady=5,sticky = S+E)
    top.mainloop()    
  
main()
