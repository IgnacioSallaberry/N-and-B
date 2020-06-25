# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:20:24 2020

@author: Ignacio Sallaberry
"""

### Como pasar imagenes lsm a grayscale y guardarlas como tiff ---->  https://imagej.net/_images/0/0e/LSM-split-howto.pdf

### Como manipular muchas imagenes TIFF con python ----> https://recalll.co/ask/v/topic/Split-multi-page-tiff-with-python/559241707d3563af728b5a04

### Como guardar solo un unico slice de todas las tiff ----> Use the Image > Duplicate... command (control+D) to duplicate the current image plane, then save that as TIFF using the File > Save As > Tiff... command.
### fuente: http://imagej.1557.x6.nabble.com/Saving-current-slice-as-tif-td5005001.html



from skimage import io

from PIL import Image
from graficos import *
imagen = Image.open(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\RFP citoplasmática\Image0027.tif.frames\Image0027_C001T001.tif')

imagen = np.array(imagen)


imagen = io.imread(r'C:\Users\ETCasa\Nextcloud\Datos Alexis NandB DENGUE y Zika\mCherry\mcherry_3hs_cell2_pcor_nucleo2\CH2 CaAsP- mcherry_3hs_cell2_pcor_nucleo2.tif')

path = r'C:\Users\ETCasa\Nextcloud\Datos Alexis NandB DENGUE y Zika\mCherry\mcherry_3hs_cell2_pcor_nucleo2\CH2 CaAsP- mcherry_3hs_cell2_pcor_nucleo2.tif'
with Image.open(path) as image_file:
    img_0 = image_file.seek(0)

import matplotlib.pyplot as plt
plt.imshow(img_0)
plt.show()

### abro TODO el set de imagenes que guardé en formato TIF
img = Image.open(r'C:\Users\ETCasa\Nextcloud\Datos Alexis NandB DENGUE y Zika\mCherry\mcherry_3hs_cell2_pcor_nucleo2\CH2 CaAsP- mcherry_3hs_cell2_pcor_nucleo2.tif')



## elijo la primera imagen y la paso a formato int
img_0 = img.asarray(key=0)

img_0 = np.array(img.seek(145))
img_0 = (np.array(img)/2).astype(int)

## guardé solamente la primer imagen del imageJ y la abro
imageJ = Image.open(r'C:\Users\ETCasa\Nextcloud\Datos Alexis NandB DENGUE y Zika\mCherry\mcherry_3hs_cell2_pcor_nucleo2\slice1 - CH2 CaAsP- mcherry_3hs_cell2_pcor_nucleo2-1.tif')
imageJ = (np.array(imageJ)/2).astype(int)

## grafico primer slice del set de imagenes
plt.figure()
plt.imshow(img_0)
plt.xlabel(r'píxel')
plt.ylabel(r'píxel')
plt.title('slice 0 - python')
plt.show()

## grafico slice 0 que separé con el image J
plt.figure()
plt.imshow(imageJ)
plt.xlabel(r'píxel')
plt.ylabel(r'píxel')
plt.title('slice 0 - imageJ')
plt.show()

## calculo la resta entre tomar el slice 0 del set de imagenes y el slice 0 que me guardé del imageJ y la grafico.
resta_de_slice = img_0 - imageJ
ax = plot_signal(resta_de_slice,r'píxel',r'Resta', 'Resta de slice')
ax.plot(resta_de_slice)
plt.tight_layout()
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.e'))
plt.show()
