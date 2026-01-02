from flask import Flask, redirect, render_template, request

# [PENTING 1] Wajib import nama file database.py (tanpa .py)
import database       
import qr_generator   

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 1. Ambil data dari HTML Form
        # Pastikan 'original_url' & 'custom_code' SAMA PERSIS dengan name="" di index.html
        url_dari_form = request.form.get('original_url')
        kode_dari_form = request.form.get('custom_code').strip()

        # [PENTING 2] Mengirim data ke Koki (database.py)
        # Urutannya harus: (code, original_url) sesuai fungsi di database.py
        sukses_disimpan = database.simpan_link_baru(kode_dari_form, url_dari_form)

        if not sukses_disimpan:
            return render_template('index.html', 
                                   message="❌ Yah, kode itu sudah dipakai!", 
                                   status="error")
        
        # Kalau berhasil...
        link_pendek = request.host_url + kode_dari_form
        gambar_qr = qr_generator.buat_qr_code(link_pendek)

        return render_template('index.html', 
                               message="✅ Berhasil!", 
                               status="success", 
                               new_link=link_pendek,
                               qr_code=gambar_qr)

    return render_template('index.html')

@app.route('/<path:code>')
def redirect_to_url(code):
    # [PENTING 3] Nanya ke database: "Ada nggak link buat kode ini?"
    link_asli = database.cari_link_asli(code)
    
    if link_asli:
        print(f"Mengalihkan {code} ke {link_asli}") # Debugging di terminal
        return redirect(link_asli)
    else:
        return "Link tidak ditemukan", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)