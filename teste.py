import time

def saltitante(x):
    lista = list(str(x))
    return not (aumentando(lista) or diminuindo(lista))

def aumentando(y):
    return sorted(y) == y

def diminuindo(z):
    return sorted(z, reverse=True) == z
    

def funcao_solucao():
    x = 1     
    contador = 0 

    while contador * 100 / x != 99:
        contador += bool(saltitante(x))
        x = x + 1

    return x

if __name__ == "__main__":
    inicio = time.time()
    funcao_solucao()
    fim = time.time()    
    print ("O resultado eh: ", funcao_solucao())
    print("O tempo gasto foi de: ", fim - inicio)