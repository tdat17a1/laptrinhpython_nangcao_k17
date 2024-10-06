from xml.dom import minidom

# Tải và phân tích file XML sample.xml
doc = minidom.parse("/Users/dotuandat/Documents/GitHub/git-python nâng cao/laptrinhpython_nangcao_k17/btap_chuong2/sample.xml")

# Lấy danh sách tất cả các phần tử trong file XML
elements = doc.getElementsByTagName("*")  # "*" để lấy tất cả các phần tử

# Duyệt qua và in tên của từng phần tử
for element in elements:
    print(element.tagName)
