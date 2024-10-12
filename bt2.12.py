import requests

#Gọi API để lấy dữ liệu các bài post
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (HTTP status code 200)
if response.status_code == 200:
    # Chuyển dữ liệu từ JSON sang danh sách các đối tượng Python
    posts = response.json()
    
    #Hiển thị tổng số bài post
    total_posts = len(posts)
    print(f"Tổng số bài post: {total_posts}")
    
    #Hiển thị chi tiết các bài post
    print("\nDanh sách các bài post:")
    for post in posts:
        print(f"UserID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)  # Đường kẻ ngăn cách giữa các bài post

else:
    print("Không thể lấy dữ liệu từ API.")
