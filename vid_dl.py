import sys
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter

import os
import urllib.request

SAVE_PATH = "./save"

def Download(link, save_path):
    youtubeObject = YouTube(link)

    # Download the thumbnail
    try:
        thumbnail = youtubeObject.thumbnail_url
        urllib.request.urlretrieve(thumbnail, f"{save_path}/thumbnail.jpg")
    except Exception as e:
        print("An error has occurred while downloading the thumbnail:", e)
        return
    
    # Download the video
    try:
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download(output_path=save_path)
    except Exception as e:
        print("An error has occurred while downloading the video:", e)
        return

    # Download the subtitle
    try:
        video_id = link.split("/")[-1]  # Extract video ID from URL
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])

        formatter = SRTFormatter()

        srt_formatted = formatter.format_transcript(transcript)

        with open(f"{save_path}/subtitle.srt", 'w', encoding='utf-8') as subtitle_file:
            subtitle_file.write(srt_formatted)
    except Exception as e:
        print("An error has occurred while downloading the subtitle:", e)
        return

    print("Download is completed successfully")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <lang>")
        sys.exit(1)
    
    url = sys.argv[1]
    lang = sys.argv[2]

    print(url)
    Download(url, SAVE_PATH)
