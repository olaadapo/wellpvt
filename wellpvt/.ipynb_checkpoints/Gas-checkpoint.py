import math
from .ProductionSystem import ProductionSystem

class Gas(ProductionSystem):

    def __init__(self, pressure=1500, temperature=50, sg=0.7):

        """
        Generic class to define PVT properties for 
        a single-phase gas in the production system

        Attributes:
            - sg (float) : gas specific gravity
        """

        ProductionSystem.__init__(self, pressure, temperature)
        self.sg = sg
        self.temperature_sc = self.temperature + 460
        self.pc, self.tc = self.calculate_pseudo_critical()
        self.z = self.calculate_z()
        self.density = self.calculate_density()
        self.bg = self.calculate_bg()
        self.viscosity = self.calculate_viscosity()
               
    def set_sg(self, sg):

        """
        Function to change the specific gravity of the gas object

        Args:
            sg (float) : the new specific gravity of the gas object

        Return:
            sg (float) : the updated specific gravity of the gas object
        """

        self.sg = sg

        return self.sg

    def calculate_pseudo_critical(self):

        """
        Function to calculate the gas pseudo-critical properties

        Args:
            None

        Return:
            pc (float) : the gas pseudo-critical pressure (Standing Associated Gas, 2005)
            tc (float) : the gas pseudo-critical temperature (Standing Associated Gas, 2005)
        """

        if self.sg < 0.75:
            pc = 667 + 15 * self.sg - 37.5 * (self.sg**2)
            tc = 168 + 325 * self.sg - 12.5 * (self.sg**2)
        else:
            pc = 706 - 51.7 * self.sg - 11.1 * (self.sg**2)
            tc = 187 + 330 * self.sg - 71.5 * (self.sg**2)

        self.pc = pc
        self.tc = tc

        return self.pc, self.tc

    def calculate_z(self):

        """
        Function to calculate the gas compressibility

        Args:
            None

        Return:
            z (float) : the gas compressibility (Hall-Yarborough)
        """

        pr = self.pressure / self.pc
        tr = self.temperature_sc / self.tc

        t = 1 / tr
        tol = 0.00001
        nmax = 1000

        xi1 = 0.06125 * pr * t * math.exp(-1.2 * (1 - t)**2)

        def aux(x, pr, tr):

            """
            Intermediate function to calculate the Hall-Yarborough gas compressibility

            Args:
                x : initial guess

            Return:
                ffnc : parameter
                dffnc : parameter
            """

            fA = -0.06125 * pr * tr * math.exp(-1.2 * (1 - tr)**2)
            fb = (((1 - x) * x + 1) * x + 1) * x / (1 - x)**3
            fC = -((4.58 * tr - 9.76) * tr + 14.76) * tr * x * x
            fD = ((42.4 * tr - 242.2) * tr + 90.7) * tr * x**(2.18 + 2.82 * tr)

            ffnc = fA + fb + fC + fD

            dA = ((((x - 4) * x + 4) * x + 4) * x + 1) / (1 - x)**4
            db = -((9.16 * tr - 19.52) * tr + 29.52) * tr * x
            dC = (2.18 + 2.82 * tr) * ((42.4 * tr - 242.2) * tr + 90.7) * \
                     tr * x**(1.182 + 2.82 * tr)

            dffnc = dA + db + dC

            return ffnc, dffnc

        for i in range(2, nmax+1):

            fxi, dfxi = aux(xi1, pr, t)
            xi = xi1 - fxi / dfxi

            if (abs((xi - xi1) / xi) < tol) or (abs(fxi) < tol):
                break

            xi1 = xi

        if i > nmax:
            print ("Note: Hall-Yarborough correlation does not converge, use a different method for more accurate results")

        z = 0.06125 * pr * t * math.exp(-1.2 * (1 - t)**2) / xi
        self.z = z

        return self.z         

    def calculate_density(self):

        """
        Function to calculate the gas compressibility

        Args:
            None

        Return:
            z (float) : the gas compressibility (Hall-Yarborough)
        """

        mw = self.sg * 28.97
        density = (self.pressure * mw) / (self.z * 10.732 * self.temperature_sc)
        self.density = density

        return self.density

    def calculate_bg(self):

        """
        Function to calculate the gas formation volume factor

        Args:
            None

        Return:
            bg (float) : the gas formation volume factor
        """

        bg = 0.0282 * self.z * self.temperature_sc / self.pressure
        self.bg = bg 

        return self.bg

    def calculate_viscosity(self):

        """
        Function to calculate the gas viscosity

        Args:
            None

        Return:
            viscosity (float) : the gas viscosity
        """

        mw = self.sg * 28.97
        x = 3.448 + 0.01009 * mw + (986.4 / self.temperature_sc)
        y = 2.447 - 0.2224 * x
        k = ((9.379 + 0.01607 * mw) * self.temperature_sc**1.5) / (209.2 + 19.26 * mw + self.temperature_sc)
        pg = 0.0433 * self.sg * (self.pressure / (self.z * self.temperature_sc))

        viscosity = 0.0001 * k * math.exp(x * pg**y)
        self.viscosity = viscosity

        return self.viscosity