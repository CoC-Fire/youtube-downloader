import os
import yt_dlp

playlist_url = input("Please enter your playlist url: ")
folder_path = input("Please enter the preferred folder to put songs in (use the relative path or the program will break): ")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

ytdl_opts = {
    "format": "bestaudio/best",
    "outtmpl": folder_path + "/%(title)s.%(ext)s",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "0"
    }],
    "ignoreerrors": True,
    "skip_download": False
}

with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
    info_dict = ydl.extract_info(playlist_url, download=False)
    playlist_length = len(info_dict["entries"])

os.system("title Downloading playlist...")
print("Downloading song 1 of " + str(playlist_length))

with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
    for i, entry in enumerate(ydl.extract_info(playlist_url, download=True)):
        print("Downloading song " + str(i + 1) + " of " + str(playlist_length))

os.system("title Cleaning up...")
for file in os.listdir(folder_path):
    if file.endswith(".part"):
        print("Removing residual .part file")
        os.remove(os.path.join(folder_path, file))

os.system("title Removing duplicates...")
files = {}
for file in os.listdir(folder_path):
    if file.endswith(".mp3"):
        if file in files:
            print("Removing duplicate file...")
            os.remove(os.path.join("musicmp3", file))
        else:
            files[file] = True

os.system("title Completed!")
input("Completed! Press enter to close the program...")
exit()
