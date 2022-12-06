import yt_dlp

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3"
    }],
    "outtmpl": "audio/audio.%(ext)s",
    "noplaylist": True
}

def download_from_url(url: str = None):
    urls = [url]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dkM9GxaCow4"
    download_from_url(url)
