import numpy as np
from scipy.special import wofz

# Voigt profile used in models.py
def voigt_profile(x, sigma, gamma):
    z = (x + 1j*gamma)/(sigma*np.sqrt(2))
    return np.real(wofz(z))/(sigma*np.sqrt(2*np.pi))

# demo parameters
sigma = 1.0
gamma = 0.5
x = np.linspace(-200,200,200001)
V = voigt_profile(x, sigma, gamma)
peak = V.max()
area = np.trapz(V, x)
print(f"sigma={sigma}, gamma={gamma}")
print(f"voigt peak (unit area normalization) = {peak:.8e}")
print(f"voigt area = {area:.8e}")

# If amplitude is intended as peak, scale factor to achieve amplitude A is A/peak
A = 2.0
scaled = (A/peak) * V
print(f"scaled peak (should equal A={A}) = {scaled.max():.8e}")
print(f"scaled area = {np.trapz(scaled,x):.8e}")
