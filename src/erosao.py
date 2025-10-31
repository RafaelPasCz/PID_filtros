
import numpy as np
import math

def erodir(A_padded, conjunto_B):
    #A_padded : numpy array, conjunto_B: numpy array
    #recebe a imagem ja com padding e o conjunto estruturante

    #obtemos as dimensões e origem do elemento estruturante
    (altura_pad, largura_pad) = A_padded.shape
    (altura_B, largura_B) = conjunto_B.shape
    
    origem_r = math.floor(altura_B / 2)
    origem_c = math.floor(largura_B / 2)

    #calculamos as dimensões sem padding para a imagem de saída
    pad_topo = origem_r
    pad_base = (altura_B - 1) - origem_r
    pad_esq = origem_c
    pad_dir = (largura_B - 1) - origem_c

    #o tamanho original é o tamanho com padding menos o padding
    altura_A = altura_pad - pad_topo - pad_base
    largura_A = largura_pad - pad_esq - pad_dir

    #criamos a base para a imagem de saída, com as dimensões originais
    imagem_erodida = np.zeros((altura_A, largura_A), dtype=np.uint8)

    #Iteramos sobre cada pixel (r, c) da imagem original.
    #(r, c) representa a posição onde a origem de B seria colocada
    #na imagem original.
    
    for r in range(altura_A):
        for c in range(largura_A):
            
            #da imagem com padding (A_padded), pegamos a "vizinhança"
            #que está "embaixo" do ES.
            sub_janela = A_padded[r : r + altura_B, c : c + largura_B]
            
            #aplicar a Lógica: "B completamente contido em A" 
            #Vamos iterar o ES para verificar a condição.
            
            #começamos assumindo que é um fit 
            houve_falha = False 
            
            
            for br in range(altura_B):
                for bc in range(largura_B):
                    
                
                    #se o pixel do ES for '1' (frente) 
                    #E 
                    #o pixel correspondente na sub-janela for '0' (fundo)
                    if (conjunto_B[br, bc] == 1) and (sub_janela[br, bc] == 0):
                        #é um "miss"
                        houve_falha = True
                        break #não precisamos checar o resto do ES
                
                if houve_falha:
                    break #sai do loop de linhas também
            
            #se, após checar todo o ES, não houve falha
            if not houve_falha:
                #é um fit. 
                #o pixel de saída (r, c) se torna 1.
                imagem_erodida[r, c] = 1
            
    return imagem_erodida