
def linha():
    print("\n")
    print("-"*10)

#Definição da função f(x)
def f(x):
    return x**2 - 4


#Recebendo os valores do intervalo [a, b]
a = float(input("a: ")) 
b = float(input("b: ")) 

#Declaração do critério de parada
epsilon = b - a
linha()

#Demarcando intervalo da tolerância
n = float(input("\nε > 10^-n   (n = 0, 1, 2...)\n\nn: "))
linha()
stop = 10**(-1*n)
 

if(f(a) * f(b) < 0):

    while epsilon > stop:
        x = (b + a)/2

        if(f(x) == 0):
            print(f"f({x}) = {f(x)}")
            break

        elif f(a) * f(x) < 0:
            b = x
        
        else:
            a = x

        epsilon = abs(f(x))
        print(f"f({x}) = {f(x)}")

else:
    print("Não há raiz no intervalo pois: ")
    print(f"f(a) * f(b) = {f(a)*f(b)}")
    print(f"f(a)*f(b) >= 0")

linha()