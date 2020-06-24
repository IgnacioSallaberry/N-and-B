# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:21:02 2020

@author: Ignacio Sallaberry
"""
from PIL import Image
import numpy as np
from skimage import io

def Imagenes(name,DIVIDER=2):
    #    
####  ------------------------    PARA UNA IMAGEN    -------------------
    im = Image.open(name)   #importa la imagen .tif
#    im = np.array(im) #crea una matriz de valores de la imagen importada
    im = (np.array(im)/DIVIDER).astype(int) ## los valores de cada pixel de la imagen están divididos por 2 en el simFCS, además tomo la parte entera para que no quede 2.5 por ejemplo
    #creo que ese dividido 2 es el "DIVIDER" del simFCS
    imarray = [im.tolist()]
    print ('001.tif')
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
    i=0
    while i<len(indice):
        im = Image.open(name[:len(name)-7]+indice[i])
        im = (np.array(im)/DIVIDER).astype(int) ## los valores de cada pixel de la imagen están divididos por 2 en el simFCS, además tomo la parte entera para que no quede 2.5 por ejemplo
        imarray.append(im.tolist())
        print(indice[i])    
        i+=1
    imarray = np.array(imarray)  ##esto convierte los datos en matrices
    
    return imarray


def stack_de_imagenes(name, DIVIDER=2, bits=np.uint16):
    im = (((io.imread(name)).astype(bits))/DIVIDER).astype(int)

    imagenes = [(im[0]).tolist()]
    i=0
    while i<len(im):
        imagenes.append((im[i]).tolist())
        i+=1
            
    imagenes = np.array(imagenes) 
    
    return np.array(imagenes)


def selector_de_imagenes(stack, primera_imagen=0, cantidad_de_imagenes=1, intervalo=1):

    imagenes = [(stack[primera_imagen]).tolist()]
    print(f'imagen{primera_imagen}')
    i=0
    j=intervalo
    while i<cantidad_de_imagenes-1:
        imagenes.append((stack[j]).tolist())
        print(f'imagen{j}')
        j+=intervalo
        i+=1
            
    imagenes = np.array(imagenes) 
    
    return np.array(imagenes)

