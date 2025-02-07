import requests
from bs4 import BeautifulSoup

def upload_file(website, filepath):
    """Mengunggah file ke situs web menggunakan formulir unggah."""

    try:
        # 1. Dapatkan URL formulir unggah
        response = requests.get("http://" + website)  # Ganti dengan https:// jika perlu
        soup = BeautifulSoup(response.content, "html.parser")
        form = soup.find("form", {"enctype": "multipart/form-data"})

        if not form:
            print("Tidak ditemukan formulir unggah di situs web.")
            return

        upload_url = form["action"]
        if not upload_url.startswith("http"):
            upload_url = "http://" + website + upload_url

        # 2. Unggah file
        files = {"fileToUpload": open(filepath, "rb")}
        data = {"submit": "Unggah File"}  # Ganti dengan nama tombol submit yang sesuai
        response = requests.post(upload_url, files=files, data=data)

        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    website = input("Masukkan nama situs web (contoh: example.com): ")
    filepath = input("Masukkan path file yang akan diunggah: ")

    upload_file(website, filepath)
