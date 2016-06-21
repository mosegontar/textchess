class Piece(object):

    def __init__(self):
        pass

    def check_legal(self, origin, dest, *rules, backwards=False):

        calculated_move = tuple(abs(numpy.subtract(dest, origin)))
        


class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):

    def __init__(self):


    def knight_test(self, origin, dest):

        calculated_move = tuple(abs(numpy.subtract(dest, origin)))
        if calculated_move == (2, 1) or calculated_move == (1, 2):
            print calculated_move
            return True
        else:
            print calculated_move
            return False


class Bishop(Piece):
    pass

class Queen(object):
    pass