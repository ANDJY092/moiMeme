# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 08:24:43 2025

@author: Elève
"""
def funA(n):
    if n==0:
        return 0
    return n+funA(n-1)
"""cette fonction calcule la somme des n premiers entiers =n*(n+1)//2 
erreur si n: n'est pas entier,est negatif"""
 
import turtle as tl
def funB(n):
    if n>=200:
        return
    else:
        tl.fd(n)
        tl.rt(90)
        tl.fd(n)
        tl.rt(90)
        funB(n+10)
        tl.exitonclick()
  
