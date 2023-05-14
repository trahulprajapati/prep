
class Vertex:
    def __init__(self, ele):
        self.ele = ele

    def __hash__(self):
        return hash(id(self))