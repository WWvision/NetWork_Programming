class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
        
    def __add__(self):
        if self.imaginary_1 + self.imaginary_2 < 0:
            return print(str(self.real_1 + self.real_2) + str(self.imaginary_1 + self.imaginary_2) + 'i')
        else:
            return print(str(self.real_1 + self.real_2) + '+' + str(self.imaginary_1 + self.imaginary_2) + 'i')


    def __del__(self):
        if self.imaginary_1 - self.imaginary_2 < 0:
            return print(str(self.real_1 - self.real_2) + str(self.imaginary_1 - self.imaginary_2) + 'i')
        else:
            return print(str(self.real_1 - self.real_2) + '-' + str(self.imaginary_1 - self.imaginary_2) + 'i')
    
result = MyComplex(2,-3,-5,4)
MyComplex.__add__(result)


