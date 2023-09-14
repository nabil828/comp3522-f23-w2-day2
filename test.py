
class Position:
    def __init__(self, x):
        self.x = x
        
class Player:
    def __init__(self, position):
        self.position = position

    def move(self, direction):
        self.old_position = self.position
        self.position.x += direction

def main():
    p1 = Position(0)
    player = Player(p1)
    player.move(1)
    print(player.position.x)
    print(player.old_position.x)

main()