from moviepy import AudioFileClip
import uuid

def mp4_to_mp3(mp4_filename: str, mp3_filename: str) -> None:

    afc = AudioFileClip(mp4_filename)
    afc.write_audiofile(mp3_filename)      
    afc.close()

if __name__ == "__main__":
    mp4_filename = "video_teste.mp4"
    mp3_filename = uuid.uuid4().hex + ".mp3"

    mp4_to_mp3(mp4_filename=mp4_filename, mp3_filename=mp3_filename)
