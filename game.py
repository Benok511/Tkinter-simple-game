from tkinter import Tk,Canvas,Label
from random import randint
from datetime import datetime
from oval import Oval

'''
https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html

had to read into the tkinter canvas docs to find out how to clear it to find out about tags and how to use them to delete stuff

after quite a lot of buggy iterations and some research and you bringing it up in the lecture I decided to use .after instead
of sleep as it didnt freeze my program and make it sluggish.
https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep

also had to look up how to make variable global within a function
https://www.w3schools.com/python/python_variables_global.asp
'''
score = 0

oval = Oval()

def clickOval(event):
    global score
    if oval.onScreen:
        xpos = event.x
        ypos = event.y
        oval.end = datetime.now()
        if oval.inOval(xpos,ypos):
            
            print('Hit')
            label.config(text=f'Hit! time {oval.end - oval.start}')
            score += 1
            scoreLabel.config(text=f'Score: {score}')
        
        else:
            print('miss')
            label.config(text=f'Miss! time {oval.end - oval.start}')

        print(f'Time: {oval.end - oval.start}')
        canvas.delete('oval')
        oval.onScreen = False

    
    root.after(randint(1000,5000),drawOval)
    
    

def drawOval():
    
    if not oval.onScreen:
        oval.new_oval()
        canvas.create_oval(oval.x0,oval.y0,oval.x1,oval.y1,fill='blue',tags='oval') #setting a tag so its easy to delete with canvas.delete('oval')
    
    

root = Tk()
canvas = Canvas(root,bg='white',height=300,width=300)
label = Label(root,text='',font='Calibri 20')
scoreLabel = Label(root,text='Score: 0')
canvas.pack()
label.pack()
scoreLabel.pack()

canvas.bind("<Button-1>",clickOval)
drawOval()


root.mainloop()


    


