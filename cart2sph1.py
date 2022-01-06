from math import sqrt, acos, atan2

def cart2sph1(x, y, z):
  r = sqrt(x**2 + y**2 + z**2) + 1e-15
  th = acos(z / r)
  phi = atan2(y, x)

  return r, th, phi