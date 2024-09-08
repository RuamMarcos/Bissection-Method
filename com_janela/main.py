import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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
n = float(input("\nε > 10^-n   (n = 0, 1, 2...)\n\nn: "))
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
            msg = f"A raiz exata é x = {xn}"
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
        msg = f"A raiz aproximada é x1 = {xn}"

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
 
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')






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
plt.savefig('tabela.png', dpi=300, bbox_inches='tight')