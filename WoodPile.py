from inventory.Item import FixtureSpec
from Lumber import Lumber

class Pile(FixtureSpec):

    def __init__(self):
        self.pieces = []

    def add(self, lumber):
        self.pieces += lumber
        print(self.pieces)