import sys
import matplotlib.pyplot as plt
import numpy as np
from utils import * 
from src import *


def plotar(img, est):
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotar Conjunto A (Imagem Carregada e Binarizada)
    axes[0].imshow(img, cmap='gray')
    axes[0].set_title("Conjunto A (Imagem Binarizada)")
    # Adiciona uma grade (útil para imagens pequenas)
    # Se a imagem for grande, a grade ficará muito densa.
    if max(img.shape) < 50:
        axes[0].set_xticks(np.arange(-.5, img.shape[1], 1), minor=True)
        axes[0].set_yticks(np.arange(-.5, img.shape[0], 1), minor=True)
        axes[0].grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

    # Plotar Conjunto B (Elemento Estruturante)
    axes[1].imshow(est, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
    axes[1].set_title("Conjunto B (ES)")
    # Destaca a origem
    axes[1].set_xticks(np.arange(-.5, 3, 1), minor=True)
    axes[1].set_yticks(np.arange(-.5, 3, 1), minor=True)
    axes[1].grid(which='minor', color='blue', linestyle='-', linewidth=0.5)

    plt.tight_layout()
    plt.show()



mat_estruturante = [

[0, 1, 0],
[1, 1, 1],
[0, 1, 0]

]

conjunto_A = binarizar(sys.argv[1])



conjunto_B, origem_B = definir_conjunto_estruturante(mat_estruturante)

plotar(conjunto_A, conjunto_B)

imagem_padding = aplicar_padding(conjunto_A, conjunto_B.shape, origem_B)

plotar(imagem_padding, conjunto_B)

imagem_erodida = erodir(imagem_padding, conjunto_B)

plotar(imagem_erodida, conjunto_B)

imagem_dilatada = dilatar(imagem_padding, conjunto_B)

plotar(imagem_dilatada, conjunto_B)




