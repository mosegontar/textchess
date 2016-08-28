import re
import pieces


class Board(object):

    def __init__(self):
        self.alphabet = "ABCDEFGH"
        self.board = [['.' for i in range(8)]]*8

    def create_new_board(self):
        """Set new board with pieces in original positions"""

        self.board[6] = ['p' for p in range(8)]
        self.board[7] = [piece for piece in 'rnbqkbnr']
        self.board[1] = ['P' for i in range(8)]
        self.board[0] = [piece.upper() for piece in 'rnbqkbnr']

    def display(self):
        """Displays current board"""

        print('     ' + '  '.join(list(self.alphabet)))
        print()
        for row_num, row in enumerate(self.board[::-1]):
            print(str(8-row_num) + '   ', '  '.join(row))
        print()

    def update_board(self, piece, origin, dest):
        """Update current board with new move"""

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
        """Determine which player is playing based on length of game so far"""

        if len(self.history) % 2 == 0:
            return "white"
        else:
            return "black"

    def parse_command(self, command):
        """Parse and return False if not valid"""

        command = command.upper().strip()
        match = re.match(r"[A-H][1-8][A-H][1-8]$", command)

        if not match:
            print("Not a valid request")
            return False, None, None

        origin = (int(command[1])-1, self.alphabet.index(command[0]))
        dest = (int(command[3])-1, self.alphabet.index(command[2]))

        symbol_at_origin = self.board[origin[0]][origin[1]]

        piece_at_origin = pieces.Piece(symbol_at_origin)

        return piece_at_origin, origin, dest

    def check_path_blocked(self, piece, movement):
        """Check if other pieces block  active piece's path to destination"""

        for move in movement[1:-1]:
            occupied = self.board[move[0]][move[1]]
            if occupied != '.' and not piece.jump:
                return True

        return False

    def check_capture(self, dest):
        """Check whether the active piece captures enemy at destination"""

        piece_at_destination = self.board[dest[0]][dest[1]]

        if piece_at_destination == '.':
            capture = False
        elif piece_at_destination.islower():
            capture = piece_at_destination
        else:
            print("Your {0} is already occupying {1}".format(
                piece_at_destination, dest)
            )
            return False, False

        return True, capture

    def validate(self, command):
        """Validate command and return False if any checks fail"""

        piece, origin, destination = self.parse_command(command)
        if not piece:
            return False

        movement = piece.track_move(origin, destination)

        if not movement:
            print('Sorry :( Bad Path')
            return False

        path_blocked = self.check_path_blocked(piece, movement)

        if path_blocked:
            print('Sorry :( Path Blocked')
            return False

        success, capture = self.check_capture(destination)

        if not success:
            print("Sorry :(, illegal move :(")
            return

        if capture:
            piece_name = pieces.Piece.PIECES[capture.upper()]['name']
            print("You captured a {}".format(piece_name))
        else:
            pass
        
        self.update_board(piece.symbol, origin, destination)
        
        self.history.append((piece.symbol, command))

g = Game()
g.create_new_board()
g.display()
g.validate('A2A3')
g.display()
g.validate('A3A4')
g.display()
g.validate('B1A3')
g.display()
g.validate('B2B4')
g.display()
g.validate('A3C4')
g.display()
g.validate('C1A3')
g.display()
g.validate('A3B2')
g.display()
g.validate('B2G7')
g.display()
print()
print(g.history)
