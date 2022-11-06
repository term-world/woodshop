from WoodPile import Pile
from Saw import Saw
from Lumber import Lumber

from TablePlans import Table
from ChairPlans import Chair
from BookshelfPlans import Bookshelf

"""
NOTE FOR TLs:

I am giving you a somewhat advanced solution. This is for those
students who want to go a little bit beyond. Only a few will.

However, the solution is essentially to make and cut enough
board-feet (bf) in order to get a pile that contains 55 (bf) _and_ 
has enough pieces to make 3 objects. This means that they can't just
make a single board of 55 feet.

But! Students savvy to how instance properties work could create
a very long board and set the cut_size in the saw to make (n) boards
of the right size. I'm good with any clever dodge that achieves the goal.
"""

def remaining_wood(pile: Pile = Pile()) -> int:
    total = 0
    for piece in pile.pieces:
        total += piece.length
    return total

def make(item: any, pieces: list = []) -> any:
    object = item(pieces)
    return object

def main():
    saw = Saw()
    pile = Pile()
    
    items = [Table, Chair, Bookshelf]

    total = 0

    for item in items:
        total += item().required
    
    while remaining_wood(pile) < total:
         board = Lumber(10)
         pile.add(saw.cut(board))

    for item in items:
        obj = make(item, pile.pieces)
    
    print(remaining_wood(pile))

if __name__ == "__main__":
    main()
