import cv2
import numpy as np

def draw_bars(image_path, bars):
    # Đọc hình ảnh
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Vẽ các cột
    for bar in bars:
        start_point = bar[0]
        end_point = bar[1]
        color = (0, 255, 0)  # Màu xanh lá cây
        thickness = 2
        img = cv2.line(img, start_point, end_point, color, thickness)
    
    # Hiển thị hình ảnh
    cv2.imshow('Bar Chart', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ví dụ sử dụng
image_path = 'ielts.png'
bars = [((np.int32(476), np.int32(268)), (np.int32(476), np.int32(9))),
        ((np.int32(479), np.int32(268)), (np.int32(479), np.int32(9))),
        ((np.int32(4), np.int32(268)), (np.int32(4), np.int32(10))),
        ((np.int32(7), np.int32(268)), (np.int32(7), np.int32(6)))]
draw_bars(image_path, bars)
