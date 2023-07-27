"""
SET:B

Write a GUI program for a  four function calculator. At the minimum GUI contains-
3 labels, 3 text boxes for 2 inputs and one output, 4 radio buttons for add, substract,
multiply and divide and two command buttons for ‘Calculate’ and ‘Reset’.
The calculator inputs are integers only. Upload source code and screen shots. 
"""

from tkinter import *
def main():
    
    top=Tk()
    top.title("Final Exam-SET B")
    top.resizable(False,False)
    def reset_value( ):
        value_1.set(" ") 
        value_2.set(" ")
        output.set(" ")
    def operation():
        """Performing operation - Add,Sub,Mul,Div."""
        selection = str(var.get())
        
        num1=int(value_1.get())
        num2=int(value_2.get())
        
        if selection =="add":
           
           result=num1+num2
           output.set(result)
        if selection == "sub":
            result=(num1)-(num2)
            output.set(result)
        if selection=="mul":
            result=(num1)*(num2)
            output.set(result)
        if selection=="div":
            result=(num1)/(num2)
            output.set(result)
            
       

    """Using StringVar() class to entry widgets to track changes to the entered value"""
    value_1=StringVar()
    value_2=StringVar()
    output=StringVar()
    var=StringVar()
    cal=StringVar()

    """Add Labels to window  """
    L1 = Label( top, text="Enter First Number")
    L1.grid(row=0,column=0,padx=5,pady=5,sticky=W+N)
    L2 = Label( top, text="Enter Second number")
    L2.grid(row=1,column=0,padx=5,pady=5,sticky=W+N)
    L3 = Label( top, text="Output")
    L3.grid(row=2,column=0,padx=5,pady=5,sticky=W+N)

    """The Entry widget used to enter text from user and display output"""
    E1 = Entry( top, bd =5,textvariable= value_1)
    E1.grid(row=0,column=1,padx=5,pady=5,sticky=N+E)
    E2 = Entry( top, bd =5,textvariable= value_2)
    E2.grid(row=1,column=1,padx=5,pady=5,sticky=N+E)
    E3 = Entry( top, bd =5,textvariable= output)
    E3.grid(row=2,column=1,padx=5,pady=5,sticky=N+E)


    L4 = Label( top, text="select radio button for performing the operation you want.")
    L4.grid(row=4,column=0,padx=5,pady=5,sticky=W+N)

    """Radio Button."""
    R1 = Radiobutton(top, text="Add", variable=var, value="add")
    R1.grid(row=4,column=1,padx=5,pady=5)

    R2 = Radiobutton(top, text="Substract", variable=var, value="sub")
    R2.grid(row=5,column=1,padx=5,pady=5)

    R3 = Radiobutton(top, text="Multiply", variable=var, value="mul")
    R3.grid(row=6,column=1,padx=5,pady=5)

    R4 = Radiobutton(top, text="Divide", variable=var, value="div")
    R4.grid(row=7,column=1,padx=5,pady=5)
    
    """Button, call operation function for performing user's operation."""
    calculate=Button( top, text="calculate", fg="Green",width="12",command=operation)
    calculate.grid(row=8,column=1,padx=5,pady=5,sticky = S+E)
    
    """Button for reset values from all entry widget so that new set of data would enter """
    reset=Button( top, text="Reset", fg="red",width="12",command=reset_value)
    reset.grid(row=8,column=0,padx=5,pady=5,sticky = S+W)

    top.mainloop()
if __name__ == "__main__":
    main()

