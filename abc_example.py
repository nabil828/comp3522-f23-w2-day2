import abc


class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

    def x(self):
        print("x")

class Parrot(Bird):
    def fly(self):
        print("Parrot flying")

def main():
    parrot = Parrot()
    parrot.fly()

main()