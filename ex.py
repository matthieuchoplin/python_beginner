class Iter:
    def __init__(self, chaine):
        self.chaine = chaine
        self.position = len(chaine)

    def __next__(self):
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaine[self.position]


class RevStr(str):

    def __iter__(self):
        return Iter(self)

for i in RevStr('matthieu'):
    print(i)