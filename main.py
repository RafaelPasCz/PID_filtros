import sys
import matplotlib.pyplot as plt
import numpy as np
from utils import * 
from src import *

def plotar(img, nome):

    fig, ax = plt.subplots()
    
    ax.imshow(img, cmap='gray')
    
    ax.axis('off')
    
    plt.tight_layout()
    
    plt.savefig(f"./{nome}.png")
    
    plt.show()


if len(sys.argv) != 2:
    raise ValueError("Uso: main.py <nome da imagem>")

mat_estruturante = [

[1, 1, 1],
[1, 1, 1],
[1, 1, 1]

]

conjunto_A = binarizar(sys.argv[1])

conjunto_B, origem_B = definir_conjunto_estruturante(mat_estruturante)

plotar(conjunto_A, "imagem_original")

imagem_padding = aplicar_padding(conjunto_A, conjunto_B.shape, origem_B)

plotar(imagem_padding, "imagem_com_padding")

imagem_erodida = erodir(imagem_padding, conjunto_B)

plotar(imagem_erodida, "imagem_erodida")

imagem_dilatada = dilatar(imagem_padding, conjunto_B)

plotar(imagem_dilatada, "imagem_dilatada")

imagem_abertura = abertura(imagem_padding, conjunto_B)

plotar(imagem_abertura, "imagem_abertura")

imagem_fechamento = fechamento(imagem_padding, conjunto_B)

plotar(imagem_fechamento, "imagem_fechamento")



