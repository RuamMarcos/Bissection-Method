import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image, ImageDraw, ImageFont
import os

def linha():
    print("-"*20)


#Definição da função f(x)
def f(x):
    return x**2 - 16
funcao = 'f(x) = x^2 - 16'


#Recebendo os valores do intervalo [a, b]
print("\n\n  Recebendo o intervalo [a,b]\n")
a = float(input("a: ")) 
b = float(input("b: ")) 
xn = float((a+b)/2)


#Declaração do critério de parada
epsilon = abs(b - a)
linha()


#Demarcando intervalo da tolerância
print("  Tolerância ε")
n = float(input("\nε < 10^-n   (n = 0, 1, 2...)\n\nn: "))
linha()
stop = 10**(-1*n)
 

#Criando os dados da tabela
dataTabela = {
    "n":list(),
    "an":list(),
    "bn":list(),
    "xn":list(),
    "f(xn)":list(),
    "ε":list()
}

n = 0
dataTabela['n'].append(int(n))
dataTabela["an"].append(round(a, 5))
dataTabela["bn"].append(round(b, 5))
dataTabela["ε"].append("--")
dataTabela["xn"].append(xn)
dataTabela["f(xn)"].append(f(xn))

#Calculando o valor aproximado de x1
if(f(a) * f(b) < 0):
    msg = str()
    xn = 0
    while epsilon > stop:

        if(xn != None): epsilon = xn
        
        xn = (b + a)/2
        
        
        epsilon = abs(xn - epsilon) 

        if(f(xn) == 0):
            msg = f"A raiz exata é x = {round(xn, 7)}"
            break

        elif f(a) * f(xn) < 0:
            b = xn
        
        else:
            a = xn

        if(n > 0):
            dataTabela["n"].append(int(n))
            dataTabela["an"].append(round(a, 5))
            dataTabela["bn"].append(round(b, 5))
            dataTabela["ε"].append(round(epsilon,5))
            dataTabela["xn"].append(round(xn, 5))
            dataTabela["f(xn)"].append(round(f(xn), 5))
        n+=1
        msg = f"A raiz aproximada é x1 = {round(xn, 7)}"

    print(msg)
else:
    print("Não há raiz no intervalo pois: ")
    print(f"f(a) * f(b) = {f(a)*f(b)}")
    print(f"f(a)*f(b) >= 0")

linha()
print("\n\n")





#Plotando o gráfico

# Crie um array de valores x
x = np.linspace(a-5, b+5, 400)

#Criando um array dos valores de y
y = f(x)

#Setando a funcao
plt.plot(x, y, label=funcao)

#Configurando algumas coisas no gráfico
plt.title('Gráfico de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='red',linewidth=0.5)  # Linha horizontal no eixo y=0
plt.axvline(0, color='red',linewidth=0.5)  # Linha vertical no eixo x=0
plt.legend()
plt.grid(True)
 
plt.savefig('images/grafico.png', dpi=300, bbox_inches='tight')




#Gerando Tabela
# Crie um DataFrame
df = pd.DataFrame(dataTabela)

# Crie a figura e o eixo
fig, ax = plt.subplots(figsize=(5, 2))  # Tamanho da imagem (largura, altura)

# Oculte o eixo
ax.axis('off')

# Desenhe a tabela no gráfico
tabela = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Ajuste o tamanho da fonte
tabela.auto_set_font_size(False)
tabela.set_fontsize(12)

# Ajuste o tamanho das células
tabela.scale(2, 1.2)

# Salve a tabela como uma imagem PNG
plt.savefig('images/tabela.png', dpi=300, bbox_inches='tight')



#Gerando a imagem sumarizando tudo

# Definir as dimensões da imagem final
img_width, img_height = 2000, 1000
output_img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))

# Definir o diretório atual onde estão as imagens
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos das imagens
grafico_path = os.path.join(current_dir, 'images/grafico.png')
tabela_path = os.path.join(current_dir, 'images/tabela.png')

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
paragraph_text = (f"Tolerância: ε < {stop}\n")
paragraph_text = paragraph_text + msg
draw.text(((img_width // 2) + 100, 300), paragraph_text, font=text_font, fill=(0, 0, 0))

# Salvar a imagem resultante
output_path = os.path.join(current_dir, "images/output_image.png")
output_img.save(output_path)