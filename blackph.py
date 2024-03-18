from PIL import Image

def converter_para_preto_e_branco(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_pb = imagem.convert("L")
    imagem_pb.save("imagem_pb.jpg")

caminho_imagem = "Malu.jpg"
converter_para_preto_e_branco(caminho_imagem)
