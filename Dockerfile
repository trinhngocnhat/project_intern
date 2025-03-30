# Sử dụng Python làm base image
FROM python:3.9

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements trước (giúp cache lại layer nếu không đổi)
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết trước để tăng tốc độ build
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ source code vào container
COPY . /app

# Expose cổng 5000 để Flask có thể chạy
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
