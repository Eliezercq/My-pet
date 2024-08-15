import time
import threading
import tkinter as tk
from tkinter import messagebox

class PetVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.felicidade = 50

    def alimentar(self):
        self.felicidade += 10

    def brincar(self):
        self.felicidade += 5

    def exibir_estado(self):
        return f"Nome: {self.nome}\nFelicidade: {self.felicidade}"

    def atualizar_estado(self):
        self.felicidade -= 5

def alimentar_pet():
    pet.alimentar()
    pet.atualizar_estado()
    atualizar_label_estado()

def brincar_com_pet():
    pet.brincar()
    pet.atualizar_estado()
    atualizar_label_estado()

def exibir_estado_pet():
    estado_pet = pet.exibir_estado()
    messagebox.showinfo("Estado do Pet", estado_pet)

def sair():
    root.destroy()

def atualizar_label_estado():
    estado_label.config(text=f"Felicidade: {pet.felicidade}")

if __name__ == "__main__":
    nome_pet = input("Digite o nome do seu pet: ")
    pet = PetVirtual(nome_pet)

    root = tk.Tk()
    root.title("Pet Virtual")

    alimentar_button = tk.Button(root, text="Alimentar", command=alimentar_pet)
    alimentar_button.pack(pady=10)

    brincar_button = tk.Button(root, text="Brincar", command=brincar_com_pet)
    brincar_button.pack(pady=10)

    exibir_estado_button = tk.Button(root, text="Exibir Estado", command=exibir_estado_pet)
    exibir_estado_button.pack(pady=10)

    sair_button = tk.Button(root, text="Sair", command=sair)
    sair_button.pack(pady=10)

    estado_label = tk.Label(root, text=f"Felicidade: {pet.felicidade}")
    estado_label.pack(pady=10)

    def simular_passagem_tempo():
        while True:
            pet.atualizar_estado()
            atualizar_label_estado()
            time.sleep(5)

    tempo_thread = threading.Thread(target=simular_passagem_tempo)
    tempo_thread.daemon = True
    tempo_thread.start()

    root.mainloop()
