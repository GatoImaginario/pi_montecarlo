# Importar módulos
from tkinter import *
from time import sleep
from random import randint as ran

tamanho = 500

# Window
window = Tk()
window.title('Calculando Pi')
window.geometry('{}x{}'.format(tamanho, int(tamanho*1.2)))
window.resizable(False, False)

# Widgets
canvas = Canvas(window, width=tamanho, height=tamanho, bg = 'black')
canvas.pack()

nPontos = Entry(window)
nPontos.pack(side=BOTTOM, pady=10)

display = Label(window, text= ' ')
display.pack(side=BOTTOM)

# Função
def calcularPi():
    canvas.delete('all')

    # Variáveis
    raio = tamanho/2
    pontoDentro = 0
    pontoTotal = 0

    # Círculo
    circulo = canvas.create_oval(0, 0, tamanho, tamanho, outline='#7d0101', width=2)

    # Loop
    inputUsuario = nPontos.get()
    for i in range(int(inputUsuario)):

        # Gerar coordenadas
        coordx = ran(0, tamanho)
        coordy = ran(0, tamanho)

        # Mostrar pontos
        canvas.create_oval(coordx, coordy, coordx, coordy, outline='#bdc1c9', width=2)

        # Checar onde caiu
        dist = ((raio - coordx)**2 + (raio - coordy)**2)**0.5
        pontoTotal += 1
        if dist <= raio:
            pontoDentro += 1

        # Calcular pi
        pi = 4*pontoDentro/pontoTotal

        # Exibir valor
        display.config(text='{:.5f}'.format(pi))
        sleep(0.01)
        canvas.update()

    canvas.itemconfig(circulo, outline='#75a158')

# Finalizar programa
iniciar = Button(window, text='Iniciar', command=calcularPi)
iniciar.pack()

window.mainloop()
