"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

class State:

    def __init__(self, vc_coord, dirt_tuples):
        self.vc_coord = vc_coord
        self.dirt_tuples = dirt_tuples

    def __eq__(self, other):
        return self.vc_coord == other.vc_coord and self.dirt_tuples == other.dirt_tuples

    def __str__(self):
        return "Vacuum Cleaner Coordinate - " + str(self.vc_coord) + " Dirt List - " + str(self.dirt_tuples)

    def __hash__(self) -> int:
        return hash( (tuple(self.vc_coord), tuple([tuple(x) for x in self.dirt_tuples])) )