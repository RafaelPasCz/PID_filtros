import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def aplicar_padding(imagem, formato_es, origem_es):
    #imagem: numpy array, formato_es: tupla(x,y), origem_es: tupla(x,y)

    #obter as dimensoes da imagem, do estruturante e seu centro (origem)
    (altura_A, largura_A) = imagem.shape
    (altura_B, largura_B) = formato_es
    (origem_r, origem_c) = origem_es

    #calculamos o padding de acordo com os dados da estruturante
    #faz o calculo com base no formato do estruturante e de sua origem
    pad_topo = origem_r
    pad_base = (altura_B - 1) - origem_r
    pad_esq = origem_c
    pad_dir = (largura_B - 1) - origem_c

    #novas dimensões da imagem com padding
    nova_altura = altura_A + pad_topo + pad_base
    nova_largura = largura_A + pad_esq + pad_dir
    
    #cria uma nova imagem em branco (tudo zero)
    imagem_com_padding = np.zeros((nova_altura, nova_largura), dtype=np.uint8)
    
    #copia a imagem original para a base com padding, preservando o tamanho original
    imagem_com_padding[pad_topo : pad_topo + altura_A, 
                       pad_esq : pad_esq + largura_A] = imagem
    
    return imagem_com_padding


def binarizar(img):
    #img : path para imagem
    #plt.imread retorna um array numpy bidimensional
    imagem_carregada = plt.imread(img)
    
    
    #se for colorida (ex: RGB), converte para tons de cinza primeiro
    if imagem_carregada.ndim == 3:

        #seleciona o canal de cor da imagem, pegando os três valores RGB (o :3 trata casos RGBA)
        #em seguida faz um produto vetorial com os valores da fórmula padrão NTSC
        #dessa forma, para cada valor RGB de um pixel, o resultante em grayscale
        #será igual r * 0.2989 + g * 0.5870 + b * 0,1140 
        imagem_cinza = np.dot(imagem_carregada[...,:3], [0.2989, 0.5870, 0.1140])

    else:

        imagem_cinza = imagem_carregada

    #normaliza a imagem para o intervalo 0-1 
    if np.max(imagem_cinza) > 1.0:
        imagem_cinza = imagem_cinza / 255.0

    #vamos usar o valor médio de intensidade da imagem como limiar para a binarização
    limiar = np.mean(imagem_cinza)

    #salva todos os pixels da imagem, como True se é maior que o limiar, e False se menor
    #em seguida salva como número, True vira 1 e False vira 0    
    conjunto_A = (imagem_cinza > limiar).astype(np.uint8)

    return conjunto_A



def definir_conjunto_estruturante(mat):
    #mat : matriz (lista de listas)

    conjunto_B = np.array(mat, dtype=np.uint8)

    formato = conjunto_B.shape
    #para facilitar a vida na hora de achar o centro do elemento estruturante
    #assumimos que o centro é o ponto médio de sua altura e largura (arredondado para baixo)

    origem_B = (math.floor(formato[0]/2), math.floor(formato[1]/2))

    return conjunto_B, origem_B

