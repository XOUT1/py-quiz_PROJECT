#import the packages

from tkinter import *
import questions


#defining the varibale for users current questions attempted

current_question = 0


#main face

if __name__ == '__main__':
    root = Tk()
    #basic window p31
    root.title("QUIZ APP")
    root.geometry("950x500")
    
#baground image
bg_img = PhotoImage(file= "Q-app/img/bg1.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
                 height = 400)
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg_img, 
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 200, 200, text = "WELCOME", font=('Helvetica','30','bold'))

# Create Buttons
button1 = Button( root, text = "start quiz",font="calibre 17 bold")


# Display Buttons
button1_canvas = canvas1.create_window( 200, 280, 
                                       anchor = "nw",
                                       window = button1)









root.mainloop()
