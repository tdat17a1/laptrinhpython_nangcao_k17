import json
from datetime import datetime

#Giả sử có một danh sách giao dịch tiền và vàng
transactions = []  # Danh sách các giao dịch

def add_transaction():
    while True:
        print("Chọn loại giao dịch:")
        print("1. Giao dịch tiền")
        print("2. Giao dịch vàng")
        transaction_type = input("Nhập loại giao dịch (1 hoặc 2): ")

        if transaction_type == "1":
            amount = float(input("Nhập số tiền giao dịch: "))
            transactions.append({
                "type": "money",
                "amount": amount
            })
        elif transaction_type == "2":
            amount = float(input("Nhập số lượng vàng giao dịch: "))
            transactions.append({
                "type": "gold",
                "amount": amount
            })
        else:
            print("Loại giao dịch không hợp lệ.")

        cont = input("Bạn có muốn tiếp tục thêm giao dịch không? (y/n): ")
        if cont.lower() != 'y':
            break

#Hỏi người dùng có muốn ghi giao dịch vào tập tin JSON không
def save_to_file():
    choice = input("Bạn có muốn ghi các giao dịch vào tập tin không? (1: Có, 0: Không): ")

    if choice == "1":
        # Bước 3: Lấy ngày hiện tại theo định dạng nam-thang-ngay-gio-phut-giay
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Tên tệp JSON
        filename = f"{current_time}.json"

        # Ghi danh sách giao dịch vào tệp JSON
        with open(filename, 'w') as file:
            json.dump(transactions, file, indent=4)

        print(f"Dữ liệu đã được ghi vào tệp {filename}")
    else:
        print("Không ghi dữ liệu vào tệp.")

# Thực hiện chương trình
add_transaction()  # Bước 1: Thêm giao dịch
save_to_file()  # Bước 2: Ghi vào tập tin nếu người dùng chọn
