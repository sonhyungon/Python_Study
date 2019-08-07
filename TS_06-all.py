# 문제 6-1
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        t = (self.x, self.y)
        return t

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# 문제 6-2
p1 = point(1, 1)

print(p1.get())

p1.setx(3)
p1.sety(3)
print(p1.get())

p1.move(2, 3)
print(p1.get())


# 문제 6-3 Pass

# 문제 6-4 정답: kospi

# 문제 6-5 Pass






