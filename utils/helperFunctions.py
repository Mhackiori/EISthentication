import numpy as np
from scipy import signal



def smooth(z, windowlength=9, polyorder=3):
    """
    Smoothens the dQ/dV values by applying a filter
    """
    if len(z) > windowlength:
        z_smooth = signal.savgol_filter(z, windowlength, polyorder)
    
    return z_smooth