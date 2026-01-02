import json
from pathlib import Path

# Setup lokasi file urls.json (biar nggak nyasar)
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "urls.json"

def ambil_semua_data():
    # Cek kalau file belum ada atau kosong, anggap dictionary kosong {}
    if not DATA_FILE.exists():
        return {}
    try:
        return json.loads(DATA_FILE.read_text())
    except:
        return {}

# --- [PENTING] ---
# Fungsi ini menerima 2 bahan: code (kuncinya) dan original_url (isinya)
def simpan_link_baru(code, original_url):
    data = ambil_semua_data()
    
    # Validasi: Kalau kode udah ada, tolak!
    if code in data:
        return False 
    
    # Kalau aman, simpan
    data[code] = original_url
    DATA_FILE.write_text(json.dumps(data, indent=2))
    return True
# -----------------

def cari_link_asli(code):
    data = ambil_semua_data()
    return data.get(code)