from xml.dom import minidom

# Tải và phân tích file XML
doc = minidom.parse("/Users/dotuandat/Documents/GitHub/git-python nâng cao/laptrinhpython_nangcao_k17/btap_chuong2/sample.xml")

# Lấy tên công ty
company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Company Name: {company_name}")

# Lấy danh sách nhân viên
staffs = doc.getElementsByTagName("staff")

# Duyệt qua từng nhân viên và in thông tin
for staff in staffs:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}, Name: {staff_name}, Salary: {salary}")
