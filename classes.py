class Point:
    def draw(self):
        print("Draw function is called")

    def move(self):
        print("Move function is called")


point1 = Point()
point1.draw()
point1.move()
point1.x = 10
print(point1.x)
