class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self,dx):
        self.dx=dx
        self.x_distance=self.x_distance+dx
        return self.x_distance

class Eagl:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self,dy):
        self.dy=dy
        self.y_distance=self.y_distance+dy
        return self.y_distance

class Pegasus(Horse,Eagl):
    def move(self,dx,dy):
        super().run(dx)
        super().fly(dy)
        return self.x_distance,self.y_distance
    def get_pas(self):
        return (self.x_distance,self.y_distance)
    def voice (self):
        print(Eagl.sound)





p1=Pegasus()
print(p1.get_pas())
p1.move(10,15)
print(p1.get_pas())
p1.move(-5,20)
print(p1.get_pas())
p1.voice()


