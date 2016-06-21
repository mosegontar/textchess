import re
import numpy

class Piece(object):

    def __init__(self):
        pass

class Pawn(object):
    pass

class Rook(object):
    pass

class Knight(object):

    def knight_test(self, origin, dest):

        calculated_move = tuple(abs(numpy.subtract(dest, origin)))
        if calculated_move == (2, 1) or calculated_move == (1, 2):
            print calculated_move
            return True
        else:
            print calculated_move
            return False


class Bishop(object):
    pass

class Queen(object):
    pass


class Player(object):

    def __init__(self, name):
        self.name = name
        self.captured_pieces = []

   

    def parse_command(self, command, board):

        command = command.upper().strip()
        match =  re.match(r"[A-H][1-8][A-H][1-8]$", command)
        
        if not match:
            return False

        origin = (int(command[1])-1, board.alphabet.index(command[0]))
        dest = (int(command[3])-1, board.alphabet.index(command[2]))

        piece = board.board[origin[0]][origin[1]]

        if check_legal(piece, origin, dest):
            set_board(piece, origin, dest)


        #board.board = board.board[::-1]


        


g = Game()
p = Player('Alex')
g.display()        



