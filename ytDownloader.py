import yt_dlp

link = input("youtube link: ")

with yt_dlp.YoutubeDL() as ydl:
    ydl.download([link])