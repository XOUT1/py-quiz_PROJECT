#import the packages

from tkinter import *


question = {
    "Who developed Python Programming Language?": ['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum', 'Niene Stom'],
    "Which type of Programming does Python support?": ['object-oriented programming', 'structured programming', 'functional programming', 'all of the mentioned'],
    "Is Python case sensitive when dealing with identifiers?": ['no', 'yes', 'machine dependent', 'none of the mentioned'],
    "Which of the following is the correct extension of the Python file?": ['.python', '.pl', '.py', '.p']
}

ans = ['Guido van Rossum', 'all of the mentioned', 'yes' , '.py']

#defining the varibale for users current questions attempted

current_question = 0


#main face

if __name__ == '__main__':
    root = Tk()
    #basic window p31
    root.title("QUIZ APP")
    root.geometry("800x500")
    root.config(background='#00fff2')
    

    

welcome = Label(root,text="WELCOME",
                font=('Arial',40,'bold'),
                fg="black",
                bg="#00fff2")

welcome.pack()




def start_quiz():
    button1.forget()
    button2.pack()
    next_question()
    
def next_question():
    global current_question
    if current_question < len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        #clear frame to update the next question
        clear_frame()
        #print questions ig it will work :)
        Label(f1, text=f"Question  :  {c_question}", padx=15,
              font="Arial",bg='#00fff2').pack(anchor=NW)
        #print options
        for option in question[c_question]:
            Radiobutton(f1, text=option,
                        variable=user_ans,
                        value=option,padx=29,bg='#00fff2').pack(anchor=NW)
        current_question += 1
    else:
        button2.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 25 bold",bg='#00fff2').pack(padx=0,pady=50)
        Label(f1, text="Thanks for Participating!",
              font="calibre 18 bold",bg='#00fff2').pack()
        
def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        #set user score
        user_score.set(user_score.get()+1)
        
def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()
        



# Create Buttons
button1 = Button( root, text = "start quiz",
                 font="calibre 17 bold",
                 fg="#f7f7f7",
                 background="black",
                 activeforeground="#f7f7f7",
                 activebackground="black",
                 command=start_quiz)

button1.pack(padx=0,pady=190)

f1 = Frame(root)
f1.pack(side=TOP, fill=X,)

button2 = Button(root, text= "NEXT QUESTION",
                 font="calibre 17 bold",
                 command=next_question)


user_ans = StringVar()
user_ans.set('None')
user_score = IntVar()
user_score.set(0)










root.mainloop()
