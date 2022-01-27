class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        area = abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)
        return area

    def get_perimeter(self):
        perimeter = abs(self.p1.x - self.p2.x) * 2 + abs(self.p1.y - self.p2.y) * 2
        return perimeter

    def is_square(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y)