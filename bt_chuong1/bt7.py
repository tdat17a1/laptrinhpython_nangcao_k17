class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin về ngày, tháng, năm."""
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        """Tính toán ngày tiếp theo."""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            days_in_month[1] = 29

        self.day += 1  # Tăng ngày lên 1

        if self.day > days_in_month[self.month - 1]:
            self.day = 1  # Đặt lại ngày thành 1
            self.month += 1  # Tăng tháng lên 1
            
            if self.month > 12:
                self.month = 1  # Đặt lại tháng thành 1
                self.year += 1  # Tăng năm lên 1

    def is_leap_year(self):
        """Kiểm tra xem năm có phải là năm nhuận hay không."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

# Kiểm tra lớp Date
if __name__ == "__main__":
    date = Date(28, 2, 2024)  # Khởi tạo một ngày
    date.display()  # In ra ngày hiện tại
    date.next()  # Tính ngày tiếp theo
    date.display()  # In ra ngày tiếp theo
