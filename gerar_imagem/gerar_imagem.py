from PIL import Image, ImageDraw, ImageFont
import os

# Definir as dimensões da imagem final
img_width, img_height = 2000, 1000
output_img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))

# Definir o diretório atual onde estão as imagens
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos das imagens
grafico_path = os.path.join(current_dir, 'grafico.png')
tabela_path = os.path.join(current_dir, 'tabela.png')

# Carregar as imagens 'grafico.png' e 'tabela.png'
grafico = Image.open(grafico_path)
tabela = Image.open(tabela_path)

# Redimensionar as imagens para se ajustarem às suas respectivas áreas
grafico_resized = grafico.resize((img_width // 2, img_height))
tabela_resized = tabela.resize((img_width // 2, img_height // 2))

# Colocar a imagem do gráfico na metade esquerda
output_img.paste(grafico_resized, (0, 0))

# Colocar a imagem da tabela na parte inferior direita
output_img.paste(tabela_resized, (img_width // 2, img_height // 2))

# Configurar o título e o texto
draw = ImageDraw.Draw(output_img)

# Carregar a fonte TrueType para aumentar o tamanho da fonte (escolha o caminho correto para a fonte)
title_font = ImageFont.truetype("arial.ttf", 80)  # Título com tamanho 80
text_font = ImageFont.truetype("arial.ttf", 40)  # Texto com tamanho 40

# Usar textbbox para obter o tamanho do título
title_text = "Método da Bisseção"
title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
title_width = title_bbox[2] - title_bbox[0]

# Centralizar o título na metade direita superior
draw.text(((img_width // 2) + (img_width // 4) - (title_width // 2), 100), title_text, font=title_font, fill=(0, 0, 0))

# Adicionar o parágrafo abaixo do título
paragraph_text = ("O método da bisseção é uma técnica iterativa utilizada para encontrar raízes de funções contínuas. "
                 "Ele se baseia na escolha de dois pontos em que o sinal da função muda e divide o intervalo ao meio, "
                 "repetindo o processo até que a raiz seja aproximada com precisão suficiente.")
draw.text(((img_width // 2) + 100, 300), paragraph_text, font=text_font, fill=(0, 0, 0))

# Salvar a imagem resultante
output_path = os.path.join(current_dir, "output_image.png")
output_img.save(output_path)

print(f"Imagem gerada com sucesso em {output_path}")
