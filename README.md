# wellpvt package

Define pressure and temperature of a producing well, and get PVT properties of oil and gas produced.

## package highlights:
- single-phase properties
    - oil: density, specific gravity
    - gas: pseudo-critical properties, compressibility, density, formation volume factor, viscosity
- multiphase mixture properties TBA

## example usage
from wellpvt import Oil

oil = Oil(40) # input oil API

print(oil.api)
\>> 40
print(round(oil.calculate_sg(), 3))
\>> 0.825
print(round(oil.calculate_density(), 1))
\>> 51.5