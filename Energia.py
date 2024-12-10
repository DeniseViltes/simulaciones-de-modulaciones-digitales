import numpy as np

def energiaDeSimbolo_ASK(d,M):
    return d**2/12 *(M**2 -1)

def energiaDeSimbolo_QAM(d,M):
    return d**2/6 *(M -1)

def energiaDeSimbolo_PSK(d,M):
    return d**2/(4 *np.sin(np.pi/M)**2)

def energiaDeSimbolo_FSK(d,M):
    return d**2/2
