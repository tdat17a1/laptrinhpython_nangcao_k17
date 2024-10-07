import json

# Giả sử dữ liệu JSON có cấu trúc như sau (bạn có thể thay thế dữ liệu theo thực tế)
data = '''
{
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abc Giải Phóng - Hà Nội",
        "departments": [
            {
                "name": "Đơn vị A1",
                "employees": 120
            },
            {
                "name": "Đơn vị A2",
                "employees": 80
            },
            {
                "name": "Đơn vị A3",
                "employees": 150
            },
            {
                "name": "Đơn vị A4",
                "employees": 50
            }
        ]
    }
}
'''

# Bước 1: Chuyển đổi dữ liệu JSON thành đối tượng Python
company_data = json.loads(data)

# Bước 2: Tính tổng số nhân viên của toàn bộ công ty
total_employees = sum(department['employees'] for department in company_data['company']['departments'])

# Bước 3: In thông tin công ty và địa chỉ
print(f"Tên công ty: {company_data['company']['name']}")
print(f"Địa chỉ: {company_data['company']['address']}")
print(".__-Thống kê nhân viên theo đơn vị------")

# Bước 4: In thống kê từng đơn vị
for idx, department in enumerate(company_data['company']['departments'], start=1):
    department_name = department['name']
    num_employees = department['employees']
    percentage = (num_employees / total_employees) * 100  # Tính tỷ lệ phần trăm
    print(f"{idx}./Tên đơn vị: {department_name}.")
    print(f"◦ Số nhân viên: {num_employees}")
    print(f"◦ Tỷ lệ: {percentage:.2f}%.")

# Bước 5: In tổng số nhân viên
print(f"Tổng số nhân viên: {total_employees}")
