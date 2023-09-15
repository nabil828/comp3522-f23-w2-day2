class Cats:
    def __init__(self):
        self._cats = ["Garfield", "Tom", "Kitty"]

    # to make this class sequence protocol compliant, we need to implement:

    def count(self):
        return len(self._cats)
    
    def index(self, a):
        return self._cats.index(a)
    
    def __len__(self):
        return len(self._cats)
    
    def __getitem__(self, a):
        return self._cats[a]
    
    def __contains__(self, a):
        return a in self._cats
    
    def __reversed__(self):
        return reversed(self._cats)
    
def main():
    c = Cats()
    print(c.count())
    print(c.index("Tom"))
    print(len(c))
    print(c[1])
    print("Garfield" in c)
    print("Garfield" not in c)
    print(list(reversed(c)))

main()