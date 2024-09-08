import numpy as np
import matplotlib.pyplot as plt

# Defina a função f(x)
def f(x):
    return x**2  # Exemplo: f(x) = x^2

# Crie um array de valores x
x = np.linspace(-10, 10, 400)  # 400 pontos entre -10 e 10

# Calcule os valores correspondentes de y = f(x)
y = f(x)

# Plote o gráfico
plt.plot(x, y, label='f(x) = x^2')

# Personalize o gráfico
plt.title('Gráfico de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)  # Linha horizontal no eixo y=0
plt.axvline(0, color='black',linewidth=0.5)  # Linha vertical no eixo x=0
plt.legend()
plt.grid(True)

# Mostre o gráfico
plt.savefig('grafico_funcao.png', dpi=300, bbox_inches='tight')