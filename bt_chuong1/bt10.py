import math

# Lớp Điểm
class Diem:
    def __init__(self, x=0, y=0):
        self.toa_do_x = x  # Tọa độ x của điểm
        self.toa_do_y = y  # Tọa độ y của điểm

    def hien_thi(self):
        print(f"Điểm tọa độ: ({self.toa_do_x}, {self.toa_do_y})")

# Lớp Elip kế thừa từ lớp Điểm
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y)  # Kế thừa tọa độ từ lớp Điểm
        self.ban_truc_lon = ban_truc_lon  # Bán trục lớn (a)
        self.ban_truc_nho = ban_truc_nho  # Bán trục nhỏ (b)

    def dien_tich(self):
        # Diện tích của elip = pi * bán trục lớn * bán trục nhỏ
        return math.pi * self.ban_truc_lon * self.ban_truc_nho

    def hien_thi(self):
        super().hien_thi()  # Gọi phương thức hiển thị từ lớp Điểm
        print(f"Bán trục lớn: {self.ban_truc_lon}")
        print(f"Bán trục nhỏ: {self.ban_truc_nho}")
        print(f"Diện tích elip: {self.dien_tich()}")

# Lớp Đường tròn kế thừa từ Elip
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  # Bán trục lớn và nhỏ bằng nhau ở đường tròn
        self.ban_kinh = ban_kinh  # Bán kính của đường tròn

    def dien_tich(self):
        # Diện tích đường tròn = pi * bán kính^2
        return math.pi * (self.ban_kinh ** 2)

    def hien_thi(self):
        super().hien_thi()  # Gọi phương thức hiển thị từ lớp Elip
        print(f"Bán kính: {self.ban_kinh}")
        print(f"Diện tích đường tròn: {self.dien_tich()}")

# Sử dụng các lớp đã xây dựng
if __name__ == "__main__":
    # Nhập thông tin cho elip
    elip = Elip(0, 0, 5, 3)
    print("Thông tin elip:")
    elip.hien_thi()

    print("\n")

    # Nhập thông tin cho đường tròn
    duong_tron = DuongTron(0, 0, 4)
    print("Thông tin đường tròn:")
    duong_tron.hien_thi()
