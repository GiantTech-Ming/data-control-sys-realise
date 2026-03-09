# control/irrigation.py
# 自动灌溉逻辑模块

class Irrigation:
    def control(self, soil_moisture):
        if soil_moisture < 30:
            print("Starting irrigation...")
        else:
            print("Soil moisture is sufficient.")