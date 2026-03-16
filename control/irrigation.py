# control/irrigation.py


class Irrigation:
    def control(self, soil_moisture):
        if soil_moisture < 30:
            print("Starting irrigation...")
        else:
            print("Soil moisture is sufficient.")