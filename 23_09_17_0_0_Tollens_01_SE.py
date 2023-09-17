# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 07:16:53 2023

@author: Gadiel Jimenez
"""

def modus_tollens(p, q):
    """

    Args:
        p (bool): La premisa p.
        q (bool): La consecuencia q.

    Returns:
        bool: El resultado de la inferencia.
    """
    if not q:
        if p is True and q is False:
            return True  # Si q es falso y p implica q, entonces p es falso
        else:
            return False  # Si q es falso pero la relación p implica q no es cierta, la inferencia no puede realizarse
    else:
        return True  # Si q es verdadero, la inferencia es verdadera ya que no hay condición que incumplir

# Definición de la premisa y la negación de la consecuencia
premisa_p = True
negacion_consecuencia_q = True

# Aplicación de Modus Tollens
resultado_inferencia = modus_tollens(premisa_p, negacion_consecuencia_q)

# Mostrar el resultado
if resultado_inferencia:
    print("Se cumple el Modus Tollens: p es falso.")
else:
    print("No se cumple el Modus Tollens: no se puede determinar si p es falso.")
