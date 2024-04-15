class Carros:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"{self.modelo} o carro está ligado"
    def desligar(self):
        return f"{self.modelo} o carro está desligado"
    def acelerar(self):
        return f"{self.modelo} o carro está acelerando"
    
if __name__ == "__main__":
    carro1 = Carros("Fiat", "Palio", "2012", "Azul")

print(carro1.ligar())
print(carro1.desligar())
print(carro1.acelerar())