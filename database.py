import json
from pathlib import Path

# Setup lokasi file urls.json (database)
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "urls.json"

def ambil_semua_data():
    if not DATA_FILE.exists():
        return {}
    try:
        return json.loads(DATA_FILE.read_text())
    except:
        return {}

def simpan_link_baru(code, original_url):
    data = ambil_semua_data()
    
    if code in data:
        return False 
    
    data[code] = original_url
    DATA_FILE.write_text(json.dumps(data, indent=2))
    return True

def cari_link_asli(code):
    data = ambil_semua_data()
    return data.get(code)