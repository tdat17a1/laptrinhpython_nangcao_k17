import json

# Ví dụ về dữ liệu JSON để chuyển đổi sang python
json_data = '{"name": "Đạt", "age": 19, "city": "Hà Nam"}'

# Chuyển đổi dữ liệu JSON thành đối tượng python 
python_object = json.loads(json_data)

# In đối tượng Python
print(python_object)
