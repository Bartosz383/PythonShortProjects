import yt_dlp
import os

# Adres playlisty
playlist_url = "https://www.youtube.com/playlist"

# Folder docelowy (zmień na swój)
output_folder = r"C:\Users\"

# Tworzymy folder, jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# Ustawienia pobierania
ydl_opts = {
    'ffmpeg_location': r"C:\ffmpeg",
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'socket_timeout': 30,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': False,
    'retries': 10,
    'playliststart': 42,  # zaczyna pobierać od 14. filmu
    'ignoreerrors': True, # pomija błędy i kontynuuje
}

# Pobieranie
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Pobieranie zakończone!")
