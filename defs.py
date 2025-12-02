import numpy as np

A = 1.78    # Deep ice index of refraction
B = 1.27   # Snow index of refraction
C = 37.25  # Exponential scale depth

def ior_exp1(z):
    """
    Single exponential ice model adapted from greenland_simple in NuRadioMC.

    Parameters
    __________
    z : float or 1D numpy array (n,)

    Returns
    _______
    n : float or 1D numpy array (n,)
    """
    def iorfunc(z):
        return A - (A - B) * np.exp(z / C)

    if isinstance(z, np.ndarray):
        iorvals = iorfunc(z)
        iorvals[z > 0] = 1.0
        return iorvals
    
    else:
        if z > 0:
            return 1.0
        else:
            return iorfunc(z)

def grad_ior_exp1(z):
    """
    Depth derivative of single exponential ice model.

    Parameters
    __________
    z : float or 1D numpy array (n,)

    Returns
    _______
    dn/dz : float or 1D numpy array (n,)
    """
    
    def grad_iorfunc(z):
        return (B - A) / C * np.exp(z / C)
    
    if isinstance(z, np.ndarray):
        grad_iorvals = grad_iorfunc(z)
        grad_iorvals[z > 0] = 0
        return grad_iorvals
    
    else:
        if z > 0:
            return 0
        else:
            return grad_iorfunc(z)      
