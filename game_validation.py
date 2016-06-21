class GameState(object):

    def __init__(self, board):



""""

class Validator(GameState):

    def __init__(self, piece, origin, dest):
        GameState.__init__(self)
        
        self.board = board
        self.origin = origin
        self.dest = dest

    def test():
        print 'hi'

    def process_move(self, origin, dest):

        calculated_move = tuple(abs(numpy.subtract(dest, origin)))
        if calculated_move == (2, 1) or calculated_move == (1, 2):
            print calculated_move
            return True
        else:
            print calculated_move
            return False


Validator('test')

""""