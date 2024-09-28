import math

# Lớp Tam giác cơ bản
class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a  # Cạnh a
        self.canh_b = canh_b  # Cạnh b
        self.canh_c = canh_c  # Cạnh c

    def chu_vi(self):
        # Chu vi của tam giác = tổng độ dài 3 cạnh
        return self.canh_a + self.canh_b + self.canh_c

    def dien_tich(self):
        # Sử dụng công thức Heron để tính diện tích tam giác
        p = self.chu_vi() / 2  # Nửa chu vi
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))

    def hien_thi(self):
        print(f"Cạnh a: {self.canh_a}, Cạnh b: {self.canh_b}, Cạnh c: {self.canh_c}")
        print(f"Chu vi tam giác: {self.chu_vi()}")
        print(f"Diện tích tam giác: {self.dien_tich()}")

# Lớp Tam giác cân (kế thừa từ TamGiac)
class TamGiacCan(TamGiac):
    def __init__(self, canh_ben, canh_day):
        # Cạnh a và cạnh c bằng nhau
        super().__init__(canh_ben, canh_day, canh_ben)

# Lớp Tam giác đều (kế thừa từ TamGiacCan)
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        # Tất cả các cạnh của tam giác đều bằng nhau
        super().__init__(canh, canh)

# Lớp Tam giác vuông (kế thừa từ TamGiac)
class TamGiacVuong(TamGiac):
    def __init__(self, canh_goc_vuong_1, canh_goc_vuong_2):
        # Tính cạnh huyền bằng định lý Pythagoras
        canh_huyen = math.sqrt(canh_goc_vuong_1**2 + canh_goc_vuong_2**2)
        super().__init__(canh_goc_vuong_1, canh_goc_vuong_2, canh_huyen)

    def hien_thi(self):
        print("Tam giác vuông:")
        super().hien_thi()

# Sử dụng các lớp đã xây dựng
if __name__ == "__main__":
    # Tam giác thường
    print("Tam giác thường:")
    tam_giac = TamGiac(3, 4, 5)
    tam_giac.hien_thi()

    print("\nTam giác vuông:")
    tam_giac_vuong = TamGiacVuong(3, 4)
    tam_giac_vuong.hien_thi()

    print("\nTam giác cân:")
    tam_giac_can = TamGiacCan(5, 6)
    tam_giac_can.hien_thi()

    print("\nTam giác đều:")
    tam_giac_deu = TamGiacDeu(4)
    tam_giac_deu.hien_thi()
