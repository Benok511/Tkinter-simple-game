from tkinter import Tk,Canvas
from random import randint
from datetime import datetime
from time import sleep
from oval import Oval

'''
https://www.w3schools.com/python/python_variables_global.asp
https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html

had to look up how to make variable global as I didnt know!
also had to read into the tkinter canvas docs to find out how to clear it
'''

start = 0
end = 0
oval = Oval()

def clickOval(event):
    global start
    global end
    xpos = event.x
    ypos = event.y
    end = datetime.now()
    if oval.inOval(xpos,ypos):
        
        print('Hit')
    
    else:
        print('miss')

    print(f'Time: {end - start}')
    end = 0
    start = 0
    canvas.delete('oval')
    drawOval()
    
    

def drawOval():
    sleep(randint(5,10))
    global start
    oval.new_oval()
    canvas.create_oval(oval.x0,oval.y0,oval.x1,oval.y1,fill='blue',tags='oval') #setting a tag so its easy to delete with canvas.delete('oval')
    start = datetime.now()
    

root = Tk()
canvas = Canvas(root,bg='white',height=300,width=300)
canvas.pack()

canvas.bind("<Button-1>",clickOval)
drawOval()






root.mainloop()


    


