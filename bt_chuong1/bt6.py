#tận dụng lớp Stack của bài 4
class Stack:
    def __init__(self, dung_luong_ngan_xep):
        self.dung_luong_ngan_xan_xep = dung_luong_ngan_xep  # dung lượng của stack
        self.stack = []  # đây là dữ liệu của ngăn xếp, ta cho bằng 1 list rỗng
        self.top = -1  # vị trí phần tử trên cùng của stack

    def isFull(self):  # kiểm tra ngăn xếp xem đầy chưa
        return self.top == self.dung_luong_ngan_xan_xep - 1

    def isEmpty(self):  # kiểm tra ngăn xếp có trống không
        return self.top == -1

    def push(self, value):  # đưa phần tử vào ngăn xếp
        if self.isFull():
            raise IndexError("Stack đã đầy, không thể thêm phần tử mới.")
        self.stack.append(value)  # thêm phần tử vào danh sách
        self.top = self.top + 1  # tăng chỉ số trên cùng

    def pop(self):  # lấy một phần tử ra từ đỉnh ngăn xếp
        if self.isEmpty():
            raise IndexError("Ngăn xếp trống, không thể lấy phần tử ra.")
        value = self.stack.pop()  # lấy phần tử ra từ danh sách
        self.top = self.top - 1  # giảm chỉ số trên cùng
        return value

    def count(self):  # thêm phương thức count để trả về số phần tử trong ngăn xếp
        return self.top + 1 if not self.isEmpty() else 0

    def print_stack(self):  # thêm phương thức print_stack để in nội dung ngăn xếp
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung của ngăn xếp từ trên xuống dưới:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def __del__(self):  # hàm huỷ, dùng để xoá/dọn dẹp tài nguyên khi cần
        self.stack.clear()  # xoá dữ liệu trong stack
        print("Ngăn xếp đã được xoá/huỷ")


# sử dụng class Stack
if __name__ == "__main__":
    stack_dung_luong_ngan_xep = 5
    stack = Stack(stack_dung_luong_ngan_xep)

    # thêm phần tử vào ngăn xếp
    try:
        stack.push(1.5)
        stack.push(2.5)
        stack.push(3.5)
        stack.push(4.5)
        stack.push(5.5)
        # gọi thêm sẽ gây ra lỗi vì ta đã gán giá trị cho dung lượng của ngăn xếp bằng 5
    except IndexError as e:
        print(e)
        # nếu có lỗi ta trả về "e" và in ra "e"

    # lấy phần tử ra khỏi ngăn xếp
    try:
        top_element = stack.pop()
        print("Phần tử lấy ra từ ngăn xếp:", top_element)
    except Exception as e:
        print(e)

    # In ra số phần tử hiện có trong ngăn xếp
    print("Số phần tử hiện có trong ngăn xếp:", stack.count())

    # In nội dung ngăn xếp
    stack.print_stack()
