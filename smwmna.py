import os
from pydub import AudioSegment

def convert_to_wma(input_folder, output_folder):
    # Verifica se a pasta de saída existe, caso contrário, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorre todos os arquivos na pasta de entrada
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp3"):
            # Carrega o arquivo MP3
            mp3_path = os.path.join(input_folder, file_name)
            audio = AudioSegment.from_mp3(mp3_path)

            # Define o nome do arquivo de saída no formato WMA
            wma_file_name = file_name.replace(".mp3", ".wma")
            wma_path = os.path.join(output_folder, wma_file_name)

            # Salva o arquivo no formato WMA
            audio.export(wma_path, format="wma")

            print(f"Arquivo convertido: {wma_file_name}")

# Pasta de entrada com os arquivos MP3
input_folder = "C:/Users/igorh/Desktop/Audios"

# Pasta de saída para os arquivos WMA
output_folder = "C:/Users/igorh/Desktop/Audios_WMA"

# Chama a função para converter os arquivos
convert_to_wma(input_folder, output_folder)