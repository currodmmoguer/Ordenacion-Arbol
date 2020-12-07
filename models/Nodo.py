class Nodo:

    def __init__(self, versn, id, parent):
        self.verns = versn
        self.id = id
        self.parent = parent

    def __str__(self):
        txt = 'Nodo = { versn: ' + self.verns + ', id: ' + str(self.id) +', parent: ' + str(self.parent) + '}'
        return txt

    def __getitem__(self, i):
        if i == 0:
            return self.verns
        elif i == 1:
            return self.id
        elif i == 2:
            return self.parent
        return None