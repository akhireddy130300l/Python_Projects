import wikipedia
from tkinter import *
from tkinter.messagebox import *
def question_answer():
    question=e1.get()
    answer=wikipedia.summary(question)
    showinfo("answer",answer)
    print(answer)
root=Tk()
root.geometry("400x100")
question=StringVar()
e1=Entry(root,width=50,textvariable=question)
e1.grid(row=1,column=1,padx=20)
b1=Button(root,width=12,command=question_answer)
b1.grid(row=3,column=3)
root.mainloop()
