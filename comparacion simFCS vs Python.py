# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:56:12 2020

@author: Ignacio Sallaberry
"""
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\ETCasa\Desktop\Proyecto N&B\New folder')    #buscar carpeta donde está el archivo funcion_de_NandB.py
from graficos import *
import matplotlib.ticker as mtick
#==============================================================================
#                                Tipografía de los gráficos
#==============================================================================    
SMALL_SIZE = 28
MEDIUM_SIZE = 32
BIGGER_SIZE = 34
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#==============================================================================    
#==============================================================================    
plt.close('all')

frame1_simFCS = abrir_datos(r'C:\Users\ETCasa\Nextcloud\mRFP0027 calib LELOIR - sin detrend - DIVIDER 2\Frame_1_mRFP_simFCS_sin_calib_sin_detrend.txt')
plt.figure()
plt.imshow(k_medio_mRFP.reshape(256,256))
plt.xlabel(r'píxel')
plt.ylabel(r'píxel')
plt.title('Intensidad \n media')
plt.show()
#==============================================================================
#                                funcion "abrir datos"
#==============================================================================  
def abrir_datos(name):
    with open(name) as fobj:
        datos = fobj.read()
    
    datos = re.split('\n', datos)
    datos.remove('')
    i=0
    while i<len(datos):
        datos[i]=np.float(datos[i])
        i+=1
    datos=np.asarray(datos)
    return datos    


#with open(r'C:\Users\ETCasa\Desktop\B_simFCS.txt') as fobj:
#    B_simFCS = fobj.read()
#B_simFCS  = re.split('\n', B_simFCS )
#B_simFCS.remove('')
#B_simFCS  = [float(i) for i in B_simFCS]
#B_simFCS = np.array(B_simFCS)

#==============================================================================
#                                Datos
#==============================================================================  
### datos - simFCS
Brillo_simFCS = abrir_datos(r'C:\Users\ETCasa\Desktop\NandB - datos para comparacion simFCS - Python\M6a\B_M6a_mRFP_0020.txt')

### datos - Python
imarray_mRFP = Imagenes(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\M6a RFP\Image0020.tif.frames\Image0020_C001T001.tif')
STD_mRFP, k_medio_mRFP, B_mRFP, VAR_mRFP = NandB(imarray_mRFP, calibration='LELOIR')

### calculo B_resta
B_resta = Brillo_simFCS-B_mRFP
#==============================================================================
#                                Graficos
#==============================================================================  
plt.figure()
plt.imshow(k_medio_mRFP.reshape(256,256))
plt.xlabel(r'píxel')
plt.ylabel(r'píxel')
plt.title('Intensidad \n media')
plt.show()


ax = plot_signal(B_resta,r'píxel',r'$B_{resta} = B_{simFCS} - B_{python}$', 'B resta')
ax.plot(B_resta)
plt.tight_layout()
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.e'))
plt.show()

ax = plot_2D(B_resta,'pixel','pixel','', r'$B_{resta}$')
ax.plot(B_resta.reshape(256,256))
#ax.colorbar(orientation='vertical', format='%.0e')
plt.tight_layout()
plt.show()

ax = plot_hist(B_resta, 256, False, r'$B_{resta} = B_{simFCS} - B_{python}$', 'cuentas','B resta')
ax.plot()
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.e'))
#plt.tight_layout()
plt.show()

ax = plot_hist2d(k_medio_mRFP, B_mRFP, 256, r'<I>', r'B', r'B vs <I>', 'Cuentas')
ax.plot()
plt.tight_layout()
plt.show()












































































plt.figure()
plt.imshow(B_resta.reshape(256,256))
plt.colorbar(orientation='vertical', format='%.0e')
plt.show()

plt.figure()
plt.plot(B_resta)
plt.xlabel(r'píxel')
plt.ylabel(r'$B_{resta} = B_{simFCS} - B_{python}$')
plt.show()

plt.figure()
plt.hist(B_resta, density=False)
plt.ylabel('cuentas')
plt.xlabel(r'$B_{resta} = B_{simFCS} - B_{python}$')
plt.show()

plt.figure()
plt.hist2d(k_medio_mRFP.ravel(),B_mRFP,bins=256,
           range=[[min(k_medio_mRFP.ravel()), max(k_medio_mRFP.ravel())], [min(B_mRFP), max(B_mRFP)]],
           norm=colors.LogNorm())
plt.colorbar(orientation='vertical')
plt.ylabel(r'$B$')
plt.xlabel(r'$<I>$')
plt.show()



imarray_mRFP_0028 = Imagenes(r'C:\Users\ETCasa\Nextcloud\UNSAM\UNSAM 28-11 EXP 3 y 4\Experimento 4\Neuronas\RFP citoplasmática\Image0028.tif.frames\Image0028_C001T001.tif')
STD_mRFP_0028, k_medio_mRFP_0028, B_mRFP_0028, VAR_mRFP_0028 = NandB(imarray_mRFP_0028, calibration='LELOIR')


with open(r'C:\Users\ETCasa\Desktop\B_simFCS_0028.txt') as fobj:
    B_simFCS_0028 = fobj.read()
B_simFCS_0028 = re.split('\n', B_simFCS_0028 )
B_simFCS_0028.remove('')
B_simFCS_0028  = [float(i) for i in B_simFCS_0028]
B_simFCS_0028 = np.array(B_simFCS_0028)

with open(r'C:\Users\ETCasa\Desktop\K_simFCS_0028.txt') as fobj:
    K_simFCS_0028 = fobj.read()
K_simFCS_0028 = re.split('\n', K_simFCS_0028 )
K_simFCS_0028.remove('')
K_simFCS_0028  = [float(i) for i in K_simFCS_0028]
K_simFCS_0028 = np.array(K_simFCS_0028)
#==============================================================================
#                               datos
#==============================================================================   
#frame1_simFCS = abrir_datos(r'C:\Users\ETCasa\Nextcloud\mRFP0027 calib LELOIR - sin detrend - DIVIDER 2\Frame_1_mRFP_simFCS_sin_calib_sin_detrend.txt')
#
#Brillo_simFCS = abrir_datos(r'C:\Users\ETCasa\Nextcloud\mRFP0027 calib LELOIR - sin detrend - DIVIDER 2\B_mRFP_simFCS_sin_calib_sin_detrend.txt')
#

B_resta = B_simFCS_0028-B_mRFP_0028
#==============================================================================
#                                Graficos
#==============================================================================  
plt.figure()
plt.imshow(B_resta.reshape(256,256))
plt.colorbar(orientation='vertical', format='%.5f')
plt.show()

plt.figure()
plt.plot(B_resta)
plt.xlabel(r'píxel')
plt.ylabel(r'$B_{resta} = B_{simFCS} - B_{python}$')
plt.show()

plt.figure()
plt.hist(B_resta, bins=256, density=False)
plt.ylabel('cuentas')
plt.xlabel(r'$B_{resta} = B_{simFCS} - B_{python}$')
plt.show()














