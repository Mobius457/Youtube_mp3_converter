
import yt_dlp
import os


def convert_youtube_to_mp3():
    """
    Prompts the user for a YouTube URL and downloads the audio as an MP3 file using yt-dlp.
    """
    video_url = input("Please enter the YouTube video URL: ")
    try:
        print("Downloading and converting to MP3...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,
            'quiet': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([video_url])
        print("\n✅ Success! Your MP3 is ready in the current folder.")
    except Exception as e:
        print("\n❌ An error occurred. Please check the URL and your internet connection.")
        print(f"Error details: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
    convert_youtube_to_mp3()