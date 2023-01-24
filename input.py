from tkinter import *
root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

enter_num = Entry(root)

label1 = Label(root,text="Fibonacci Series: ")
label2 = Label(root,text="Fibonacci Sum: ")

def fibonacci():
    input_num = int(enter_num.get())
    
    first_num = 0
    second_num = 1
    sum = 0
    counter = 1
    sum2 = 0
    
    while counter<=input_num:
        label1["text"]+=str(sum)+" "
        label2["text"]="Fibonacci Sum: "+str(sum2)
        counter = counter+1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
        
        sum2 = sum2+sum
        
enter_num.pack()
btn = Button(root,text="Show Fibonacci Series",command=fibonacci,bg="black",fg="white")
btn.pack()
label1.pack()
label2.pack()


root.mainloop()