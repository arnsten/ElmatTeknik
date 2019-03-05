import numpy as np
import math as math


x = lambda a, b, c : a + b + c

def effekt_Lodstation(t_heat):
    T = 20 /1000
    w = 2*math.pi*50
    Vut = 56.88/1000
    Im = 0.6 #- 10 * Vut + 24.4
    print(Im)
    K = 230*(Im/2)*math.sqrt(2)/(T*2)
    integral2 = lambda a: math.sin(2*w*a)/(2*w)
    p = K * ((T-t_heat)-t_heat - (integral2(T-t_heat) - integral2(t_heat)))
    return p
#print(effekt_Lodstation(6.7/1000))
#print(effekt_Lodstation(5.27/1000))
#print(effekt_Lodstation(1.2/1000))

def effekt_LED():
    t_led = 7/1000
    T = 20/1000
    Va = 230*math.sqrt(2)
    Ia = 12.1
    w = 2*math.pi*50
    integral = lambda a, b, f: f(b) - f(a)
    K1 = -Va*2*1730.0 / (T * w * w)
    integral1 = lambda t: math.sin(w*t) - w*math.cos(w*t)
    K2 = -2*Va*Ia / (T*w)
    integral2 = lambda t: math.cos(w*t)
    p = K1 * integral(0,t_led,integral1) + K2 * integral(0,t_led,integral2)
    return p

print(effekt_LED())

