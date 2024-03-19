import math as m
class Figure:
    def area(self):
        pass
class Krug(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return m.pi * (self.r)**2
class Triangle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

        # try:
        #     not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a)
        # except ValueError: raise ValueError('не треугольник')
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a)\
                and (self.a>0 and self.b>0 and self.c>0):
            raise ValueError('не треугольник')

    def area(self):
        p = (self.a + self.b + self.c)/2
        return (p * (p - self.a)* (p - self.b)* (p - self.c))**0.5
    def right_triangle(self):
        into_list = list([self.a, self.b, self.c])
        new_list = sorted(into_list)
        return True if (new_list[0] > 0 and new_list[0]*new_list[0]+new_list[1]*new_list[1] == new_list[2]*new_list[2]) else False
class Right(Figure):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

def area(*args):
    if len(args) == 1:
        return Krug(*args).area()
    if len(args) == 2:
        return Right(*args).area()
    if len(args) == 3:
        return Triangle(*args).area()
    if len(args) > 3:
        return False

if __name__ == '__main__':
    # print(area(3,4,5,1))
    # krug = Krug(6)
    # area_krug = krug.area()
    # print(area_krug)
    tri = Triangle(1,-2,3)
    area_tri = tri.area()
    pu = tri.right_triangle()
    print(area_tri, pu)
    # right = Right(6, 2)
    # area_right = right.area()
    # print(area_right)