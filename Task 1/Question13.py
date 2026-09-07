class shape():
    def __init__(self, n):
        self.color = n
    def get_color(self):
        return self.color
    def get_area(self):
        pass
class square(shape):
    def __init__(self, c,side):
        super().__init__(c)
        self.side = side
    def get_area(self):
        return self.side * self.side
s=input("Enter a color")
a=int(input("Enter a side"))
sq=square(s,a)
print("The area of square is:",sq.get_area())
print("The color of square is:",sq.get_color())
