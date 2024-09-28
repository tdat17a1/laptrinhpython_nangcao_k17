class thi_sinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0
        
    #phương thức nhập thông tin thí sinh
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ và tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm toán của thí sinh: "))
        self.diem_ly = float(input("Nhập điểm lý của thí sinh: "))
        self.diem_hoa = float(input("Nhập điểm hoá của thí sinh: "))
        
    #phương thức/hành động tính tổng điểm
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa 
        ##tổng điểm được trả về bằng cách cộng 3 điểm toán lý hoá  
        
    #phương thức in thông tin thí sinh
    def in_thong_tin(self):
        print("họ tên thí sinh: {}".format(self.ho_ten))
        print("Điểm toán thí sinh: {}".format(self.diem_toan))
        print("Điểm lý thí sinh: {}".format(self.diem_ly))
        print("Điểm hoá thí sinh: {}".format(self.diem_hoa))
        print("Tổng điểm 3 môn của thí sinh: {}".format(self.tinh_tong_diem()))
        #tinh_tong_diem là một phương thức nên sẽ đi kèm ()

# Hàm so sánh để lấy tổng điểm
def lay_tong_diem(thi_sinh):
    #hàm này trả về tổng điểm của thí sinh
    return thi_sinh.tinh_tong_diem()
#khởi tạo hàm này để xắp sếp danh sách thí sinh theo thứ tự giảm dần


if __name__ == "__main__":
    danh_sach_thi_sinh = [] #tạo một list rỗng để chút nữa dùng append gắn phần tử
    
    #nhập số lượng thí sinh 
    so_luong = int(input("Nhập số lượng thí sinh: "))
    
    #nhập thông tin cho từng thí sinh 1
    #dùng vòng for thay while vì số lượng thí sinh có giới hạn
    for i in range(so_luong):
        ts = thi_sinh()
        print(f"Nhập thông tin cho thí sinh thứ {i+1}")
        ts.nhap_thong_tin() #dùng phương thức nhập thông tin đã khởi tạo bên trên
        danh_sach_thi_sinh.append(ts)
        #dùng append để thêm phần tử "ts" vào cuối danh sách
        
    #điểm chuẩn(theo giả thiết đầu bài là 20)
    diem_chuan = 20
    
    #lọc danh sách thí sinh trúng tuyển
    ds_thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
    
    #lọc danh sach trúng tuyển theo điểm giảm dần bằng sort
    ds_thi_sinh_trung_tuyen.sort(key=lay_tong_diem, reverse=True)
    
    #in ra danh sách trung tuyển
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in ds_thi_sinh_trung_tuyen:
        ts.in_thong_tin()
        print("---------")
    