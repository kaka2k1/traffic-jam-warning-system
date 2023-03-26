### Get data từ URL
# import datetime
# import time

# import cv2
# import requests
# from ultralytics import YOLO

# model = YOLO("D:\\HK2-22-23\\TLCN\\predict\\yolov8n.pt")

# URL = 'http://www.giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx'

# IDs = ['587ef5dfb807da0011e33d59']
# millisecond = datetime.datetime.now()
# t = int(time.mktime(millisecond.timetuple()) * 1000)
# PARAMS = {'id': IDs[0], 't': t}

# while True:
#     time.sleep(45)
#     results = model(URL+'?id='+IDs[0]+'?t='+t,show=True)
#     cv2.waitKey(0)
 
### Xoá dòng trắng
# import pandas as pd

# # Đọc file csv
# df = pd.read_csv('D:\\HK2-22-23\\TLCN\\file.csv')

# # Loại bỏ các dòng trống
# df.dropna(inplace=True)

# # Lưu lại file csv sau khi loại bỏ các dòng trống
# df.to_csv('filename_new.csv', index=False)

### Tạo boudung box từ csv
## Xử lí file csv sang txt
# import pandas as pd
# import os

# csv_file_path = 'D:\\HK2-22-23\\TLCN\\labeltest\\filename_new.csv'
# txt_folder_path = 'D:\\HK2-22-23\\TLCN\\labeldata13'
# df = pd.read_csv(csv_file_path)
# for index, row in df.iterrows():
#     # Lấy tên file text từ cột đầu tiên của dòng
#     file_name = row[0]
    
#     # Tạo tên đầy đủ của file text
#     txt_file_path = os.path.join(txt_folder_path, file_name + '.txt')
    
#     # Kiểm tra xem file text đã tồn tại hay chưa, nếu chưa thì tạo mới
#     if not os.path.exists(txt_file_path):
#         txt_file = open(txt_file_path, 'w')
#     else:
#         txt_file = open(txt_file_path, 'a')
    
#     # Ghi các cột còn lại vào file text
#     for i in range(1, len(row)):
#         txt_file.write(str(row[i]) + '\n')
    
#     # Đóng file text
#     txt_file.close()
## xử lí file txt
# import os

# path = 'D:\\HK2-22-23\\TLCN\\labeldata13 - Copy'

# FJoin = os.path.join
# files = [FJoin(path, f) for f in os.listdir(os.path.expanduser(path))]

# data = []

# for f in files:
#     with open(f, 'r', encoding='UTF-8') as file:
#         l_strip = []
#         read_file = file.readlines()
#         for i in read_file:
#             if (read_file.index(i) + 1) % 5 == 0:
#                 l_strip.insert(0,i.strip())
#                 data.append(l_strip.copy())
#                 l_strip.clear()
#             else:
#                 l_strip.append(i.strip())
#     with open(f, 'w') as file:
#         for l in data:
#             file.write(' '.join(l) + '\n')
#     data.clear()

## Xử lí file csv
# import csv
# import re

# # Đường dẫn tới file csv
# csv_file_path = "D:\\HK2-22-23\\TLCN\\data_kaggle\\data13gb\\data.csv"

# # Tạo mẫu regex để tìm kí tự cần xoá
# regex_pattern = re.compile(r'original/imgs/(.*).jpg')

# # Mở file csv và tạo file mới để ghi kết quả
# with open(csv_file_path, 'r') as csv_file, open('file.csv', 'w') as new_file:
#     csv_reader = csv.reader(csv_file)
#     csv_writer = csv.writer(new_file)
    
#     # Đọc header và ghi vào file mới
#     header = next(csv_reader)
#     csv_writer.writerow(header)
    
#     # Lặp qua từng dòng và xử lý cột đầu tiên
#     for row in csv_reader:
#         # Tìm kí tự cần xoá và xoá chúng
#         match = regex_pattern.search(row[0])
#         if match:
#             row[0] = match.group(1)
        
#         # Ghi dòng mới vào file mới
#         csv_writer.writerow(row)

# import os
# import csv

# csv_file = "D:\\HK2-22-23\\TLCN\\file.csv"

# with open(csv_file, "r") as file:
#     csv_reader = csv.reader(file)

#     # Lấy header của file CSV
#     headers = next(csv_reader)

#     # Lặp qua từng dòng trong file CSV
#     for row in csv_reader:
#         # Lấy tên file text từ cột đầu tiên
#         txt_file = row[0]

#         # Lấy các giá trị của bounding box
#         x_min = row[1]
#         y_min = row[2]
#         x_max = row[3]
#         y_max = row[4]
#         last_col = row[-1]

