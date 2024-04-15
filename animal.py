class Animal:
    def __init__(self, nome, idade, especie, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.som = som

    def emite(self):
        return f"{self.especie} emite o som: {self.som}"
    def informacoes(self):
        return f"informações sobre {self.nome} são: {self.especie} e {self.idade}"
    
if __name__ == "__main__":
    animal1 = Animal("Mel", "10 Anos", "Cachorro", "Latir")

print(animal1.emite())
print(animal1.informacoes())