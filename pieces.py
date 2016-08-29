import numpy

class Piece(object):
    
    PIECES = {'P': {'name': 'Pawn',
                    'deltas': [(1,0)],
                    'backwards': False,
                    'jump': False}, 
              'R': {'name': 'Rook',
                    'deltas': [(1,0), (0,1)],
                    'backwards': True,
                    'jump': False},
              'N': {'name': 'Knight', 
                    'deltas': [(1,2), (2, 1)],
                    'backwards': True,
                    'jump': False},
              'B': {'name': 'Bishop',
                    'deltas': [(1,1)],
                    'backwards': True,
                    'jump': False},
              'Q': {'name': 'Queen',
                    'deltas': [(1,1), (1,0), (0, 1)],
                    'backwards': True,
                    'jump': False,},
              'K': {'name': 'King',
                    'deltas': [(1,1), (1,0), (0, 1)],
                    'backwards': True,
                    'jump': False,}
    }    

    def __init__(self, symbol):
        self.symbol = symbol
        self.piece = Piece.PIECES[symbol]
        self.name = self.piece['name']
        self.legal_delta = self.piece['deltas']
        self.backwards = self.piece['backwards']
        self.jump = self.piece['jump']

    def track_move(self, origin, destination):

        delta = tuple(numpy.subtract(destination, origin))

        # check if piece is making illegal move backwards
        if delta[0] < 0 and not self.backwards:
            return False

        for d in self.legal_delta:
            new_origin = origin
            moves = []
            moves.append(new_origin)

            while True:
                y = new_origin[0] + d[0] if delta[0] >= 0 else new_origin[0] - d[0]
                x = new_origin[1] + d[1] if delta[1] >= 1 else new_origin[1] - d[1]
                move = (y, x)

                if [i for i in move if abs(i) > 8]:
                    break
                elif move == destination:
                    moves.append(move)
                    
                    if self.name == 'Pawn':
                        if (len(moves) == 3 and origin[0] != 1) or len(moves) > 3:
                            print("Pawn can't move there")
                            return False

                    if self.name == 'Knight' and len(moves) > 2:
                        print("Knight can't move there")
                        return False

                    return moves

                else:
                    moves.append(move)
                    new_origin = move

        return False


def test_track_move():

    p = Piece('R')
    assert p.track_move((0, 0), (0,-2)) == [(0, 0), (0, -1), (0, -2)]
    assert p.track_move((0, 0), (-8, 0)) == [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)]
    assert p.track_move((-1, -1), (1, -1)) == [(-1, -1), (0, -1), (1, -1)]

    p = Piece('N')
    assert p.track_move((0, 0), (2, 1)) == [(0, 0), (2, 1)]
    assert p.track_move((-3, -2), (-1, -1)) == [(-3, -2), (-1, -1)]
    assert len(p.track_move((1, 1), (3, 2))) == 2
    assert p.track_move((-4, 0), (-3, 2)) == [(-4,0), (-3, 2)]
    assert p.track_move((-4, 0), (-3, -2)) == [(-4, 0), (-3, -2)]
    assert p.track_move((-2, 0), (-4, -1)) == [(-2, 0), (-4, -1)]
    assert p.track_move((-8, -2), (-7, 0)) == [(-8, -2), (-7, 0)]
    assert p.track_move((-8, -2), (-6, 2)) == False

    p = Piece('B')
    assert p.track_move((0, 0), (-3,-3)) == [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (-3,-3)) != [(0, 0), (-1, -1), (-2, -2), (-3, -2)]
    assert p.track_move((0, 0), (-3,-2)) != [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (3, 3)) == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert p.track_move((0, 0), (2, -2)) == [(0, 0), (1, -1), (2, -2)]
    assert p.track_move((0, 0), (2, -2)) != [(0, 0), (1, -1), (2, -1)]

    p = Piece('Q')
    assert p.track_move((0, 0), (-3,-3)) == [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (-3,-3)) != [(0, 0), (-1, -1), (-2, -2), (-3, -2)]
    assert p.track_move((0, 0), (-3,-2)) != [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (3, 3)) == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert p.track_move((0, 0), (2, -2)) == [(0, 0), (1, -1), (2, -2)]
    assert p.track_move((0, 0), (2, -2)) != [(0, 0), (1, -1), (2, -1)]
