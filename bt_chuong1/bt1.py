class hinhchunhat:
    def __init__(self): #hàm khởi tạo giá trị của chiều dài và chiều rộng
        self.chieu_dai = 0
        self.chieu_rong = 0
        #chiều dài và chiều rộng ta mặc định cho bằng 0
        
    def nhap_kich_thuoc(self): #phương thức nhập dữ liệu 2 cạnh dài và rộng
        self.chieu_dai =  float(input("Nhập chiều dài hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
        
    def chu_vi(self): #phương thức tính chu vi hình chữ nhật
            chu_vi = (self.chieu_dai + self.chieu_rong) * 2
            print("chu vi hình chữ nhật bằng {} ".format(chu_vi))
            
    def dien_tich(self): #phương thức tính diện tích
        dien_tich = self.chieu_dai * self.chieu_rong
        print("diện tích hình chữ nhật bằng {} ".format(dien_tich))
        
    def in_thong_tin(self): #phương thức in thông tin
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        self.chu_vi()   # In chu vi
        self.dien_tich()  # In diện tích

# Chương trình chính
if __name__ == "__main__":
    hcn = hinhchunhat()  # Tạo đối tượng hình chữ nhật
    hcn.nhap_kich_thuoc()  # Nhập dữ liệu cho hình chữ nhật
    hcn.in_thong_tin()  # In thông tin của hình chữ nhật