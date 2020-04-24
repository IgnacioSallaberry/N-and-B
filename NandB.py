# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:06:58 2020

@author: Ignacio Sallabery
"""
import numpy as np
from PIL import Image

import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.stats import norm
import matplotlib.mlab as mlab


import sys
sys.path.append(r'C:\Users\ETCasa\Desktop\New folder')    #buscar carpeta donde está el archivo funcion_de_NandB.py


from funcion_de_NandB import NandB




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
#                                STD - k_medio - Brillo
#==============================================================================  
STD_mRFP, k_medio_mRFP, B_mRFP, imarray_mRFP = NandB(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\RFP citoplasmática\Image0027.tif.frames\Image0027_C001T001.tif')
STD_M6a, k_medio_M6a, B_M6a, imarray_M6a = NandB(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\M6a RFP\Image0020.tif.frames\Image0020_C001T001.tif')


#==============================================================================
#                                Gráficos mRFP
#==============================================================================  
plt.figure()
#plt.hexbin(k_medio.ravel(),B)
plt.hist2d(k_medio_mRFP.ravel(),B_mRFP,bins=500,range=[[min(k_medio_mRFP.ravel()), max(k_medio_mRFP.ravel())], [min(B_mRFP), max(B_mRFP)]],
           norm=colors.LogNorm())
plt.show()


bineado = 5000
plt.figure()
#bineado = 'fd'
n,bin_positions_ajuste,p  = plt.hist(B_mRFP, bins=bineado, color='lightsalmon', density=False)    #esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p
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

#==============================================================================
#                                Gráficos M6a
#==============================================================================  
plt.figure()
#plt.hexbin(k_medio.ravel(),B)
plt.hist2d(k_medio_M6a.ravel(),B_M6a,bins=500,range=[[min(k_medio_M6a.ravel()), max(k_medio_M6a.ravel())], [min(B_M6a), max(B_M6a)]],
           norm=colors.LogNorm())
plt.show()

bineado = 2500
plt.figure()
n,bin_positions_ajuste,p  = plt.hist(B_M6a, bins=bineado, color='yellowgreen', density=False)    #esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p
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
#impor
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
##
#b=np.reshape(b,(2,2,3))
##
#print(np.sum(b,axis=0))
##
#print(np.sum(b,axis=1))
##
#print(np.sum(b,axis=2))

