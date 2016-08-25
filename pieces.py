import numpy 

class Piece(object):

    def __init__(self, legal_delta, infinite, backwards):
        self.legal_delta = legal_delta
        self.infinite = infinite
        self.backwards = backwards

    def check_legal(self, origin, destination):

        if self.infinite:
            moves = []
            for d in self.legal_delta:
                while True:
                    m = tuple(abs(numpy.add(destination, origin)))
                    if m[0] > 8:
                        break
                    elif m == destination:
                        return True
            return False
                        

        delta = tuple(abs(numpy.subtract(dest, origin)))
        if delta not in self.legal_delta:
            pass

def knight_test(origin, dest):
    pos = tuple(abs(numpy.add(dest, origin)))
    print(pos)
    delta = tuple(abs(numpy.subtract(dest, origin)))
    if delta == (2, 1) or delta == (1, 2):
        print delta
        return True
    else:
        print delta
        return False

print knight_test((0, 1), (2,1))