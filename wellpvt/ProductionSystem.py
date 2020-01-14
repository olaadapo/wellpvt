class ProductionSystem:

    
    def __init__(self, pressure=1500, temperature=50):
        
        """
        Generic class to define specs for a well with fluids 
        produced, given the wellhead pressure and temperature 
        for the system

        Attributes:
            - pressure (float) : the wellhead pressure in psia
            - temperature (float) : the wellhead temperature in deg. F
        """
        
        self.pressure = pressure
        self.temperature = temperature
                
    def set_pressure(self, pressure):
        
        """
        Function to change the pressure of the production system
        object
        
        Args:
            pressure (float) : the new pressure of the production system object
            
        Return:
            pressure (float) : the updated pressure of the production system object
        """
            
        self.pressure = pressure
        
        return self.pressure
    
    def set_temperature(self, temperature):
        
        """
        Function to change the temperature of the production system
        object
        
        Args:
            temperature (float) : the new temperature of the production system object
            
        Return:
            temperature (float) : the updated temperature of the production system object
        """
        
        self.temperature = temperature
        
        return self.temperature