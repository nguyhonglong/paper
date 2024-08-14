import nltk
from transformers import pipeline
import numpy as np

nltk.download('punkt')

def generate_overview(text):
    """
    Tạo phần tổng quan từ văn bản đầu vào.
    
    :param text: Văn bản chứa thông tin phân tích biểu đồ.
    :return: Phần tổng quan ngắn gọn.
    """
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

def generate_trends(bars):
    """
    Phân tích các xu hướng chính từ các tọa độ của cột.
    
    :param bars: Danh sách các tọa độ của các cột.
    :return: Văn bản mô tả các xu hướng chính.
    """
    trends = []
    heights = [abs(bar[0][1] - bar[1][1]) for bar in bars]
    positions = [bar[0][0] for bar in bars]
    
    # Phát hiện xu hướng chính
    max_height = max(heights)
    min_height = min(heights)
    
    if max_height == min_height:
        trends.append("All bars are of the same height.")
    else:
        max_index = heights.index(max_height)
        min_index = heights.index(min_height)
        trends.append(f"The tallest bar is at position {positions[max_index]} with a height of {max_height}.")
        trends.append(f"The shortest bar is at position {positions[min_index]} with a height of {min_height}.")
    
    return " ".join(trends)

def generate_body(bars):
    """
    Tạo phần thân bài từ các tọa độ của cột.
    
    :param bars: Danh sách các tọa độ của các cột.
    :return: Phần thân bài chi tiết.
    """
    body = []
    heights = [abs(bar[0][1] - bar[1][1]) for bar in bars]
    positions = [bar[0][0] for bar in bars]
    
    for i, height in enumerate(heights):
        body.append(f"The bar at position {positions[i]} has a height of {height}.")
    
    return " ".join(body)

def create_ielts_task1_writing(image_path, bars):
    """
    Tạo bài viết IELTS Task 1 từ hình ảnh biểu đồ và các tọa độ của cột.
    
    :param image_path: Đường dẫn đến hình ảnh.
    :param bars: Danh sách các tọa độ của các cột.
    :return: Bài viết hoàn chỉnh.
    """
    overview_text = generate_trends(bars)
    body_text = generate_body(bars)
    overview_summary = generate_overview(overview_text)
    
    # Tạo bài viết
    writing = f"""
    The given bar chart illustrates various data points extracted from the image at {image_path}.
    
    Overview:
    {overview_summary}
    
    Details:
    {body_text}
    """
    
    return writing

# Ví dụ sử dụng
image_path = 'path_to_your_barchart_image.jpg'
bars = [((np.int32(476), np.int32(268)), (np.int32(476), np.int32(9))),
        ((np.int32(479), np.int32(268)), (np.int32(479), np.int32(9))),
        ((np.int32(4), np.int32(268)), (np.int32(4), np.int32(10))),
        ((np.int32(7), np.int32(268)), (np.int32(7), np.int32(6)))]

ielts_writing = create_ielts_task1_writing(image_path, bars)
print(ielts_writing)
 