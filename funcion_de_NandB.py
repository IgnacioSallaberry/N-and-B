# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:21:58 2020

@author: Ignacio Sallaberry
"""
import numpy as np

def NandB (imarray,calibration='Photon Count'):

#==============================================================================
#                                CALIBRACION DE DETECTOR
#==============================================================================    
    if calibration == 'Photon Count':
        detector_offset = 0
        S_factor = 1
        sigma_cero = 0
    
#    elif calibration == 'UNSAM':
#        detector_offset = 0.197
#        S_factor = 4.008
#        sigma_cero = 0.002
    
    else:
        detector_offset = np.float(input ("Enter Offset value :"))
        S_factor = np.float(input ("Enter S value :"))
        sigma_cero = np.float(input ("Enter Sigma_0  value :"))
        
    
    STD = np.std(imarray, axis=0)   #axis=0   recorre en profundidad la matriz en 3D----> numpy.sum(matriz, axis=0)
    k_medio = np.mean(imarray, axis=0)
    VAR=np.var(imarray, axis=0)


#    B = np.divide((STD**2+sigma_cero**2)*S_factor**2,(k_medio+detector_offset)*S_factor)
    B = np.divide((VAR+sigma_cero**2)*S_factor,(k_medio+detector_offset))
#    B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
#    B = np.divide(VAR-sigma_cero**2,k_medio-detector_offset)     ## var = std**2
    
 
    B = B.ravel()   #esto hace que el array de matrices se haga simplemente una array de valores del brillo
    k_medio = k_medio.ravel()
    
    i=0
    while i<len(B):
        if np.isnan(B[i]):
            B[i]=float(np.nan_to_num(B[i]))
            i+=1
        else:
            i+=1
            
    return(STD, k_medio, B, VAR)




#def NandB_MAV (imarray,calibration='LELOIR'):
#
##==============================================================================
##                                CALIBRACION DE DETECTOR
##==============================================================================    
#    if calibration == 'Photon Count':
#        detector_offset = 0
#        S_factor = 1
#        sigma_cero = 0
#    
#    elif calibration == 'UNSAM':
#        detector_offset = 0.197
#        S_factor = 4.008
#        sigma_cero = 0.002
#    
#    else:
#        detector_offset = np.float(input ("Enter Offset value :"))
#        S_factor = np.float(input ("Enter S value :"))
#        sigma_cero = np.float(input ("Enter Sigma_0  value :"))
#    
#    
#    STD = np.std(imarray, axis=0)   #axis=0   recorre en profundidad la matriz en 3D----> numpy.sum(matriz, axis=0)
#    k_medio = np.mean(imarray, axis=0)
#    VAR=np.var(imarray, axis=0)
#
##    B = np.divide((STD**2+sigma_cero**2)*S_factor**2,(k_medio+detector_offset)*S_factor)
#    B = np.divide((VAR+sigma_cero**2)*S_factor**2,(k_medio+detector_offset)*S_factor)
##    B = np.divide(STD**2-sigma_cero**2,k_medio-detector_offset)
##    B = np.divide(VAR-sigma_cero**2,k_medio-detector_offset)     ## var = std**2
#    
#    B = B.ravel()   #esto hace que el array de matrices se haga simplemente una array de valores del brillo
#    
#    return(STD, k_medio, B, VAR)

### función para saber si la imagen que cargamos está en RGB o en escala de grises
def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b: return False
    return True

