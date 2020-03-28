# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:06:58 2020

@author: Ignacio Sallabery
"""
import numpy as np
from PIL import Image

import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
#==============================================================================
#                                Tipografía de los gráficos
#==============================================================================    
SMALL_SIZE = 28
MEDIUM_SIZE = 32
BIGGER_SIZE = 34
plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#==============================================================================    
#==============================================================================    
plt.close('all')

#==============================================================================
#                                CALIBRACION DE DETECTOR
#==============================================================================    
detector_offset = 0
S_factor = 1
sigma_cero = 0

#detector_offset = 0.197
#S_factor = 4.008
#sigma_cero = 0.002


##==============================================================================
##
##                                    mRFP
##
##==============================================================================    


####  ------------------------    PARA UNA IMAGEN    -------------------
im = Image.open(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\RFP citoplasmática\Image0027.tif.frames\Image0027_C001T001.tif')   #importa la imagen .tif
im = np.array(im) #crea una matriz de valores de la imagen importada
imarray = [im.tolist()]
####  ------------------------    armo los nombres de los archivos    -------------------
i=2
indice=[]
while i<101:
    if i<10:
        indice.append(f'00{i}')
    elif 9<i<100:
        indice.append(f'0{i}')
    else:
        indice.append(f'{i}')
    i+=1
####  ------------------------    armo array con las matrices de las 100 imágenes  -------------------
i=1
while i<len(indice):
    im = Image.open(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\RFP citoplasmática\Image0027.tif.frames\Image0027_C001T{}.tif'.format(indice[i]))   #importa la imagen .tif
    im = np.array(im) #crea una matriz de valores de la imagen importada
    imarray.append(im.tolist())
    print(i)    
    i+=1
imarray = np.array(imarray)

STD = np.std(imarray, axis=0)
k_medio = np.mean(imarray, axis=0)
B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
B = B.ravel()   #esto hace que el array de matrices se haga simplemente una array de valores del brillo


#STD[0][0]**2/N[0][0] == B[0][0]
#STD[0][1]**2/N[0][1] == B[0][1]
#STD[1][0]**2/N[1][0] == B[1][0]

bineado = 5000
plt.figure(1)
#bineado = 'fd'
n,bin_positions_ajuste,p  = plt.hist(B, bins=bineado, color='lightsalmon', density=False)    #esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p
bin_size_ajuste=bin_positions_ajuste[1]-bin_positions_ajuste[0] # calculo el ancho de los bins del histograma
plt.title('mRFP')
plt.tick_params(which='minor', length=5, width=2)
plt.tick_params(which='major', length=7, width=3)
plt.xlim(0,80)
plt.ylim(1,5000)
plt.yscale('log')
#figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
#figManager.window.showMaximized()   
plt.show()


##==============================================================================
##
##                                    M6a - mRFP
##
##==============================================================================    
im = Image.open(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\M6a RFP\Image0020.tif.frames\Image0020_C001T001.tif')   #importa la imagen .tif
im = np.array(im) #crea una matriz de valores de la imagen importada
imarray = [im.tolist()]
i=1
while i<len(indice):
    im = Image.open(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\M6a RFP\Image0020.tif.frames\Image0020_C001T{}.tif'.format(indice[i]))    
    im = np.array(im) #crea una matriz de valores de la imagen importada
    imarray.append(im.tolist())
    print(i)    
    i+=1
imarray = np.array(imarray)

STD = np.std(imarray, axis=0)
k_medio = np.mean(imarray, axis=0)
B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
B = B.ravel()


bineado = 2500
plt.figure(2)
n,bin_positions_ajuste,p  = plt.hist(B, bins=bineado, color='yellowgreen', density=False)    #esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p
bin_size_ajuste=bin_positions_ajuste[1]-bin_positions_ajuste[0] # calculo el ancho de los bins del histograma
plt.title('M6a - mRFP')
plt.tick_params(which='minor', length=5, width=2)
plt.tick_params(which='major', length=7, width=3)
plt.xlim(0,80)
plt.ylim(1,5000)
plt.yscale('log')

#figManager = plt.get_current_fig_manager()  ####   esto y la linea de abajo me maximiza la ventana de la figura
#figManager.window.showMaximized()   
plt.show()







#a=np.array([
#            [[1,2,3],[14,15,16]],
#            [[7,8,9],[10,11,12]]
#            ])
#
#    
#a1 = np.array([[1,2,3],[4,5,6]])
#
#a2 = np.array([[21,22,23],[24,25,26]])
#
#a3 = np.array([[331,332,333],[334,335,336]])
#
#
#a1 = [a1.tolist()]
#
#i=1
#while i<4:
#    a2 = a2*i
#    a1.append(a2.tolist())
#
#    
#    print(i)    
#    i+=1
#
#a1 = np.array(a1)
#
#
#
#b=a1+a2
#
#
#b=np.concatenate((a1,a2))
#
#b=np.reshape(b,(2,2,3))
#
#

