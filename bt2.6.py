import requests  # Thư viện dùng để gửi yêu cầu HTTP và lấy dữ liệu từ URL
import xml.etree.ElementTree as ET  # Thư viện để phân tích cú pháp XML
import csv  # Thư viện để làm việc với tệp CSV

#b1 tải nguồn cấp RSS từ URL và lưu dưới dạng tệp XML
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'  # Đường dẫn URL đến RSS feed
response = requests.get(url)  # Gửi yêu cầu GET để tải nội dung từ URL
# Lưu nội dung tải về dưới dạng tệp XML (ở chế độ ghi nhị phân)
with open('rss_feed.xml', 'wb') as file:
    file.write(response.content)  # Ghi dữ liệu nhận được vào tệp 'rss_feed.xml'

#b2 Phân tích cú pháp tệp XML và lưu tin tức thành danh sách từ điển
tree = ET.parse('rss_feed.xml')  # Phân tích cú pháp của tệp XML đã tải về
root = tree.getroot()  # Lấy phần tử gốc của cây XML

news_items = []  # Danh sách để lưu các mục tin tức dưới dạng từ điển
# Tìm tất cả các phần tử <item> trong tệp XML, mỗi phần tử đại diện cho một tin tức
for item in root.findall('.//item'):
    news = {}  # Tạo một từ điển cho mỗi mục tin tức
    # Lấy nội dung của các thẻ <title>, <link>, <description>, và <pubDate>
    news['title'] = item.find('title').text  # Lấy tiêu đề của tin tức
    news['link'] = item.find('link').text  # Lấy liên kết của tin tức
    news['description'] = item.find('description').text  # Lấy mô tả của tin tức
    news['pubDate'] = item.find('pubDate').text  # Lấy ngày xuất bản của tin tức
    news_items.append(news)  # Thêm mục tin tức vào danh sách

#b3 Lưu các mục tin tức vào tệp CSV
# Mở tệp CSV ở chế độ ghi, dùng UTF-8 để tránh lỗi ký tự đặc biệt
with open('news.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Định nghĩa các tên cột của tệp CSV
    fieldnames = ['title', 'link', 'description', 'pubDate']
    # Tạo đối tượng DictWriter để ghi từ điển vào tệp CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Ghi hàng tiêu đề vào tệp CSV
    for news in news_items:  # Duyệt qua từng mục tin tức trong danh sách
        writer.writerow(news)  # Ghi mục tin tức vào tệp CSV

print("Đã lưu tin tức vào tệp news.csv.")  # Thông báo sau khi hoàn thành
