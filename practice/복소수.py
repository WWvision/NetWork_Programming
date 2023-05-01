import math
class Complexnumber:
    def __init__(self, real, img):
        self.x = real 
        self.y = img
    
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Complexnumber(new_x, new_y)
    
    def __sub__(self, pt):
        new_x = self.x - pt.x
        new_y = self.y - pt.y
        return Complexnumber(new_x, new_y)
    
    def __mul__(self, factor):
        if type(factor) == int:
            return Complexnumber(self.x * factor, self.y * factor)
        elif type(factor) == Complexnumber:
            return Complexnumber(self.x*factor.x - self.y*factor.y, self.x*factor.y + self.y*factor.x)
            # (a+bj) * (c+dj) = (ac-bd) + (ad + bc)j    

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, pt): # 비교
        if self.x == pt.x and self.y == pt.y:
            return True
        else :
            return False
            
    def __str__(self):
        if self.y >= 0:
            return '{} + {}j'.format(self.x, self.y)
        else :
            return '{} - {}j'.format(self.x, abs(self.y))
        
a = Complexnumber(1, 2)
b = Complexnumber(3, 4)

print(a+b)
print(a * b)
print(a * 3)
a == b

>> 4 + 6j
>> -5 + 10j
>> 3 + 6j
>> False