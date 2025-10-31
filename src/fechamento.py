
import math
from .erosao import erodir
from .dilatacao import dilatar
from utils import aplicar_padding

def fechamento(A_padded, conjunto_B):
    imagem_dilatada = dilatar(A_padded, conjunto_B)
    imagem_dilatada_padded = aplicar_padding(imagem_dilatada, conjunto_B.shape, 
                                            (math.floor(conjunto_B.shape[0]/2), math.floor(conjunto_B.shape[1]/2)))

    imagem_fechamento = erodir(imagem_dilatada_padded, conjunto_B)
    return imagem_fechamento