import requests

# Bước 1: Gọi API để lấy dữ liệu các bài post với postId = 1
url = 'https://jsonplaceholder.typicode.com/comments?postId=1'
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (HTTP status code 200)
if response.status_code == 200:
    # Chuyển đổi dữ liệu JSON sang danh sách các đối tượng Python
    posts = response.json()
    
    # Bước 2: Hiển thị danh sách các bài post nổi bật
    print("Danh sách các bài post nổi bật (chỉ hiển thị 3 bài đầu):")
    
    # Bước 3: Giới hạn hiển thị chỉ 3 bài đầu tiên
    for post in posts[:3]:
        print(f"Post ID: {post['postId']}")
        print(f"ID: {post['id']}")
        print(f"Name: {post['name']}")
        print(f"Email: {post['email']}")
        print(f"Body: {post['body']}")
        print("-" * 40)  # Đường kẻ ngăn cách giữa các bài post

else:
    print("Không thể lấy dữ liệu từ API.")
