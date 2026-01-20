class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def emitir_som(self):
        return "O animal emitiu um som genérico."
class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro latiu!"
class Gato(Animal):
    def emitir_som(self):
        return "O gato miou!"
cachorro = Cachorro("Akira", 2)
gato = Gato("Tereza", 6)
print(cachorro.emitir_som())
print(gato.emitir_som())