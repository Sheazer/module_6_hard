class Figure:
    sides_count = 0

    def __init__(self, color, sides):

        self.__sides = self.__is_valid_sides(sides)
        if self.__is_valid_color(*color):
            self.__color = list(color)
            self.filled = True
        else:
            self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and g >= 0 <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = color

    def __is_valid_sides(self, args):
        s = []
        if self.sides_count == len(args):
            for i in args:
                if i > 0:
                    s.append(i)
                else:
                    s = []
                    break
            if len(s) != 0:
                return s
        for i in range(self.sides_count):
            s.append(1)
        return s

    def get_sides(self):
        return self.__sides

    def __len__(self):
        s = 0
        for i in self.__sides:
            s += i
        return s

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_square(self):
        if self.sides_count == 3:
            p = 0
            for i in self.__sides:
                p += i
            p /= 2
            return p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]) ** (0.5)
        elif self.sides_count == 1:
            self.radius = self.__sides[0]/2*3.14
            return 3.14 * self.radius**2


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = 0


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        x = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                x.append(sides[0])
        super().__init__(color, x)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
