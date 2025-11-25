from tkinter import Tk,Canvas,Label
from random import randint
from datetime import datetime
from oval import Oval
from gamemanager import GameManager

'''
https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html

had to read into the tkinter canvas docs to find out how to clear it to find out about tags and how to use them to delete stuff

after quite a lot of buggy iterations and some research and you bringing it up in the lecture I decided to use .after instead
of sleep as it didnt freeze my program and make it sluggish.
https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep

i used objects to sort of act like global variables for the GameManager class
'''

manager = GameManager()
oval = Oval()

def clickOval(event):
    # check if game has started if not set it to started and then call the first wait for oval
    if manager.started:
        
        # if theres a click and its on screen then check if its been clicked print the time
        # and then call the next oval to be drawn
        if oval.onScreen:
            xpos = event.x
            ypos = event.y
            oval.end = datetime.now()
            if oval.inOval(xpos,ypos):
                
                print('Hit')
                label.config(text=f'Hit! time {oval.end - oval.start}')
                manager.score += 1
                scoreLabel.config(text=f'Score: {manager.score}')
            
            else:
                print('miss')
                label.config(text=f'Miss! time {oval.end - oval.start}')

            print(f'Time: {oval.end - oval.start}')
            canvas.delete('oval')
            oval.onScreen = False
            root.after(randint(1000,5000),drawOval)
        

    else:
        manager.started = True
        root.after(randint(1000,5000),drawOval)

    
    
    
    

def drawOval():
    
    if not oval.onScreen:
        oval.new_oval()
        canvas.create_oval(oval.x0,oval.y0,oval.x1,oval.y1,fill='blue',tags='oval') #setting a tag so its easy to delete with canvas.delete('oval')
        oval.onScreen = True
    

root = Tk()
canvas = Canvas(root,bg='white',height=300,width=300)
label = Label(root,text='',font='Calibri 20')
scoreLabel = Label(root,text='Score: 0')
canvas.pack()
label.pack()
scoreLabel.pack()

canvas.bind("<Button-1>",clickOval)



root.mainloop()


    


