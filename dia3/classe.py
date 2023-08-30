from abc import ABC, abstractmethod

class IAnimal: 
    

    @abstractmethod
    def falar(self):
        """defina na classe filha"""
    @abstractmethod
    def andar(self):
        """dafina na classe filha"""

class Cachorro(IAnimal):
    def falar(self):
        print("AuAu")
    def andar(self):
        print("Ando com quatro patas")

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self.__humano = True
    def fala_pessoa(self):
        print("Falando")

#animal = cachorro
pingo = Cachorro()
pingo.falar()
pingo.andar()



