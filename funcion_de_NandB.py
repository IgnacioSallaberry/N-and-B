# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:21:58 2020

@author: ETCasa
"""
import numpy as np
from PIL import Image


def NandB (name):

#==============================================================================
#                                CALIBRACION DE DETECTOR
#==============================================================================    
    detector_offset = 0
    S_factor = 1
    sigma_cero = 0
    
    #detector_offset = 0.197
    #S_factor = 4.008
    #sigma_cero = 0.002
    
    
####  ------------------------    PARA UNA IMAGEN    -------------------
    im = Image.open(name)   #importa la imagen .tif
    im = np.array(im) #crea una matriz de valores de la imagen importada
    imarray = [im.tolist()]
####  ------------------------    armo los nombres de los archivos    -------------------
    i=2
    indice=[]
    while i<101:
        if i<10:
            indice.append(f'00{i}.tif')
        elif 9<i<100:
            indice.append(f'0{i}.tif')
        else:
            indice.append(f'{i}.tif')
        i+=1
####  ------------------------    armo array con las matrices de las 100 imágenes  -------------------
    i=1
    while i<len(indice):
        im = Image.open(name[:len(name)-7]+indice[i])
        im = np.array(im) #crea una matriz de valores de la imagen importada
        imarray.append(im.tolist())
        print(i)    
        i+=1
    imarray = np.array(imarray)
    
    STD = np.std(imarray, axis=0)   #axis=0   recorre en profundidad la matriz en 3D----> numpy.sum(matriz, axis=0)
    k_medio = np.mean(imarray, axis=0)
    B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
    B = B.ravel()   #esto hace que el array de matrices se haga simplemente una array de valores del brillo
    
    return(STD, k_medio, B, imarray)




def NandB_detrend (name):

    
#==============================================================================
#                                CALIBRACION DE DETECTOR
#==============================================================================    
    detector_offset = 0
    S_factor = 1
    sigma_cero = 0
    
    #detector_offset = 0.197
    #S_factor = 4.008
    #sigma_cero = 0.002
    
    
    STD = np.std(imarray, axis=0)
    k_medio = np.mean(imarray, axis=0)
    B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
    B = B.ravel()   #esto hace que el array de matrices se haga simplemente una array de valores del brillo
   
    
    return(STD, k_medio, B)
