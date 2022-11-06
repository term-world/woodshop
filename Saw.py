from inventory.Item import FixtureSpec
from Lumber import Lumber

class Saw(FixtureSpec):

    def __init__(self, cut_size: int = 2):
        self.cut_size = cut_size

    def cut(self, lumber: Lumber = Lumber()) -> [Lumber]:
        pieces = []
        while len(pieces) < self.cut_size:
            piece = Lumber(lumber.length / self.cut_size)
            pieces.append(piece)
        return pieces