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


class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name  # Họ tên
        self.birth_date = birth_date  # Ngày sinh
        self.hire_date = hire_date  # Ngày vào công ty

    def display_info(self):
        """In thông tin của nhân viên ra màn hình."""
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()  # Gọi phương thức display của lớp Date
        print("Ngày vào công ty: ", end="")
        self.hire_date.display()  # Gọi phương thức display của lớp Date

# Kiểm tra lớp Employee
if __name__ == "__main__":
    # Khởi tạo ngày sinh và ngày vào công ty
    birth_date = Date(15, 5, 1990)  # Ngày sinh: 15/5/1990
    hire_date = Date(1, 6, 2020)  # Ngày vào công ty: 1/6/2020

    # Khởi tạo nhân viên
    employee = Employee("Nguyen Van A", birth_date, hire_date)

    # In thông tin nhân viên
    employee.display_info()