# Lớp Đa giác (Polygon)
class Polygon:
    def __init__(self, sides):
        self.sides = sides  # Số cạnh của đa giác

    def display_info(self):
        print(f"Đây là một đa giác với {self.sides} cạnh.")

# Lớp Hình bình hành (Parallelogram) kế thừa từ Đa giác
class Parallelogram(Polygon):
    def __init__(self, base, side, height):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.base = base  # Cạnh đáy
        self.side = side  # Cạnh bên
        self.height = height  # Chiều cao

    def perimeter(self):
        return 2 * (self.base + self.side)  # Chu vi = 2*(cạnh đáy + cạnh bên)

    def area(self):
        return self.base * self.height  # Diện tích = cạnh đáy * chiều cao

# Lớp Hình chữ nhật (Rectangle) kế thừa từ Hình bình hành
class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, width, height)  # Hình chữ nhật có 2 cạnh bằng nhau
        self.width = width  # Chiều rộng
        self.height = height  # Chiều cao

    def perimeter(self):
        return 2 * (self.width + self.height)  # Chu vi = 2*(chiều dài + chiều rộng)

    def area(self):
        return self.width * self.height  # Diện tích = chiều dài * chiều rộng

# Lớp Hình vuông (Square) kế thừa từ Hình chữ nhật
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Hình vuông có chiều dài = chiều rộng
        self.side = side  # Cạnh của hình vuông

    def perimeter(self):
        return 4 * self.side  # Chu vi = 4 * cạnh

    def area(self):
        return self.side ** 2  # Diện tích = cạnh^2

# Sử dụng các lớp đã xây dựng
if __name__ == "__main__":
    # Tạo một hình bình hành
    parallelogram = Parallelogram(10, 8, 6)
    print("Hình bình hành:")
    print(f"Chu vi: {parallelogram.perimeter()}")
    print(f"Diện tích: {parallelogram.area()}\n")

    # Tạo một hình chữ nhật
    rectangle = Rectangle(10, 5)
    print("Hình chữ nhật:")
    print(f"Chu vi: {rectangle.perimeter()}")
    print(f"Diện tích: {rectangle.area()}\n")

    # Tạo một hình vuông
    square = Square(7)
    print("Hình vuông:")
    print(f"Chu vi: {square.perimeter()}")
    print(f"Diện tích: {square.area()}")
