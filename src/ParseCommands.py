from os import path, environ
import sys, getopt

def parse_commands():
  """Parse command line arguments arguments

  :return: output_name -> output name vídeo or None

  :return: output_path -> output path vídeo or $Home/Vídeo

  :return: url -> url vídeo or None

  """
  argv = sys.argv[1:]

  home_path = environ.get('HOME')
  path_output = path.join(f"{home_path}/Vídeos")

  output_name: None or str = None
  output_path: None or str = path_output
  url: None or str = None

  try:
    opts, args = getopt.getopt(argv, "u:o:n:", ["url=", "output=", "name="])
  except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

  for opt, arg in opts:
    if opt in ['-u', '--url']:
      url = arg
    elif opt in ['-o', '--output']:
      output_path = arg
    elif opt in ['-n', '--name']:
      output_name = arg

  return output_name, output_path, url
