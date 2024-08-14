from PIL import Image
import pytesseract

# Đường dẫn đến tesseract nếu cần thiết (Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Trích xuất văn bản từ hình ảnh sử dụng Tesseract OCR.
    
    :param image_path: Đường dẫn đến hình ảnh.
    :return: Văn bản được trích xuất từ hình ảnh.
    """
    try:
        # Mở hình ảnh
        img = Image.open(image_path)
        
        # Sử dụng Tesseract OCR để trích xuất văn bản
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Ví dụ sử dụng
image_path = 'ielts.png'
text = extract_text_from_image(image_path)
print(text)
