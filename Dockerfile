# Sử dụng Python làm base image
FROM python:3.9

# Đặt thư mục làm thư mục làm việc chính
WORKDIR /app

# Sao chép toàn bộ project vào container
COPY . flask_translate /app

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
