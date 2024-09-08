import tkinter as tk
from tkinter import messagebox
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
        
        # Gere o primeiro gráfico
        x = np.linspace(0, 10, 100)
        y1 = a * np.sin(x) + b
        plt.plot(x, y1, label=f'Gráfico 1: {a}*sin(x) + {b}')
        plt.title('Gráfico 1')
        plt.legend()
        plt.savefig('grafico1.png')
        plt.clf()  # Limpa o gráfico para o próximo
        
        # Gere o segundo gráfico
        y2 = b * np.cos(x) + a
        plt.plot(x, y2, label=f'Gráfico 2: {b}*cos(x) + {a}')
        plt.title('Gráfico 2')
        plt.legend()
        plt.savefig('grafico2.png')
        plt.clf()
        
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

# Inicia o loop da interface gráfica
root.mainloop()
