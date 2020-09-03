# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:56:42 2020

@author: Ignacio Sallaberry
"""
import matplotlib.pyplot as plt
from matplotlib import colors
#==============================================================================
#                                Graficos
#==============================================================================  
def plot_signal(x, xlabel, ylabel, titulo):
    f, ax = plt.subplots()
    ax.plot(x)
    ax.set_xlabel(f'{xlabel}')
    ax.set_ylabel(f'{ylabel}')
    ax.tick_params(which='minor', length=5, width=2)
    ax.tick_params(which='major', length=7, width=3)
    return ax

def plot_2D(x, xlabel, ylabel, titulo,label_colorbar):
    f, ax = plt.subplots()
    ax.imshow(x.reshape(256,256))
    ax.set_xlabel(f'{xlabel}')
    ax.set_ylabel(f'{ylabel}')
    ax.set_title(f'{titulo}')
    f.colorbar(ax.imshow(x.reshape(256,256)), orientation='vertical', format='%.0e', label=label_colorbar)
    ax.tick_params(which='minor', length=5, width=2)
    ax.tick_params(which='major', length=7, width=3)
    return ax
    
def plot_hist(x, bins, density, xlabel, ylabel, titulo):
    f, ax = plt.subplots()
    ax.hist(x, bins=bins, density=density)
    ax.set_xlabel(f'{xlabel}')
    ax.set_ylabel(f'{ylabel}')
    ax.set_title(f'{titulo}')
    ax.tick_params(which='minor', length=5, width=2)
    ax.tick_params(which='major', length=7, width=3)
    return ax

def plot_hist2d (x, y, bins, xlabel, ylabel, titulo, label_colorbar):
    f, ax = plt.subplots()
    AX = ax.hist2d(x, y, bins=bins, range=[[min(x),max(x)],[min(y),max(y)]], norm=colors.LogNorm())
    ax.set_xlabel(f'{xlabel}')
    ax.set_ylabel(f'{ylabel}')
    ax.tick_params(which='minor', length=5, width=2)
    ax.tick_params(which='major', length=7, width=3)
    f.colorbar(AX[3], ax=ax, label=label_colorbar)
    return ax
