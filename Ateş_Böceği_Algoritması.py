#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:04:10 2022

@author: barisbalci
"""

import math
from random import random
import numpy as np

#İTERASYON SÜRECİ
for t in range(0,durma_kriteri):

#ATEŞ BÖCEKLERİNİN KONUMLARININ  GÜNCELLENME SAFHASI
#her Bir iterasyonda rassallık ölçeğinin yenilenmesi(Alfa[0,1] aralığında sabit bir deger de alınabilir.)
#alfa0: başlangıç rassallık ölçeği
#delta:soğutma faktörü

        alfa=alfa0*(delta**(1/t))
        
        for k in range(0,fn):
            for j in range(0,fn):
                
#her bir ateş böçeğinin kendisinden daha parlak olan ateş böçeğine doğru uçması
    if(IX[0][j]<Ix[0][k])#(minimizasyon problemi olması nedeniyle amaç fonksiyonu (yoğunluğu)küçük olan daha iyi durumdadır)
#toplam_r: ateşböçekleri arasındaki toplam mesafenin karesi(geçici toplam olarak kullanılmıştır )
#uzaklık: ateşböcekleri arasındaki her bir tasarım değişkenine ait mesafenin karesi

    ts=..
    toplam_r=0
    for p in range(0,ts):
        uzaklık[0][p]=(OPT[p][k]-OPT[p][j])**2
        toplam_r=toplam_r+uzaklık[0][p]
        
#beta0:minimum (r{k}{j}=0)çekicilik değeri
#gama: ışık emilim katsayısı

    r[k][j]=mathçsqrt(toplam_r)
    beta[0][j]=beta0*math.exp(1)**(gama*(r[k][j]**2))
    
    X1new=OPT[0][k]+beta[0][j]*(OPT[0][j]-OPt[0][k]+alfa*
(random()-0.5)
    X2new=OPT[1][k]+beta[0][j]*(OPT[1][j]-OPT[1][k]+alfa*
(random()-0.5)

        ......
        
        else:
            X1new=OPT[0][k]+alfa*(random()-0.5)
            X2new=OPT[1][k]+alfa*(random()-0.5)
            
            
#ışık yoğunluğunu güncellenmesi
#// FA'da diğer bazı algoritmalardan faarklı olarak aday çözümlerin kıyaslanabilmesiiçin ışık yoğunluğu değerleri de güncellenmektedir.

    Ix[0][k]=OPT[AF][k]
    
#Tüm ateş böcekleri iterasyonlar sonucunda elde edilen en iyi çözümün amaç fonksiyonu değeri
#sira: güncellenen OPT matrisinde bu çözümün yer aldığı vektör 
deger=min (OPT[AF][:])
sira=np.argmin(OPT[AF])











