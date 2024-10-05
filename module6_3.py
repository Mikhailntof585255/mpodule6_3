class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self,x_distance):
        self.x_distance=x_distance

    def run(self, dx):
        self.dx = dx
        self.x_distance = self.x_distance + dx
        return self.x_distance


class Eagl:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self,y_distance):
        self.y_distance=y_distance

    def fly(self, dy):
        self.dy = dy
        self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus(Horse, Eagl):
    def __init__(self,x_distance,y_distance):
        self.x_distance=x_distance
        self.y_distance=y_distance

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self.x_distance, self.y_distance

    def get_pas(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagl.sound)










