#sucessor e antecessor de um numero

num = input("escreva um numero: ")#retorna uma string

antecessor = 0 
sucessor = 0

try:
    antecessor = int(num) - 1 
    sucessor = int(num) + 1
except ValueError:
    raise ValueError("Digite um numero valido")
    print("Digite um numero valido")

print(f"O numero é {num} e o sucessor é {sucessor} e o antecessor é {antecessor}.")




