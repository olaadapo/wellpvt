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

`from wellpvt import Oil`  
     
`oil = Oil(40)`   

`print(oil.api)`    
\>> `40`  

`print(round(oil.calculate_sg(), 3))`    
\>> `0.825`     

`print(round(oil.calculate_density(), 1))`    
\>> `51.5`     

## License
wellpvt is licensed under the MIT License