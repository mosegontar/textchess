import numpy 

PAWN = {'deltas': [(1,0)],
        'infinite': True,
        'backwards': False}

ROOK = {'deltas': [(1,0), (0,1)],
        'infinite': True,
        'backwards': True}

KNIGHT = {'deltas': [(1,2), (2, 1)],
          'infinite': False,
          'backwards': True}

BISHOP = {'deltas': [(1,1)],
          'infinite': True,
          'backwards': True}

QUEEN = {'deltas': [(1,1), (1,0), (0, 1)],
         'infinite': True,
         'backwards': True}


KING = {'deltas': [(1,1), (1,0), (0, 1)],
        'infinite': False,
        'backwards': True}

class Piece(object):

    def __init__(self, legal_delta, infinite, backwards):
        self.legal_delta = legal_delta
        self.infinite = infinite
        self.backwards = backwards

    def check_legal(self, origin, destination):

        if self.infinite:
            new_origin = origin
            for d in self.legal_delta:
                moves = []
                moves.append(new_origin)
                while True:
                    if destination[0] > origin[0]:
                        m = tuple(numpy.add(d, new_origin))
                    else:
                        m = type(abs(numpy.subtract(d, new_origin)))
                    if m[0] > 8:
                        break
                    elif m == destination:
                        moves.append(m)
                        return moves
                    else:
                        moves.append(m)
                    new_origin = m
            return False
                        

p = Piece(BISHOP['deltas'], BISHOP['infinite'], BISHOP['backwards'])

print p.check_legal((-2, -1), (1,2))

