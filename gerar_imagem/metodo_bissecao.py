from PIL import Image, ImageDraw, ImageFont

# Carregue as imagens necessárias
grafico_img = Image.open("sem_janela/grafico.png")
tabela_img = Image.open("sem_janela/tabela.png")

# Redimensione as imagens para caber na metade esquerda e na metade inferior direita
grafico_img = grafico_img.resize((540, 960), Image.Resampling.LANCZOS)
tabela_img = tabela_img.resize((540, 480), Image.Resampling.LANCZOS)

# Crie a imagem final de 1920x1920
final_img = Image.new("RGB", (1920, 1080), "white")

# Coloque a imagem 'grafico.png' na metade esquerda
final_img.paste(grafico_img, (0, 540))

# Configurações para o texto
titulo = "Método da bisseção"
texto = ("Esse método é utilizado para encontrar as raízes de funções contínuas."
         " Ele se baseia na ideia de dividir o intervalo ao meio repetidamente,"
         " convergindo para a raiz da função com precisão.")

# Defina a fonte e o tamanho (você pode precisar ajustar o caminho para sua fonte)
try:
    fonte_titulo = ImageFont.truetype("arial.ttf", 60)  # Tamanho da fonte do título
    fonte_texto = ImageFont.truetype("arial.ttf", 10)   # Tamanho da fonte do texto
except IOError:
    fonte_titulo = ImageFont.load_default()
    fonte_texto = ImageFont.load_default()

# Desenhe na imagem final
draw = ImageDraw.Draw(final_img)

# Desenhe o título na parte superior direita e o texto
draw.text((550, 50), titulo, font=fonte_titulo, fill="black")
draw.text((50, 550), texto, font=fonte_titulo, fill="black")

# Coloque a imagem 'tabela.png' na metade inferior direita
final_img.paste(tabela_img, (1440, 540))

# Salve a imagem final
final_img.save("imagem_final.png")

# Mostra a imagem (opcional)
final_img.show()
