import math


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z      
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)      
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z       
        
    def cross(self, other):
        return Point(
            self.y * other.z - self.z * other.y, 
            self.z * other.x - self.x * other.z, 
            self.x * other.y - self.y * other.x
        )    
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


def plane_angle(a: Point, b: Point, c: Point, d: Point):
    ab = b - a
    bc = b - c
    cd = c - d
    x = ab.cross(bc)
    y = bc.cross(cd)
    cos_f = x.dot(y) / (x.absolute() * y.absolute())
    return math.degrees(math.acos(cos_f))


if __name__ == '__main__':
    a = Point(*map(float, input().split()))
    b = Point(*map(float, input().split()))
    c = Point(*map(float, input().split()))
    d = Point(*map(float, input().split()))
    print(plane_angle(a, b, c, d))
