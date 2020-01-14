class Oil:

    def __init__(self, api=58):

        """
        Generic class to define PVT properties for 
        a single-phase oil produced

        Attributes:
            - api (float) : oil API gravity 
        """

        self.api = api
        self.sg = self.calculate_sg()
        self.density = self.calculate_density()

    def set_api(self, api):

        """
        Function to change the API gravity of the oil object

        Args:
            api (float) : the new API gravity of the oil object

        Return:
            api (float) : the updated API gravity of the oil object
        """

        self.api = api

        return self.api

    def calculate_sg(self):

        """
        Function to calculate the specific gravity of the oil produced

        Args:
            None

        Return:
            sg (float) : the specific gravity of the oil produced
        """

        sg = 141.5 / (self.api + 131.5)
        self.sg = sg

        return self.sg      

    def calculate_density(self):

        """
        Function to calculate the single-phase density of the oil produced

        Args:
            None

        Return:
            density (float) : the single-phase density of the oil produced
        """

        density = self.sg * 62.4
        self.density = density

        return self.density  