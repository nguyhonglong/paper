import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Tiền xử lý hình ảnh để dễ dàng phân tích.
    
    :param image_path: Đường dẫn đến hình ảnh.
    :return: Hình ảnh đã được xử lý.
    """
    # Đọc hình ảnh
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Làm mờ ảnh để giảm nhiễu
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Sử dụng Canny edge detection để tìm các cạnh
    edges = cv2.Canny(blurred, 50, 150)
    
    return edges

def find_bars(image):
    """
    Tìm các cột trong biểu đồ.
    
    :param image: Hình ảnh đã được xử lý.
    :return: Danh sách các tọa độ của các cột.
    """
    # Tìm các đường thẳng trong ảnh sử dụng Hough Line Transform
    lines = cv2.HoughLinesP(image, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    
    bars = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if abs(x1 - x2) < 10:  # Kiểm tra xem đó có phải là đường thẳng đứng (cột) hay không
                bars.append(((x1, y1), (x2, y2)))
    
    return bars

def analyze_barchart(image_path):
    """
    Phân tích biểu đồ cột từ hình ảnh.
    
    :param image_path: Đường dẫn đến hình ảnh.
    :return: Danh sách các tọa độ của các cột.
    """
    edges = preprocess_image(image_path)
    bars = find_bars(edges)
    return bars

# Ví dụ sử dụng
image_path = 'ielts.png'
bars = analyze_barchart(image_path)
print(bars)
