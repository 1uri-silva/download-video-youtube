from pytube import Stream

def OnProgress(stream: Stream, chunk: bytes, bytes_remaining: int):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  percentage_of_completion = bytes_downloaded / total_size * 100

  percentage_split = str(percentage_of_completion)
  print(f"\n {percentage_split.split('.')[0]}%")
