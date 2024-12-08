class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        print(f'Information about the figure: {self.unit}')
class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length * self.__side_length
    def info(self):
        print(f'Square side length:{self.__side_length}, area:{self.calculate_area()}')

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calculate_area(self):
        return self.__length * self.__width
    def info(self):
        print(f'Rectangle length: {self.__length}, width: {self.__width}, area: {self.calculate_area()}')

figures = [
        Square(4),
        Square(6),
        Rectangle(5, 6),
        Rectangle(7, 8),
        Rectangle(9, 10) ]

for figure in figures:
    figure.info()