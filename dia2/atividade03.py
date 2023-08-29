#idade para tirar CNH
idade = input("Escreva sua idade: ")
#variavel
idade = 0
# checa se é possivel fazer o casting
try: 
    idade = int(idade)
except ValueError:
    raise ValueError("Digite novamente")
if idade < 18 :
    print ("você não pode ter CNH")

else :
    print("Você esta apto a ter CNH")