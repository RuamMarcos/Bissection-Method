import numpy as np
import matplotlib.pyplot as plt


def linha():
    print("-"*20)

#Definição da função f(x)
def f(x):
    return x**2 - 4 
funcao = 'f(x) = x^2 - 4'

#Recebendo os valores do intervalo [a, b]
print("\n\n  Recebendo o intervalo [a,b]\n")
a = float(input("a: ")) 
b = float(input("b: ")) 
xn = float()



#Declaração do critério de parada
epsilon = abs(b - a)
linha()




#Demarcando intervalo da tolerância
print("  Tolerância ε")
n = float(input("\nε > 10^-n   (n = 0, 1, 2...)\n\nn: "))
linha()
stop = 10**(-1*n)
 

if(f(a) * f(b) < 0):
    msg = str()
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
