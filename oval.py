from random import randint
import math
from datetime import datetime
class Oval:
    '''
        Class for an Oval x and y represent the center coords
        then x0,x1,y0,y1 represend 4 points on the circle to be used
        in the create_oval method in the main tk loop.
    '''

    def __init__(self):
        
        self._radius = randint(10,30)
        self._x = randint(10,250)
        self._y = randint(10,250)
        self._x0 = self._x - self._radius
        self._x1 = self._x + self._radius
        self._y0 = self._y - self._radius
        self._y1 = self._y + self._radius
        self._start = datetime.now()
        self._end = None
    '''
    getters for all vars
    '''
    @property
    def radius(self):
        return self._radius

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,x):
        if type(x) is not int:
            raise TypeError("x must be of type int")

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,y):
        if type(y) is not int:
            raise TypeError("y must be of type int")

    @property
    def x0(self):
        return self._x0
    @x0.setter
    def x0(self,x0):
        if type(x0) is not int:
            raise TypeError("x0 must be of type int")
    

    @property
    def y0(self):
        return self._y0
    @y0.setter
    def y0(self,y0):
        if type(y0) is not int:
            raise TypeError("y0 must be of type int")

    @property
    def x1(self):
        return self._x1
    @x1.setter
    def x1(self,x1):
        if type(x1) is not int:
            raise TypeError("x1 must be of type int")

    @property
    def y1(self):
        return self._y1
    
    @y1.setter
    def y1(self,y1):
        if type(y1) is not int:
            raise TypeError("y1 must be of type int")
    
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self,time):
        if type(time) is not datetime and time is not None:
            raise TypeError("start must be of type datetime")
        self._start = time
    
    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self,time):
        if type(time) is not datetime and time is not None:
            raise TypeError("end must be of type datetime")

        self._end = time
        
    
    def new_oval(self):
        '''
        Method to create 'new' oval
        re-assigns all vars to new ones
        easier to manage 
        '''
        self.radius = randint(10,30)
        self.x = randint(10,250)
        self.y = randint(10,250)
        self.x0 = self.x - self.radius
        self.x1 = self.x + self.radius
        self.y0 = self.y - self.radius
        self.y1 = self.y + self.radius
        self.start = datetime.now()
        self.end = None


    def inOval(self,x,y):
        distance = math.dist((x,y),(self.x,self.y))
        if distance <= self.radius:
            return True
        
        return False
    

        

    

