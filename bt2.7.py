import json

# Ví dụ về dữ liệu JSON để chuyển đổi sang python
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Chuyển đổi dữ liệu JSON thành đối tượng python 
python_obj = json.loads(json_data)

# In đối tượng Python
print(python_obj)