#         # Tạo file .txt với tên từ cột đầu tiên của dòng hiện tại
#         with open(txt_file + ".txt", "w") as txt:
#             # Ghi dữ liệu bounding box vào file .txt
#             txt.write(f"{x_min}, {y_min}, {x_max}, {y_max}, {last_col}\n")

########## Xử lí
# import os
# import re

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = 'D:\\HK2-22-23\\TLCN\\data_kaggle\\motor\\train\\labels'

# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và lọc các dòng theo yêu cầu
#         with open(file_path, 'r') as f:
#             lines = f.readlines()
#         lines = [line for line in lines if re.match(r'^[01]', line)]
        
#         # Ghi lại các dòng thỏa mãn vào tập tin
#         with open(file_path, 'w') as f:
#             f.writelines(lines)

# ## xoá txt k có dữ liệu
# import os

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = 'D:\\HK2-22-23\\TLCN\\data_kaggle\\motor\\train\\labels'

# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và kiểm tra xem có dữ liệu không
#         with open(file_path, 'r') as f:
#             file_content = f.read()
#         if not file_content.strip():
#             os.remove(file_path)
## Đổi kí tự đầu tiên của từng dòng trong file txt
# import os

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = 'D:\\HK2-22-23\\TLCN\\data_kaggle\\motor\\test\\labels'

# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và thay thế kí tự đầu tiên bằng số 1
#         with open(file_path, 'r') as f:
#             lines = f.readlines()
#         lines = ['1' + line[1:] for line in lines]
        
#         # Ghi lại nội dung đã sửa vào tập tin
#         with open(file_path, 'w') as f:
#             f.writelines(lines)

## Xoá file jpg không có file txt  và ngược lại 
import os

# Đường dẫn đến thư mục chứa ảnh
image_folder_path = 'D:\\HK2-22-23\\TLCN\\data_kaggle\\motor\\valid\\images'
# Đường dẫn đến thư mục chứa tệp chú thích
label_folder_path = 'D:\\HK2-22-23\\TLCN\\data_kaggle\\motor\\valid\\labels'

# Tạo danh sách các tệp ảnh và tệp chú thích
image_files = os.listdir(image_folder_path)
label_files = os.listdir(label_folder_path)

# Lấy danh sách các tệp ảnh và tệp chú thích với định dạng tên tệp giống nhau
image_names = [os.path.splitext(file)[0] for file in image_files if file.endswith('.jpg')]
label_names = [os.path.splitext(file)[0] for file in label_files if file.endswith('.txt')]

# Xóa các tệp ảnh không có tên tương ứng trong tệp chú thích
for image_name in image_names:
    if image_name not in label_names:
        image_file_path = os.path.join(image_folder_path, image_name + '.jpg')
        os.remove(image_file_path)

# Xóa các tệp chú thích không có tên tương ứng trong tệp ảnh
for label_name in label_names:
    if label_name not in image_names:
        label_file_path = os.path.join(label_folder_path, label_name + '.txt')
        os.remove(label_file_path)
         
## Xử lí
# import os

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = "D:\\HK2-22-23\\TLCN\\data_kaggle\\truck\\valid\\labels"

# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và lọc các dòng theo yêu cầu
#         with open(file_path, 'r') as f:
#             lines = f.readlines()
#         lines = [line for line in lines if not line.startswith('4')]
        
#         # Ghi lại các dòng thỏa mãn vào tập tin
#         with open(file_path, 'w') as f:
#             f.writelines(lines)
##Xử lí
# import os

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = "D:\\HK2-22-23\\TLCN\\data_kaggle\\truck\\train\\labels"
# # folder_path = 'D:\\HK2-22-23\\TLCN\\thumuctest'
# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và lọc các dòng theo yêu cầu
#         with open(file_path, 'r') as f:
#             lines = f.readlines()
#         lines = [line for line in lines if line.startswith('5')]
        
#         # Ghi lại các dòng thỏa mãn vào tập tin
#         with open(file_path, 'w') as f:
#             f.writelines(lines)
            
# ## Xử lí
# import os

# # Đường dẫn tới thư mục chứa các tập tin txt
# folder_path = "D:\\HK2-22-23\\TLCN\\data_kaggle\\truck\\train\\labels"

# # Liệt kê các tập tin txt trong thư mục
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.txt'):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Đọc nội dung tập tin và kiểm tra xem có dữ liệu không
#         with open(file_path, 'r') as f:
#             file_content = f.read()
#         if not file_content.strip():
#             os.remove(file_path)
