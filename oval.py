from random import randint
import math
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

    '''
    getters for all vars
    '''
    @property
    def radius(self):
        return self._radius

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def x0(self):
        return self._x0

    @property
    def y0(self):
        return self._y0

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1
    
    def new_oval(self):
        '''
        Method to create 'new' oval
        re-assigns all vars to new ones
        easier to manage 
        '''
        self._radius = randint(10,30)
        self._x = randint(10,250)
        self._y = randint(10,250)
        self._x0 = self._x - self._radius
        self._x1 = self._x + self._radius
        self._y0 = self._y - self._radius
        self._y1 = self._y + self._radius


    def inOval(self,x,y):
        distance = math.dist((x,y),(self.x,self.y))
        if distance <= self.radius:
            return True
        
        return False
    

        

    

