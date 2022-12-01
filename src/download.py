from os import path, mkdir

from pytube import YouTube

from src import ParseCommands
import src.progress as progress

def downloadYoutubeVideos():
  name, path_out, url = ParseCommands.parse_commands()

  yt = YouTube(url)
  video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().get_highest_resolution()

  if not path.exists(path_out):
    mkdir(path_out)

  yt.register_on_progress_callback(progress.OnProgress)
  print(f"Fetching \"{video.title}\"..")
  print(f"Fetching successful\n")
  print(f"Information: \n"
        f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
        f"Highest Resolution: {video.resolution}\n")

  print(f"Downloading \"{video.title}\"..")

  path_output = path.join(f"{path_out}/{name}")

  print(f"Downloading from path \"{path_output}\"..")
  video.download(path_output, name)
