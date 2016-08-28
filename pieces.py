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

                y = new_origin[0] + d[0] if delta[0] >= 0 else new_origin[0] - d[0]
                x = new_origin[1] + d[1] if delta[1] >= 1 else new_origin[1] - d[1]
                move = (y, x)

                if [i for i in move if abs(i) > 8]:
                    break
                elif move == destination:
                    moves.append(move)
                    return moves
                elif not self.infinite:
                    break
                else:
                    moves.append(move)
                    new_origin = move

        return False


def test_track_move():

    PIECE = ROOK
    p = Piece(PIECE['deltas'], PIECE['infinite'], PIECE['backwards'])
    assert p.track_move((0, 0), (0,-2)) == [(0, 0), (0, -1), (0, -2)]
    assert p.track_move((0, 0), (-8, 0)) == [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)]
    assert p.track_move((-1, -1), (1, -1)) == [(-1, -1), (0, -1), (1, -1)]

    PIECE = KNIGHT
    p = Piece(PIECE['deltas'], PIECE['infinite'], PIECE['backwards'])
    assert p.track_move((0, 0), (2, 1)) == [(0, 0), (2, 1)]
    assert p.track_move((-3, -2), (-1, -1)) == [(-3, -2), (-1, -1)]
    assert len(p.track_move((1, 1), (3, 2))) == 2
    assert p.track_move((-4, 0), (-3, 2)) == [(-4,0), (-3, 2)]
    assert p.track_move((-4, 0), (-3, -2)) == [(-4, 0), (-3, -2)]
    assert p.track_move((-2, 0), (-4, -1)) == [(-2, 0), (-4, -1)]
    assert p.track_move((-8, -2), (-7, 0)) == [(-8, -2), (-7, 0)]
    assert p.track_move((-8, -2), (-6, 2)) == False

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




