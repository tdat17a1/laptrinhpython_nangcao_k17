import json

# Tạo một từ điển Python 
python_dict = {
    "name": "tuấn Đạt",
    "age": 19,
    "city": "Hà Nam",
    "job": "Analyst"
}

# Chuyển đổi từ điển thành chuỗi JSON với mức thụt lề 4
json_data = json.dumps(python_dict, indent=4)

# In chuỗi JSON
print("Chuỗi JSON với thụt lề 4:")
print(json_data)
