import numpy as np
import math

def dilatar(A_padded, conjunto_B):

    (altura_pad, largura_pad) = A_padded.shape
    (altura_B, largura_B) = conjunto_B.shape
    
    origem_r = math.floor(altura_B / 2)
    origem_c = math.floor(largura_B / 2)
    
    pad_topo = origem_r
    pad_base = (altura_B - 1) - origem_r
    pad_esq = origem_c
    pad_dir = (largura_B - 1) - origem_c

    altura_A = altura_pad - pad_topo - pad_base
    largura_A = largura_pad - pad_esq - pad_dir
   
    imagem_dilatada = np.zeros((altura_A, largura_A), dtype=np.uint8)

    for r in range(altura_A):
        for c in range(largura_A):
            
            sub_janela = A_padded[r : r + altura_B, c : c + largura_B]

            # Começamos assumindo que NÃO é um fit
            houve_acerto = False 
            
            # Loop sobre o Elemento Estruturante 
            for br in range(altura_B):
                for bc in range(largura_B):
                    
                    # Verificamos a condição de acerto:
                    # Se o pixel do ES for '1' (frente)
                    # E
                    # o pixel correspondente na sub-janela for '1' (frente)
                    if (conjunto_B[br, bc] == 1) and (sub_janela[br, bc] == 1):
                        # É um "acerto" (hit).
                        houve_acerto = True
                        break # Não precisamos checar o resto do ES
                
                if houve_acerto:
                    break # Sai do loop de linhas também
            
            # Se, após checar todo o ES, houve PELO MENOS UM acerto
            if houve_acerto:
                # O pixel de saída (r, c) se torna 1.
                imagem_dilatada[r, c] = 1
            # Se não houve acertos (else), o pixel de saída permanece 0.
            
    print("Processamento de Dilatação concluído.")
    return imagem_dilatada