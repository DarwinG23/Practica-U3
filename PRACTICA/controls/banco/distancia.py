import pandas as pd
import numpy as np

class Distancia:
    def calcularDistancia(self, lon1, lat1, lon2, lat2):
        
        
        lon1 = np.radians(float(lon1))
        lat1 = np.radians(float(lat1))
        lon2 = np.radians(float(lon2))
        lat2 = np.radians(float(lat2))

        r = 6371
        
        
        dlon = np.subtract(lon2, lon1)
        dlat = np.subtract(lat2, lat1)

        a = np.add(np.power(np.sin(np.divide(dlat, 2)), 2),
                np.multiply(np.cos(lat1),
                            np.multiply(np.cos(lat2),
                                        np.power(np.sin(np.divide(dlon, 2)), 2))
                            )
                )
        c = np.multiply(2, np.arcsin(np.sqrt(a)))

        return c*r