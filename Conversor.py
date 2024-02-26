import os
from moviepy.editor import *

def convert_to_mp3(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".mp4"):
            try:
                video = VideoFileClip(os.path.join(input_folder, file))
                audio = video.audio
                audio.write_audiofile(os.path.join(output_folder, file[:-4] + ".mp3"))
                audio.close()
            except Exception as e:
                print(f"Failed to process file: {file}. Error: {e}")

# Defina a pasta de entrada e a pasta de saída
input_folder = "C:/Users/igorh/Desktop/Videos"
output_folder = "C:/Users/igorh/Desktop/Audios"

# Chame a função para converter os arquivos
convert_to_mp3(input_folder, output_folder)
