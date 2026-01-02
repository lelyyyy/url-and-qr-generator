import qrcode
from io import BytesIO
import base64

def buat_qr_code(text_link):
    # 1. Settingan QR
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text_link)
    qr.make(fit=True)
    
    # 2. Bikin Gambar
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 3. Simpan ke Memory (RAM)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    # 4. Ubah jadi text Base64
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return img_str