import os
from yt_dlp import YoutubeDL

# Fungsi untuk membaca URL dari file txt
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls if url.strip()]
    return urls

# Path file txt yang berisi URL
url_file_path = 'urls.txt'

# Membaca URL dari file
video_urls = read_urls_from_file(url_file_path)

def download_video(url, save_path='./downloads'):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'best'
    }
    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading: {url}")
            ydl.download([url])
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

# Buat folder 'downloads' jika belum ada
if not os.path.exists('./downloads'):
    os.makedirs('./downloads')

# Download semua video
for url in video_urls:
    download_video(url)

print("All videos have been downloaded.")
