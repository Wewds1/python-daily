


def launch_fuel(payload):
    mass = payload
    left = 0
    
    while True:
        fuel = mass / 5
        extra = fuel - left
        if extra < 1:
            return round(fuel, 1)
        mass = payload + fuel
        left = fuel

print(launch_fuel(50))
