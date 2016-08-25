import re
#from game_validation import Validator

class Board(object):

    def __init__(self):
        self.alphabet = "ABCDEFGH"
        self.board = [['.' for i in range(8)]]*8

    def create_new_board(self):

        self.board[6] = ['p' for p in range(8)]
        self.board[7] = [piece for piece in 'rnbqkbnr']
        self.board[1] = ['P' for i in range(8)]
        self.board[0] = [piece.upper() for piece in 'rnbqkbnr']

    def display(self):
        print '     ' + ' '.join(list(self.alphabet)) 
        print 
        for row_num, row in enumerate(self.board[::-1]):
            print str(8-row_num) + '   ', ' '.join(row)
        print

    def update_board(self, piece, origin, dest):

        origin_row = list(self.board[origin[0]])
        origin_row[origin[1]] = '.'
        self.board[origin[0]] = origin_row
        
        dest_row = list(self.board[dest[0]])
        dest_row[dest[1]] = piece
        self.board[dest[0]] = dest_row 

class Game(Board):

    def __init__(self):
        Board.__init__(self)
        self.history = []

        # True if castle available to white/black player
        self.white_castle = True
        self.black_castle = True

    @property
    def determine_player(self):
        if len(self.history) % 2 == 0:
            return "white"
        else:
            return "black"

    def parse_command(self, command):

        command = command.upper().strip()
        match =  re.match(r"[A-H][1-8][A-H][1-8]$", command)
        
        if not match: 
            print "Not a valid request"
            return False

        origin = (int(command[1])-1, self.alphabet.index(command[0]))
        dest = (int(command[3])-1, self.alphabet.index(command[2]))

        active_piece = self.board[origin[0]][origin[1]]
        piece_at_destination =  self.board[dest[0]][dest[1]]

        if piece_at_destination == '.':
            capture = False   
        elif piece_at_destination.islower():
            capture = True
        else:
            print "Your {0} is already occupying {1}".format(piece_at_destination, dest)
            return 

        print origin
        return active_piece, origin, dest

    def validate(self, command):
        piece, origin, destination = parse_command(command)


g = Game()
g.create_new_board()
g.display()
g.parse_command("A1A3")
g.display()
g.parse_command("C2C3")
g.display()