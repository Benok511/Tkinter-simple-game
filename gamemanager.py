
class GameManager:
    '''
    class to manage the variable with the game state - score and if the game has started
    '''


    def __init__(self):
        self._score = 0
        self._started = False

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if type(score) is not int:
            raise TypeError('score must be an int')
        if score < 0:
            raise ValueError('Type must be non negative')
        
        self._score = score

    @property
    def started(self):
        return self._started
    
    @started.setter
    def started(self,started):
        if type(started) is not bool:
            raise TypeError('started must be a bool')
        
        self._started = started

    