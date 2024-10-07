import json

# Tạo một từ điển Python (bắt đầu từ Python 3.7, từ điển giữ thứ tự các khóa theo thứ tự thêm vào)
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

# Chuyển đổi từ điển thành chuỗi JSON với mức thụt lề 4
json_data = json.dumps(python_dict, indent=4)

# In chuỗi JSON
print("Chuỗi JSON với thụt lề 4:")
print(json_data)
