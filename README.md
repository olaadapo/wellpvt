Simple computations on single- and multi-phase properties of fluids ( Oil and Gas ) in a production system.

## Installation
`$ pip install wellpvt`

## Project Highlights
Sinlge-phase properties of Oil ( Density, Specific Gravity ) and Gas ( Pseudo-critical Properties, Compressibility, Density, Formation Volume Factor, Viscosity ) are live. 

The development of the features are on-going, and the README will be updated as features are added.

## Usage
```
# From package, import class to define the Oil produced
from wellpvt import Oil

# Declare an instance of the single-phase Oil
# Parameter passed in is the Oil API Gravity
oil = Oil(40)   

# This is included as a property of the Oil instance
print(oil.api)    
40  

# Calculate the Specific Gravity from the API
print(round(oil.calculate_sg(), 3)) 
0.825     

# Calculate the Oil Density from the API + Specific Gravity
print(round(oil.calculate_density(), 1))
51.5
```

## License
`wellpvt` is licensed under the MIT License
