# Fingerprint Tools
Essa biblioteca apresenta ferramentas para pré-processamento de impressões digitais. 

É necessário ter o OPEN CV instalado.


# # anguloCalc(imagem,w)

Calcula a orientação preferencias de cada janela de tamanho w da imagem. Calcula também a magnitide da orientação em cada janela
imagem - pode ser RGB (3 canais) ou GRAY (1 canal)
w - tamanho da janela (valor default 10)
 
Sintaxe:  D,Mag = anguloCalc(img,w = 7)

# # OrietationFigure(img,D,w, Mag)

Plota uma figura com o mapa de orientações sobreposto.
img - pode ser RGB (3 canais) ou GRAY (1 canal)
D - mapa de orientações
w - tamanho da janela (default 10)
Mag - magnitude. Se vazio será utilizado um valor unitário (default) 
Sintaxe:  D,Mag = anguloCalc(img,w = 7)

# # averageOrientation(orientations, weights=None, deviation=False)

Calcula a média do mapa de orientações
 
Sintaxe:  D = averageOrientation(D)

# Referências bibliográficas 
Hong, Lin; Wan, Yifei; Jain, Anil: Fingerprint image enhancement: Algorithm and performance evaluation. IEEE transactions on pattern analysis and machine intelligence, 20(8):777–789, 1998.

Sherlock, BG; Monro, DM; Millard, K: Fingerprint enhancement by directional Fourier filtering. IEE Proceedings-Vision, Image and Signal Processing, 141(2):87–94, 1994.

Wahab, A; Chin, SH; Tan, EC: Novel approach to automated fingerprint recognition. IEE Proceedings-Vision, Image and Signal Processing, 145(3):160–166, 1998.
