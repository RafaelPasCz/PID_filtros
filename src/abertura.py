
import math
from .erosao import erodir
from .dilatacao import dilatar
from utils import aplicar_padding

def abertura(A_padded, conjunto_B):
    imagem_erodida = erodir(A_padded, conjunto_B)
    imagem_erodida_padded = aplicar_padding(imagem_erodida, conjunto_B.shape, 
                                            (math.floor(conjunto_B.shape[0]/2), math.floor(conjunto_B.shape[1]/2)))

    imagem_abertura = dilatar(imagem_erodida_padded, conjunto_B)
    return imagem_abertura