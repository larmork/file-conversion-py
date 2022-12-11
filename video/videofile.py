import moviepy.editor
from pathlib immport Path

video_file = Path(input("video file: "))

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')