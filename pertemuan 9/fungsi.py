import os

def create_directory(path):
    """Membuat direktori jika belum ada."""
    os.makedirs(path, exist_ok=True)
    # print(f"Directory created: {path}") # Bisa diaktifkan untuk debugging

def write_to_file(path, content):
    """Menulis konten ke file menggunakan mode 'a' (append)."""
    try:
        # Gunakan 'a' (append) agar konten terus ditambahkan
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content + "\n")
    except Exception as e:
        print(f"Error writing file {path}: {e}")

def does_file_exist(path):
    """Memeriksa apakah file ada."""
    return os.path.exists(path)

def create_new_file(path):
    """Membuat file baru (mode 'w' akan menimpa jika sudah ada)."""
    with open(path, 'w', encoding='utf-8') as f:
        pass