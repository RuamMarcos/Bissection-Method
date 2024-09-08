import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

# Função que será executada ao apertar o botão
def calcular():
    try:
        # Obtém os valores inseridos pelo usuário
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())

        # Realize a computação (exemplo simples: somas e produto)
        resultado_1 = a + b + n
        resultado_2 = a * b * n
        
        # Gere o primeiro gráfico e salve como PNG
        x = np.linspace(0, 10, 100)
        y1 = a * np.sin(x) + b
        plt.plot(x, y1, label=f'Gráfico 1: {a}*sin(x) + {b}')
        plt.title('Gráfico 1')
        plt.legend()
        plt.savefig('grafico1.png')
        plt.clf()  # Limpa o gráfico para o próximo
        
        # Gere o segundo gráfico e salve como PNG
        y2 = b * np.cos(x) + a
        plt.plot(x, y2, label=f'Gráfico 2: {b}*cos(x) + {a}')
        plt.title('Gráfico 2')
        plt.legend()
        plt.savefig('grafico2.png')
        plt.clf()

        # Carregue e exiba a primeira imagem
        img1 = Image.open("grafico1.png")
        img1 = img1.resize((250, 200), Image.Resampling.LANCZOS)  # Redimensiona a imagem
        img1_tk = ImageTk.PhotoImage(img1)
        label_img1.config(image=img1_tk)
        label_img1.image = img1_tk  # Referência para a imagem

        # Carregue e exiba a segunda imagem
        img2 = Image.open("grafico2.png")
        img2 = img2.resize((250, 200), Image.Resampling.LANCZOS)  # Redimensiona a imagem
        img2_tk = ImageTk.PhotoImage(img2)
        label_img2.config(image=img2_tk)
        label_img2.image = img2_tk  # Referência para a imagem
        
        # Mostre a mensagem do resultado em uma caixa de diálogo
        mensagem = f'Resultado 1: {resultado_1}\nResultado 2: {resultado_2}'
        messagebox.showinfo("Resultado", mensagem)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de PNGs")

# Labels e campos de entrada para os valores de a, b e n
label_a = tk.Label(root, text="Valor de a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Valor de b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_n = tk.Label(root, text="Valor de n:")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Botão para realizar o cálculo
button_calcular = tk.Button(root, text="Calcular e Gerar PNGs", command=calcular)
button_calcular.pack()

# Labels para exibir as imagens
label_img1 = tk.Label(root)
label_img1.pack()

label_img2 = tk.Label(root)
label_img2.pack()

# Inicia o loop da interface gráfica
root.mainloop()
