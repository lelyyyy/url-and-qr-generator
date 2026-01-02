import qrcode
from io import BytesIO
import base64

def buat_qr_code(text_link):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return img_str