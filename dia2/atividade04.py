velocidade = input("A velocidade do carro é: ")

velocidade_valida = 0

try:
    velocidade_valida = int(velocidade)
except ValueError:
    raise ValueError("Digite apenas numeros")
if velocidade_valida > 80 :
    print(f"Você foi multado{velocidade_valida}")
    print(f"multa{(velocidade_valida - 80) * 7}")

elif velocidade_valida == 80 :
    print("velocidade limite")

else:
    print("Voce esta longe de ultrapassar a velocidade")