import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Exemplo de dados
dados = {
    'Coluna 1': [10, 20, 30],
    'Coluna 2': [15, 25, 35],
    'Coluna 3': [20, 30, 40]
}

# Crie um DataFrame
df = pd.DataFrame(dados)

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
tabela.scale(2.0, 1.2)

# Salve a tabela como uma imagem PNG
plt.savefig('tabela.png', dpi=300, bbox_inches='tight')