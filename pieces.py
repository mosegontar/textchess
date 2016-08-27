import numpy

PAWN = {'deltas': [(1,0)],
        'infinite': False,
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

    def track_move(self, origin, destination):

        delta = tuple(numpy.subtract(destination, origin))

        for d in self.legal_delta:
            new_origin = origin
            moves = []
            moves.append(new_origin)

            while True:

                a = new_origin[0] + d[0] if delta[0] >= 0 else new_origin[0] - d[0]
                b = new_origin[1] + d[1] if delta[1] >= 1 else new_origin[1] - d[1]
                m = (a,b)

                if [y for y in m if abs(y) > 8]:
                    break
                elif m == destination:
                    moves.append(m)
                    return moves
                else:
                    moves.append(m)
                new_origin = m

        return False


def test_trackmove():

    PIECE = ROOK
    p = Piece(PIECE['deltas'], PIECE['infinite'], PIECE['backwards'])
    assert p.track_move((0, 0), (0,-2)) == [(0, 0), (0, -1), (0, -2)]

    PIECE = BISHOP
    p = Piece(PIECE['deltas'], PIECE['infinite'], PIECE['backwards'])
    assert p.track_move((0, 0), (-3,-3)) == [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (-3,-3)) != [(0, 0), (-1, -1), (-2, -2), (-3, -2)]
    assert p.track_move((0, 0), (-3,-2)) != [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (3, 3)) == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert p.track_move((0, 0), (2, -2)) == [(0, 0), (1, -1), (2, -2)]
    assert p.track_move((0, 0), (2, -2)) != [(0, 0), (1, -1), (2, -1)]

    PIECE = QUEEN
    p = Piece(PIECE['deltas'], PIECE['infinite'], PIECE['backwards'])
    assert p.track_move((0, 0), (-3,-3)) == [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (-3,-3)) != [(0, 0), (-1, -1), (-2, -2), (-3, -2)]
    assert p.track_move((0, 0), (-3,-2)) != [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    assert p.track_move((0, 0), (3, 3)) == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert p.track_move((0, 0), (2, -2)) == [(0, 0), (1, -1), (2, -2)]
    assert p.track_move((0, 0), (2, -2)) != [(0, 0), (1, -1), (2, -1)]




