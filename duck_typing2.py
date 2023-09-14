class TwoDPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class XYObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sum(a):
    return a.x + a.y

def main():
    p = TwoDPoint(1, 2)
    xy = XYObject(1, 2)
    print(sum(p))
    print(sum(xy))
    
main()