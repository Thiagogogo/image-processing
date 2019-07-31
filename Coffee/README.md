# Coffee Tools
Essa biblioteca apresenta ferramentas para pré-processamento de imagens aplicado a cultura do café 
É necessário ter o OPEN CV instalado.


## Severidade

Ferramentas relacionadas com o cálculo do índice de severidade de pragas e doenças que atacam a folha do café
Necessária a utilização da biblioteca OpenCV

__init__(self, image_file,scale = 100)
        image_file: caminho da imagem. Pode ser do tipo TIF, PNG, JPG
        scale = 0 a 100: valor de redução de escala em porcentagem (default 100%)

imshow()
        apresenta em uma janela do OpenCV a imagem 

resize(self, rows = 800, collumns = 600, interpol = cv2.INTER_CUBIC)
        redimensiona a imagem através de linhas e colunas
        rows - linhas
        collumns - colunas
        interpolation - cv2.INTER_CUBIC
                         - cv2.INTER_AREA for shrinking
                         - cv2.INTER_CUBIC (zoom) (slow)
                         - cv2.INTER_LINEAR (zoom)
                         - cv2.INTER_NEAREST



# Referências bibliográficas 

