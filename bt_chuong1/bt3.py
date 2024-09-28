class PS:
    def __init__(self, tu_so=0, mau_so=1):
        #khởi tạo tử số và mẫu số. phân số mẫu phải luôn lớn hơn 0
        self.tu_so = tu_so
        self.mau_so = mau_so
        #phòng trường hợp mẫu bằng 0 sẽ lỗi chương trình ta dùng cách sau
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không được bằng 0.")
        
    def kiem_tra_hop_le(self): #kiểm tra tính hợp lệ của phân số
        return self.mau_so!= 0
    
    def nhap_phan_so(self): #nhập phân số từ bàn phím
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không được bằng 0.")
        
    def in_phan_so(self): #in phân số ra màn hình
        print(f"Phân số nhập vào là {self.tu_so}/{self.mau_so}")
        
#sử dụng lớp PS
if __name__ == "__main__":
    try:
        ps = PS()
        ps.nhap_phan_so()
        ps.in_phan_so()
    except ValueError as e:
        print(e)
