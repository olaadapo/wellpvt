Define pressure and temperature of a producing well, and get PVT properties of oil and gas produced.

## Installation
`$ pip install wellpvt`

## Project Highlights
- single-phase properties
    - **oil**: density, specific gravity
    - **gas**: pseudo-critical properties, compressibility, density, formation volume factor, viscosity
- multiphase mixture properties TBA

## Example Usage
define produced oil with 40 deg. API  

```
# Create a class to define the oil produced
from wellpvt import Oil

# Declare an instance of the single-phase oil
# Parameter passed in is the oil API Gravity
oil = Oil(40)   

# This is included as a property of the oil instance
print(oil.api)    
40  

# Calculate the Specific Gravity from the API
print(round(oil.calculate_sg(), 3)) 
0.825     

# Calculate the oil Density from the API + Specific Gravity
print(round(oil.calculate_density(), 1))
51.5
```

## License
wellpvt is licensed under the MIT License
